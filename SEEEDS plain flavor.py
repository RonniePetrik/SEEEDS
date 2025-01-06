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
print('                                                                                SEEEDS COPYRIGHT        IN               ')
time.sleep(1)
print('                                                                                     2025               G               ')
time.sleep(1)
print('                                                                                  TOUCHPORT             UP!                         ')
time.sleep(1)
print('                                                                                  COMPUTERS                                       ')
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
print('                                                                                   |                 version 0.0.0.6.9                         |')
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
            
    else:
        print('No such input!')
                
        
