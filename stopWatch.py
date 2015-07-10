# a simple digital stopwatch that keeps track of the time in tenths of a second. 
# The stopwatch contains "Start", "Stop" and "Reset" buttons. It has two numerical 
# counters that keep track of the number of times that you have stopped the watch 
# and how many times you manage to stop the watch on a whole second (1.0, 2.0, 3.0, etc.). 
# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables

start = False
total_counter = 0
right_counter = 0
counter = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    min = t//600
    sec = (t - 600*min)//10        
    tenth_sec = t%10    
    return str(min) + ":"+str(sec) + "."+ str(tenth_sec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global start
    start = True        

def stop():
    global start, total_counter, right_counter
    start = False
    total_counter += 1
    if counter%10 == 0:
        right_counter += 1
           
def reset():
    global counter 
    counter = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    if start == True:
        counter = counter + 1
   
def stop_watch(canvas):
    global total_counter, right_counter
    canvas.draw_text(str(right_counter)+"/"+str(total_counter),[150,30],20,"Green")
    canvas.draw_text(format(counter),[55,90],30,"White")
    
timer = simplegui.create_timer(100,tick)

# create frame
frame = simplegui.create_frame("StopWatch",200,150)
frame.add_button("Start",start,75)
frame.add_button("Stop",stop,75)
frame.add_button("Reset",reset,75)

# register event handlers
frame.set_draw_handler(stop_watch)

# start timer and frame
frame.start()
timer.start()
# remember to review the grading rubric