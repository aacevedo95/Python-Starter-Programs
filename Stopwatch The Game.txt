# "Stopwatch: The Game!"
# Good luck!
import simplegui

# define global variables
attempts = 0
font = 20
score = 0
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def convert_units(t):
    result = str(t)
    result = result
    return result

def format(t):
    global message
    minutes = int(t // 1000)
    seconds =  int(t // 10 )
    tenths = int(t %10)
    
    # converting to strings
    minutes_string = convert_units(minutes)
    seconds_string = convert_units(seconds)
    tenths_string = convert_units(tenths)
    
    # return string
    if minutes == 0 and seconds == 0 and tenths == 0:
        return "0:00.0"
    elif t < 100:
        return minutes_string + ":0" + seconds_string + "." + tenths_string
    elif t > 100:
        return minutes_string + ":" + seconds_string + "." + tenths_string
    elif minutes == 0:
        return "0:" + seconds_string + "." + tenths_string
    elif seconds == 0:
        return minutes_string + ":0." +tenths_string
    else:
        return minutes_string + ":" + seconds_string + "." + tenths_string
      
# define event handler for buttons
def start():
    timer.start()

def stop():    
    global attempts, score    
    attempts += 1  
    if timer.is_running():
        if time %10 == 0:
            score += 1
        timer.stop()
        
def reset():
    global time, attempts, score
    time = 0
    score = 0
    attempts = 0
    timer.stop()
    
def tick():
    global time
    time += 1

def increment():
    global time
    return str(format(time))
           
# define event handler for timer with 0.1 sec interval
def timer_handler():
    timer  = simplegui.create_timer(100, tick)

# define draw handler
def draw(canvas):
    
    x = (200 - frame.get_canvas_textwidth(increment(), font)) /2
    y = (200 / 2) + (font / 3.75)
    canvas.draw_text(increment(),[x,y], font, "White")
    canvas.draw_text("Score: "+str(score), [130, 30], 15, "Yellow")
    canvas.draw_text("Attempts: "+str(attempts), [120,50], 15, "Yellow")

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
frame.add_button("Start", start,100)
frame.add_button("Stop", stop,100)
frame.add_button("Reset", reset,100)
timer  = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.set_canvas_background("Black")

# start frame
frame.start()
timer.stop()
