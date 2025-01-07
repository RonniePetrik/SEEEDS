#!/usr/bin/python

import time
def coin_collector():
    print("This is the game")
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
import random
import string
print('                                                                                    ____________________________________________________________')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |        Welcome to SEEEDS, Basic Operating System          |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |                 version 0.1.0.0.0                         |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |             Original Release:12/31/2024                   |')
time.sleep(1)
print('                                                                                   |            Last Major Update:12/31/2024                   |')
time.sleep(1)
print('                                                                                   |           Read User Manual (type \'help\')                  |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |       C input will not work until games are added         |')
time.sleep(1)
print('                                                                                   |              YOU MAY NOT COPY/EDIT THIS SOFTWARE          |')
time.sleep(1)
print('                                                                                   |               WITHOUT DIRECT PERMISSION                   |')
time.sleep(1)
print('                                                                                   |                        FROM ME!!                          |')
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
        elif input_mode_a == 'note_2':
            type_2 = input('TYPE NOTE 2 HERE--')
        elif input_mode_a == 'show_note_2':
            print('\n\n\n\n')
            print(type_2)
            print('\n\n\n')
        else:  
            print('SYNTAX ERROR, MISTYPE?')
    elif input_mode == 'B':
        input_mode_b = input('B>>>')
        if input_mode_b == input('??????'):
            print('something')
        else:
            print('SYNTAX ERROR, MISTYPE?')
    elif input_mode == 'C':
        input_mode_c = input('C>>>>')
        if input_mode_c == 'simplegame_coincollector':
            coin_collector()
        elif input_mode_c == 'simplegame_shootthefruit':
            pass
        else:
            print('Error, No such command')
    elif input_mode == 'help':
        input_help = input('What Do You Need Help With? Commands or Manual?>>')
        if input_help == ('commands'):
            print('Commands: in input A (type and uppercase A into MM>): random_numb=random number 1 to 100, random_numb_2=random number 1 to 1000, note=type a note, note_2=type a second note, show_note=show first note, show_note_2=show second note')
        elif input_help == ('manual'):
            with open('seeeds_manual.txt', 'r') as f:
                data = f.readlines()
                for d in data:
                    print('\n\n\n\n')
                    print(d)
    elif input_mode == 'passpick':
        #!/usr/bin/python
        import random
        import string
        
        adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave', 'sweaty', 'sticky', 'slobbery', 'sad', 'dead', 'honest', 'gray']
        
        nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'person', 'laptop', 'fire', 'drawer', 'outlet', 'flamingo', 'turtle', 'bunny', 'rabbit', 'tea', 'coffee']
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
            print('Your New Password is: %s' % password)
            print('\n')
            
            response = input('Would you like another password? Type yes {<-or->} no: ')
            print('\n')
            if response == 'no':
                print('Your Final password was' + password)
                break
            
    else:
        print('No such input!')
                
        
