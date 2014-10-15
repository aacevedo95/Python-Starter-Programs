# Rock-Paper-Scissors-Lizard-Spock Mini-Project #1:
#"Rock", "Paper", "Scissors", "Lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def number_to_name(number):
    if (number == 0):
        return 'rock!'
    elif number == 1:
        return 'Spock!'
    elif (number == 2):
        return 'paper!'
    elif (number == 3):
        return 'lizard!'
    elif (number == 4):
        return 'scissors!'
    else:
        return "Error in number to name!!"
        
def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"): 
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print "Error in name to number!!"
           
def rpsls(name):
    comp_number =  (random.randrange(0,5))
    player_number =  name_to_number(name)
   
    player_guess = "Player chooses " + name
    print ""
    computer_guess = "Computer chooses " + number_to_name(comp_number)
    
    print player_guess
    print computer_guess
    
    difference = (player_number - comp_number)%5 
    if difference == 1 or difference == 2:
        print "Player Wins!"
    elif (difference == 3) or (difference == 4):
        print "Computer Wins!"
    else:
        print "It's a Tie!"
    return difference
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


