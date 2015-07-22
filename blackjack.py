import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = "Hit or stand?"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def draw_back(self, canvas, pos):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
# define hand class
class Hand:
    def __init__(self):
        self.hand = []  

    def __str__(self):
        cards = ""
        for card in self.hand:
            cards += str(card) + " "
        return cards

    def add_card(self, card):
        self.hand.append(card)
 
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        aces  = 0
        value = 0
        for card in self.hand:
            if card.rank == "A":
                aces += 1
            value += VALUES[card.rank]              
        while (value + 10) <= 21 and aces > 0:
            value += 10
            aces -= 1
        return value
     
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            if i == 5: break
            self.hand[i].draw(canvas, [pos[0] + i * 100, pos[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []  
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                card = Card(SUITS[i], RANKS[j])
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    

    def deal_card(self):
        return self.deck.pop()  # deal a card object from the deck
    
    def __str__(self):
        deck = ""
        for card in self.deck:
            deck += str(card) + " "
        return deck 

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, message, score
    if in_play:
        score -= 1
        outcome = "You quit this round and lose"
        message = "New deal?"
        in_play = False
    else:    
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        # add two cards to player and dealer
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

        in_play = True
        outcome = ""
        message = "Hit or stand?"
    
    print "player: ", player, player.get_value()
    print "dealer: ", dealer, dealer.get_value()
    
def hit():
    global player, deck, outcome, in_play, message, score
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
        value = player.get_value()       
        print "dealer: ", dealer, dealer.get_value()
        print "player: ", player, player.get_value()
        # if busted, assign a message to outcome, update in_play and score 
        if value > 21:               
            outcome = "You went bust and lose"  
            message = "New deal?"
            in_play = False 
            score -= 1
    
def stand():
    global player, dealer, deck, outcome, in_play, message, score   
    if in_play:
        dealerValue = dealer.get_value()    
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealerValue < 17:
            dealer.add_card(deck.deal_card())
            dealerValue = dealer.get_value()
        message = "New deal?"
        in_play = False 
        print "dealer: ", dealer, dealerValue
        print "player: ", player, player.get_value()
        if dealerValue > 21:
            outcome = "Dealer went bust, you win"
            score += 1
        else:
            playValue = player.get_value()
            if playValue <= dealerValue:
                outcome = "Dealer wins"
                score -= 1
            else:
                outcome = "You win"      
                score += 1
        
# draw handler    
def draw(canvas):
    global score, player, dealer, outcome, in_play
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack",[100,80],35,"Yellow")
    canvas.draw_text("Score  " + str(score),[450,80],25,"Black")
    canvas.draw_text("Dealer",[70,150],25,"Black")
    canvas.draw_text(outcome,[300,150],25,"Black")
    canvas.draw_text("Player",[70,380],25,"Black")
    canvas.draw_text(message,[350,380],25,"Black")
    dealer.draw(canvas, [70, 200])
    # the first card of deal is facing down
    dealer.hand[0].draw_back(canvas, [70, 200])
    player.draw(canvas, [70, 430])
    # if the round is over, make the first card face up
    if not in_play:
        dealer.hand[0].draw(canvas, [70, 200])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()