from tkinter import *
import time
def printSomething():
    # if you want the button to disappear:
    button.destroy() or button.pack_forget()
    label = Label(root, text= "Welcome to SEEEDS! Copyright (c) 2025 Ronald Petrik \n https://github.com/RonniePetrik/SEEEDS/tree/main \n \n Please Wait!")
    #this creates a new label to the GUI
    label.pack() 

def delete_window(window):
    window.destroy()

root = Tk()
root.geometry("600x600")

button = Button(root, text="Info", command=printSomething) 
button.pack()
root.after(10000, lambda: delete_window(root))
root.mainloop()

#time.sleep(1)
#!/usr/bin/python

#Import time
import time
def SNAKE():
    print('Coming Soon!')
#Start printing the boot up screen.
#time.sleep(7)
#print('                                                                                                                         ')
#time.sleep(1)
#print('                                                                                                        Welcome!'         )
#time.sleep(1)
#print('                                                                                                                         ')
#time.sleep(1)
#print('                                                                                                                       ')
#time.sleep(1)
#print('                                                                                                                       ')
#time.sleep(1)
#print('                                                                                                                                    ')
#time.sleep(1)
#print('                                                                                                                         ')
#time.sleep(1)

time.sleep(1)
#import random and string (used later)
import random
import string
import sys
print('\n')
#print('                                                                                   Welcome to SEEEDS, Version 7.9.2.0.1                          ')
#time.sleep()
#sys.stdout.write("\033[K") # Clear the current line
#sys.stdout.write("\033[F") # Move cursor to the beginning of the previous line
print('                                                       _________________________________________________________________________________________')        #Welcome Screen
time.sleep(0.5)
print('                                                      |                                                                                         |')
time.sleep(0.5)
print('                                                      |              Welcome to SEEEDS, Basic Operating System!    Version 7.9.2.0.1            |')
time.sleep(1)
print('                                                      |                             Copyright (C) 2025  Ronald Petrik                           |')
time.sleep(1)
print('                                                      |                                                                                         |')
time.sleep(0.5)
print('                                                      |              Distributed under the GNU AFFERO GENERAL PUBLIC LICENSE                    |')
time.sleep(0.5)
print('                                                      |                          Originally Released: 12/31/2024                                |')
time.sleep(1)
print('                                                      |                           Last Major Update:03/29/2025                                  |')
time.sleep(1)
print('                                                      |                         Read User Manual (type \'help\')                                  |')
time.sleep(0.5)
print('                                                      |                                                                                         |')
time.sleep(0.5)
print('                                                      |                                                                                         | ')
print('                                                       _________________________________________________________________________________________')
time.sleep(1)
#print('                        |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|')#
#time.sleep(1)
#print('                                                                                   |///////////////////////////////////////////////////////////|')
#time.sleep(0.5)
#print('                                                                                   |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|')
#time.sleep(0.5)
#print('                                                                                   |///////////////////////////////////////////////////////////|')
#time.sleep(1)
#print('                                                                                   |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|')
#time.sleep(1)
#print('                                                                                   |___________________________________________________________|')
#time.sleep(1)
print('\n\n\n')
time.sleep(2)


