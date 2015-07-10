# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
# helper functions

def number_to_name(number):
    # fill in your code below
    name = -1
    if(number == 0):
        name = "rock"
    elif(number == 1):
        name = "spock"
    elif(number == 2):
        name = "paper"
    elif(number == 3):
        name = "lizard"
    elif(number == 4):
        name = "scissors"
    return name
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    number = -1
    if( name == "rock"):
        number = 0
    elif(name == "spock"):
        number = 1
    elif(name == "paper"):
        number = 2
    elif(name == "lizard"):
        number = 3
    elif(name == "scissors"):
        number = 4
    else: 
        print "Please input the right name!"
        number = -1
    return number
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    print "Player choose",name
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    print "Computer choose",number_to_name(comp_number)
    
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number)%5

    # use if/elif/else to determine winner
    if(diff == 0 ):
        print "Player and computer ties!\n"
    elif( diff <= 2 and diff > 0):
        print "Player wins!\n"
    elif( diff <= 4 and diff > 2):
        print "Computer wins!\n"
    
# test your code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


