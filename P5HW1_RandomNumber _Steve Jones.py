# Random Number Guessing Game
# 11-03-2019
# CTI-110 P5HW1 - Random Number
# Steve Jones 
#

# Main Menu
# Guess a random number
# to low or to high guess again
# Would you like to play again


import random
def MainMenu():
    print('1. Play Game')
    print('2. Exit')
    option=int(input('Enter Option: '))
    if 1:
         
        number = random.randint(1, 100)
        while True:
            print ('Guess the number between 1 and 100')
            guess = input()
            num = int(guess)
            if num == number:
                print ('CONGRADULATIONS! YOU GOT IT!')
                print ('would you like to play again?')    
            elif num < number:
                print ('To low, try again.')   
            elif num > number:
                print ('To high, try again.')

MainMenu()
