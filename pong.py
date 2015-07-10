# Implementation of classic arcade game Pong
# The "w" and "s" keys control the vertical velocity of the left paddle 
# while the "Up arrow" and "Down arrow" key control the velocity of the right paddle.

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
radius = 15

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH/2,HEIGHT/2]
    if right == True :
        ball_vel = [random.randrange(2,4),-random.randrange(1,3)]
    else:
        ball_vel = [-random.randrange(2,4),-random.randrange(1,3)]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  # these are floats
    global score1, score2  # these are ints
    global right
    # initiate paddles positions and paddles velocity
    paddle1_pos = [HALF_PAD_WIDTH,HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH,HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0 
    score1 = 0
    score2 = 0
    right = random.choice([True, False])
    ball_init(right)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, radius 
    # update paddle's vertical position, keep paddle on the screen        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT],[HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH,"White")                 
    # draw ball 
    c.draw_circle([ball_pos[0],ball_pos[1]],radius,1,"White","White")
    
    # update ball    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #move paddles 
    if paddle1_pos[1] + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT and paddle1_pos[1] + paddle1_vel >= HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    if paddle2_pos[1] + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT and paddle2_pos[1] + paddle2_vel >= HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel

    #ball bounces from the top and bottom    
    if ball_pos[1] <= radius :
        ball_vel[1] = - ball_vel[1]
        
    if ball_pos[1] >= HEIGHT - radius:
        ball_vel[1] = - ball_vel[1]
        
    #ball bounces from left and right
    if ball_pos[0] <= radius + PAD_WIDTH:
        if ball_pos[1] > paddle1_pos[1]-HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos[1]+HALF_PAD_HEIGHT:        
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            ball_init(True)
            score2 += 1
            
    if ball_pos[0] >= WIDTH - radius - PAD_WIDTH:
        if ball_pos[1] > paddle2_pos[1]-HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos[1]+HALF_PAD_HEIGHT:        
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            ball_init(False)
            
            score1 += 1
            
    #draw score
    c.draw_text(str(score1),[180,100],40,"White")
    c.draw_text(str(score2),[380,100],40,"White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -5
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -5            
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 5
  
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0   
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0            
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
      
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()