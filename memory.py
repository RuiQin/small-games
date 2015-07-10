# implementation of card ge - Memory
# In Memory, a turn (or a move) consists of the player flipping over two cards. 
# If they match, the player leaves them face up. If they don't match, the player 
# flips the cards back face down. The goal of Memory is to end up with all of the 
# cards flipped face up in the minimum number of turns.

import simplegui
import random

card_list = []
exposed = [False]*16
state = 0
current = -1    #current click
click1 = -1     #the first clilck
click2 = -1     #the second click
count = 0       #the number of moves

# helper function to initialize globals
def init():
    global card_list, count, exposed
    card_list = range(8) + range(8)
    random.shuffle(card_list)
    exposed = [False]*16
    count = 0
    l.set_text("Moves = "+str(count))
     
# define event handlers
def mouseclick(pos):
    global current, state, click1, click2, count
    current = pos[0]//50
    
    if state == 0:
        if exposed[current] == False:
            state = 1
            click1 = current
            exposed[current] = True   
            count += 1
            l.set_text("Moves = "+str(count))
    elif state == 1:
        if exposed[current] == False:
            state = 2
            click2 = current
            exposed[current] = True           
            if card_list[click1] == card_list[click2]:
                exposed[click1] = True
                exposed[click2] = True
                state = 0
    else:
        if exposed[current] == False:
            exposed[current] = True            
            count += 1
            l.set_text("Moves = "+str(count))            
            if card_list[click1] != card_list[click2]:
                exposed[click1] = False
                exposed[click2] = False
                state = 1
            click1 = current

# cards are logically 50x100 pixels in size    
def draw(canvas):

    for i in range(0,800,50):
        canvas.draw_line([i,0],[i,100],1,"Red")
    for i in range(25,800,50):
        canvas.draw_line([i,0],[i,100],49,"Green")
#if the card is exposed, show its number   
    for i in range(16):    
        if exposed[i] == True:
            canvas.draw_line([25+50*i,0],[25+50*i,100],49,"Black")
            canvas.draw_text(str(card_list[i]),[15+50*i,60],30,"White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric