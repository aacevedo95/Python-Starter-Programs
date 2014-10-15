#Guess the number mini-project
import simplegui
import random
import math 

# Global variables used
num_range = 100
secret_number = random.randrange(0,100)
guesses_remaining = 7
max_guesses = 7

#Helper Function
def init():
    global secret_number, max_guesses, guesses_remaining
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is",  max_guesses
    print ""
    if num_range == 100:
        guesses_remaining= 7
    elif num_range == 1000:
        guesses_remaining = 10
  
# Event handlers for control panel
def range100():
    global num_range, max_guesses, secret_number 
    secret_number = random.randrange(1, 100)
    num_range = 100
    max_guesses = 7 
    guesses_remaining = 7
    print "New game. Range is from 0 to 100."
    print "Number of remaining guesses is ", max_guesses
    print ""
       
def range1000():
    global num_range,max_guesses, secret_number 
    secret_number = random.randrange(1, 1000)
    num_range = 1000
    max_guesses = 10
    guesses_remaining = 10
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is ",  max_guesses
    print ""
    
def get_input(guess):
    global secret_number, guesses_remaining,max_guesses
    guesses_remaining -= 1

    if (guesses_remaining >= 0) and (float(guess) == secret_number):
        
        print "Guess was ", guess
        print "Number of remaining guesses is ",  guesses_remaining
        print 'Correct!'
        print ""
        init()
        return
    
    elif guesses_remaining == 0:
        
        print "Guess was ", guess
        print "Number of remaining guesses is ",  guesses_remaining
        print 'You ran out of guesses. The number was', secret_number 
        print ""
        init()
        return
    
    elif float(guess) < secret_number:
        print "Guess was ", guess
        print "Number of remaining guesses is ",  guesses_remaining
        print "Higher!"
        print ""
        
    elif float(guess) > secret_number:
        print "Guess was ", guess
        print "Number of remaining guesses is ",  guesses_remaining
        print "Lower!"
        print ""
        
    elif float(guess) == secret_number:
        print "Guess was ", guess
        print "Number of remaining guesses is ",  guesses_remaining
        print "Correct!"
        print ""
        init()
        return

# Frame
f = simplegui.create_frame("Guess the number!", 200, 200)

# Event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess.", get_input, 200)

# start frame
init()
f.start()