while True:
    input_mode = input('MM>')  #change input mode
    if input_mode == 'A':     #if typed 'A'
        input_mode_a = input('A>')  #switched to input mode 'A'
        if input_mode_a == 'random_numb':     #if typed random_numb
            random_numb = random.randrange(0, 100)   #generate a random number
            random_numb_2 = random.randrange(0, 1000)  #generate a random number
            print(random_numb)   #print a random number between 1 and 100
        elif input_mode_a == 'random_numb_2':
            print(random_numb_2)
        elif input_mode_a == 'note':       
            type_1 = input('TYPE YOUR NOTE HERE--')
        elif input_mode_a == 'show_note':
            print('\n\n\n\n')
            print(type_1)               #print what was typed
            print('\n\n\n')
        elif input_mode_a == 'note_2':               #if you type in the "note_2" command;  
            type_2 = input('TYPE YOUR SECOND NOTE HERE--')    #type your note_2
        elif input_mode_a == 'show_note_2':          #if you type to show note 2, show the note you typed.
            print('\n\n\n\n')
            print(type_2)     #Print "Type 2"
            print('\n\n\n')  
        elif input_mode_a == 'calculator':
            # This adds two numbers
            def add(x, y):
                return x + y
            
            # This subtracts numbers
            def subtract(x, y):
                return x - y
            
            # This multiplies two numbers
            def multiply(x, y):
                return x * y
            
            # This divides two numbers
            def divide(x, y):
                return x / y
            
            
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            
            while True:
                # take input from the user
                choice = input("Enter choice(1/2/3/4): ")
            
                # check if choice is one of the four options
                if choice in ('1', '2', '3', '4'):
                    try:
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
            
                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))
            
                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))
            
                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))
            
                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    
                    # check if user wants another calculation
                    # break the while loop if answer is no
                    next_calculation = input("Let's do next calculation? (yes/no): ")
                    if next_calculation == "no":
                      break
                    else:
                        print("Invalid Input")
        else:  
            print('ERROR, COMMAND DOES NOT EXIST')     #Displayed if you put in an unknown command
    elif input_mode == 'B':
        input_mode_b = input('B>')
        if input_mode_b == input('?'):    #Little random thing
            print('something or nothing.')
        else:
            print('ERROR, MISTYPE?')         #Displayed if you type an unknown command
    elif input_mode == 'C':                            #if you type 'C' into MM
        input_mode_c = input('C>')                   #Display this
        if input_mode_c == 'moonlander':
            print('Welcome to M O O N L A N D E R!')
            time.sleep(1)
            print('M O O N L A N D E R! v0.0.1 BETA')
            print('You are an astronaut that has just finished training, and wants to get to space, prefferably the moon...')
            time.sleep(1)
            print('But NASA is not currently sending astronauts to space...')
            time.sleep(1)
            print('So you decide to build your own rocket. Once you finish, you secretly launch during the night, and no one notices')
            time.sleep(1)
            print('')
            break
        if input_mode_c == 'simplegame_snake':
            SNAKE()
        elif input_mode_c == 'simplegame_battleship':  #if you enter the command for battleship
            import random

            def createnewBoard():                                          #Start Battleship Game
                BombBoard = ['~','~','~','~','~','~','~','~','~']
                alreadytaken=''
                position=random.randint(0,8)
                bombs=1
                while bombs <=3:
                    while str(position) not in alreadytaken:
                        BombBoard[position]='X'
                        alreadytaken=alreadytaken + str(position)
                        bombs = bombs + 1
                    else:
                        position=random.randint(0,8)
                   
                return BombBoard
                
            def displayBoard(BombBoard):
                print('  1' + ' 2' + ' 3')
                print('A', end='')
                for i in range(3):
                    print(' ' + BombBoard[i], end= '')
                print()
            
                print('B', end='')
                for i in range(3):
                    print(' ' + BombBoard[i+3], end= '')
                print()
            
                print('C', end='')
                for i in range(3):
                    print(' ' + BombBoard[i+6], end= '')
                print()
            
            def checkHit(row,column, gameBoard):
                Hit=False
                if row== 'A' or row == 'a':
                    if gameBoard[int(column)-1] == 'X':
                        Hit=True
                        
                if row== 'B' or row == 'b':
                    if gameBoard[int(column)+2] == 'X':
                        Hit=True
                        
                if row== 'C' or row == 'c':
                    if gameBoard[int(column)+5] == 'X':
                        Hit=True
                
                return Hit
            
            def checkForIndex(row,column,gameboard):
                if row== 'A' or row == 'a':
                    if gameBoard[int(column)-1] == 'X':
                        index=int(column)-1
                        
                if row== 'B' or row == 'b':
                    if gameBoard[int(column)+2] == 'X':
                        index=int(column)+2
                        
                if row== 'C' or row == 'c':
                    if gameBoard[int(column)+5] == 'X':
                        index=int(column)+5
                
                return index
                
            #gamebegins   
            playAgain=True
            
            while playAgain==True:
                print('B A T T L E - S H I P II!\n' + '-------------____________-------------')
                print('There are 3 Ships in the Ocean, AKA the board in front of you.,\n' + 'you have 5 guesses to bomb them all! Good Luck, and Have Fun!')
                print()
                playerBoard = ['?','?','?','?','?','?','?','?','?']
                gusses=0
                hits=0
                gameBoard=createnewBoard()
                while gusses<=4:
                    displayBoard(playerBoard)
                    print()
                    print('Choose a row (A / B / C):')
                    row=input()
                    while row != 'a' and row != 'A' and row != 'b' and row != 'B' and row != 'c' and row != 'C':
                        print('You can only choose between A, B, or C!')
                        row=input()
                    
                    print('Choose a column (1/2/3):')
                    column=input()
                    while column != '1' and column != '2' and column != '3':
                        print('You can only choose between 1, 2, or 3!')
                        column=input()
                        
                    Hit=checkHit(row,column,gameBoard)
                    if Hit==True:
                        print('You hit a ship with a BOMB, nice job!')
                        hits = hits + 1
                        if hits==3:
                            print('You Did It, You Beat The Enemy! Would you like to play again? (y/n):')
                            playerinput=input()
                            if playerinput == 'y' or playerinput == 'Y':
                                playAgain=True
                            else:
                                playAgain=False
                                break
                        playerBoard[checkForIndex(row,column,gameBoard)] = 'X'
                        gusses = gusses + 1
                    else:
                        print('You Missed!')
                        gusses = gusses + 1
                else:
                    print('You ran out of guesses, and did not defeat the enemy!, would you like to play again? (y/n):')
                    playerinput=input()
                    if playerinput == 'y' or playerinput == 'Y':
                        playAgain=True
                    else:
                        break
        else:
            print('Error, No such command') #If you type in a nonexistent command into input C,  display this.
    elif input_mode == 'help':
        input_help = input('What Do You Need Help With? do you need a list of commands or the manual? Type one! (commmands/manual) CASE SENSITIVE!>>')
        if input_help == ('commands'):
            print('Commands: in input A (type and uppercase A into MM>): random_numb=random number 1 to 100, random_numb_2=random number 1 to 1000, note=type a note, note_2=type a second note, show_note=show first note, show_note_2=show second note, calculator=simple calculator in input B, simplegame_battleship=open battleship game, in input C, moonlander=Moonlander Game (In MM>) passpick=open Password Picker 25')
        elif input_help == ('manual'):
            with open('seeeds_manual.txt', 'r') as f:
                data = f.readlines()
                for d in data:
                    print('\n\n\n\n')
                    print(d)
    elif input_mode == 'passpick': #Starts the password picker 25 program!
        #!/usr/bin/python
        import random     #import random and string
        import string
        
        adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave', 'sweaty', 'sticky', 'slobbery', 'sad', 'dead', 'honest', 'gray']
        
        nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'person', 'laptop', 'fire', 'drawer', 'outlet', 'flamingo', 'turtle', 'bunny', 'rabbit', 'tea', 'coffee']  #lists of words for password picker which generates secure passwords.
        verbs = ['Running', 'sleeping', 'Breathing', 'Sniffing', 'screaming', 'burping', 'FARTING', 'LICKING', 'crazy', 'funny', 'growing', 'Dying', 'Jumping']
        print('Welcome to Password Picker 25! version 0.0.0.5 by Ronnie')
        print('\n')
        print('\n')
        print('The 3rd and newest Generation of Password Picker')
        print('last updated: 3/17/2025     last major update: 12/30/2024 Receiving Updates Weekly-ish')
        print('\n\n\n\n')
        while True:
            adjective = random.choice(adjectives)
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            number = random.randrange(0, 100)
            special_char = random.choice(string.punctuation)
            password = adjective + verb + noun + str(number) + special_char
            print('Your New Password is: %s' % password)       #Displays your new ##SECURE## password
            print('\n')          #print an empty line.
            
            response = input('Would you like another password? Type yes {<-or->} no: ')    #asks if you would like another password to be generated!
            print('\n')
            if response == 'no':
                print('Your Final password was:' + password)      #shows your final password that was generated before quitting the program.
                break  #breaks the loop
            
    else:
        print('No such input!, Try A, B, or C!, Or type help for commands and manual!')    #Tells you that the input/command you have put into the main menu does not exist
                
        
