#!/usr/bin/python

#Import time
import time
def coin_collector():
    print("This is the game")
#Start printing the boot up screen.
print('                                                                                                                         ')
time.sleep(1)
print('                                                                                                        BO                     ')
time.sleep(1)
print('                                                                                                        OT                ')
time.sleep(1)
print('                                                                                                        IN               ')
time.sleep(1)
print('                                                                                                        G               ')
time.sleep(1)
print('                                                                                                        UP!                         ')
time.sleep(1)
print('                                                                                                                         ')
time.sleep(1)

time.sleep(1)
#import random and string (used later)
import random
import string
print('                                                                                    ____________________________________________________________')        #Boot screen thingie
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |        Welcome to SEEEDS, Basic Operating System          |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |                 version 0.2.0.0.7                         |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |             Original Release:12/31/2024                   |')
time.sleep(1)
print('                                                                                   |            Last Major Update:2/18/2025                    |')
time.sleep(1)
print('                                                                                   |           Read User Manual (type \'help\')                  |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |       C input will not work until games are added         |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |___________________________________________________________|')
time.sleep(1)
print('\n\n\n')
time.sleep(4)


while True:
    input_mode = input('MM>')  #change input mode
    if input_mode == 'A':     #if typed 'A'
        input_mode_a = input('A>>')  #switched to input mode 'A'
        if input_mode_a == 'random_numb':     #if typed random_numb
            random_numb = random.randrange(0, 100)   #generate a random number
            random_numb_2 = random.randrange(0, 1000)  #generate a random number
            print(random_numb)   #print a random number between 1 and 100
        elif input_mode_a == 'random_numb_2':
            print(random_numb_2)
        elif input_mode_a == 'note':       #unfinished
            type_1 = input('TYPE NOTE HERE--')
        elif input_mode_a == 'show_note':
            print('\n\n\n\n')
            print(type_1)               #print what was typed
            print('\n\n\n')
        elif input_mode_a == 'note_2':               #if you type in the "note_2" command;  
            type_2 = input('TYPE NOTE 2 HERE--')    #type your note
        elif input_mode_a == 'show_note_2':          #if you type to show note 2, show the note you typed.
            print('\n\n\n\n')
            print(type_2)     #Print "Type 2"
            print('\n\n\n')
        else:  
            print('SYNTAX ERROR, MISTYPE?')     #Displayed if you put in an unknown command
    elif input_mode == 'B':
        input_mode_b = input('B>>>')
        if input_mode_b == input('??????'):    #Little Easter Egg
            print('something')
        else:
            print('SYNTAX ERROR, MISTYPE?')         #Displayed if you type an unknown command
    elif input_mode == 'C':                            #if you type 'C' into MM
        input_mode_c = input('C>>>>')                   #Display this
        if input_mode_c == 'simplegame_coincollector':
            coin_collector()
        elif input_mode_c == 'simplegame_shootthefruit':  #if you enter the command for shoot the fruit then pass (game has not been added yet)
            pass
        else:
            print('Error, No such command') #If you type in a nonexistent input mode, display this.
    elif input_mode == 'help':
        input_help = input('What Do You Need Help With? commands or manual?>>')
        if input_help == ('commands'):
            print('Commands: in input A (type and uppercase A into MM>): random_numb=random number 1 to 100, random_numb_2=random number 1 to 1000, note=type a note, note_2=type a second note, show_note=show first note, show_note_2=show second note, (In MM>) passpick=open Password Picker 25')
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
        
        nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'person', 'laptop', 'fire', 'drawer', 'outlet', 'flamingo', 'turtle', 'bunny', 'rabbit', 'tea', 'coffee']  #lists of words for password picker witch generates secure passwords.
        verbs = ['Running', 'sleeping', 'Breathing', 'Sniffing', 'screaming', 'burping', 'FARTING', 'LICKING', 'crazy', 'funny', 'growing', 'Dying']
        print('Welcome to Password Picker 25!, version 0.0.0.1, by Ronnie Petrik')
        print('')
        print('')
        print('\n')
        print('The 3rd version of Password Picker')
        print('last upadated: 0/0/0     last major update: 12/30/2024')
        print('\n\n\n\n\n')
        while True:
            adjective = random.choice(adjectives)
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            number = random.randrange(0, 100)
            special_char = random.choice(string.punctuation)
            password = adjective + verb + noun + str(number) + special_char
            print('Your New Password is: %s' % password)       #Displays your new password
            print('\n')          #print an empty line.
            
            response = input('Would you like another password? Type yes {<-or->} no: ')    #asks if you would like another password to be generated
            print('\n')
            if response == 'no':
                print('Your Final password was:' + password)      #shows your final password that was generated before quitting the program.
                break  #breaks the loop
            
    else:
        print('No such input!')    #Tells you that the input you have put into the main menu does not exist
                
        
