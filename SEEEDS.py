#!/usr/bin/python

#Import time
import time
def SNAKE():
    import turtle
    import random
     
    w = 500
    h = 500
    food_size = 10
    delay = 100
     
    offsets = {
        "up": (0, 20),
        "down": (0, -20),
        "left": (-20, 0),
        "right": (20, 0)
    }
     
    def reset():
        global snake, snake_dir, food_position, pen
        snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        snake_dir = "up"
        food_position = get_random_food_position()
        food.goto(food_position)
        move_snake()
         
    def move_snake():
        global snake_dir
     
        new_head = snake[-1].copy()
        new_head[0] = snake[-1][0] + offsets[snake_dir][0]
        new_head[1] = snake[-1][1] + offsets[snake_dir][1]
     
         
        if new_head in snake[:-1]:
            reset()
        else:
            snake.append(new_head)
     
         
            if not food_collision():
                snake.pop(0)
     
     
            if snake[-1][0] > w / 2:
                snake[-1][0] -= w
            elif snake[-1][0] < - w / 2:
                snake[-1][0] += w
            elif snake[-1][1] > h / 2:
                snake[-1][1] -= h
            elif snake[-1][1] < -h / 2:
                snake[-1][1] += h
     
     
            pen.clearstamps()
     
             
            for segment in snake:
                pen.goto(segment[0], segment[1])
                pen.stamp()
     
             
            screen.update()
     
            turtle.ontimer(move_snake, delay)
     
    def food_collision():
        global food_position
        if get_distance(snake[-1], food_position) < 20:
            food_position = get_random_food_position()
            food.goto(food_position)
            return True
        return False
     
    def get_random_food_position():
        x = random.randint(- w / 2 + food_size, w / 2 - food_size)
        y = random.randint(- h / 2 + food_size, h / 2 - food_size)
        return (x, y)
     
    def get_distance(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance
    def go_up():
        global snake_dir
        if snake_dir != "down":
            snake_dir = "up"
     
    def go_right():
        global snake_dir
        if snake_dir != "left":
            snake_dir = "right"
     
    def go_down():
        global snake_dir
        if snake_dir!= "up":
            snake_dir = "down"
     
    def go_left():
        global snake_dir
        if snake_dir != "right":
            snake_dir = "left"
     
     
    screen = turtle.Screen()
    screen.setup(w, h)
    screen.title("Snake")
    screen.bgcolor("blue")
    screen.setup(500, 500)
    screen.tracer(0)
     
     
    pen = turtle.Turtle("square")
    pen.penup()
     
     
    food = turtle.Turtle()
    food.shape("square")
    food.color("yellow")
    food.shapesize(food_size / 20)
    food.penup()
     
     
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
     
     
    reset()
    turtle.done()

Output:
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
print('                                                                                   |                 version 5.1.6.3.9                         |')
time.sleep(1)
print('                                                                                   |                                                           |')
time.sleep(1)
print('                                                                                   |             Original Release:12/31/2024                   |')
time.sleep(1)
print('                                                                                   |            Last Major Update:2/23/2025                    |')
time.sleep(1)
print('                                                                                   |           Read User Manual (type \'help\')                  |')
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
        if input_mode_b == input('?'):    #Little random thing
            print('something')
        else:
            print('SYNTAX ERROR, MISTYPE?')         #Displayed if you type an unknown command
    elif input_mode == 'C':                            #if you type 'C' into MM
        input_mode_c = input('C>>>>')                   #Display this
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
                print('B A T T L E - S H I P S\n' + '=======================')
                print('There are 3 Ships in the Ocean,\n' + 'you have 5 guesses to bomb them all! Good Luck!')
                print()
                playerBoard = ['?','?','?','?','?','?','?','?','?']
                gusses=0
                hits=0
                gameBoard=createnewBoard()
                while gusses<=4:
                    displayBoard(playerBoard)
                    print()
                    print('Choose a row (A/B/C):')
                    row=input()
                    while row != 'a' and row != 'A' and row != 'b' and row != 'B' and row != 'c' and row != 'C':
                        print('You can only choose between A/B/C!')
                        row=input()
                    
                    print('Choose a column (1/2/3):')
                    column=input()
                    while column != '1' and column != '2' and column != '3':
                        print('You can only choose between 1/2/3!')
                        column=input()
                        
                    Hit=checkHit(row,column,gameBoard)
                    if Hit==True:
                        print('You Bombed a ship!')
                        hits = hits + 1
                        if hits==3:
                            print('You Did It!, would you like to play again? (y/n):')
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
                    print('You ran out of guesses!, would you like to play again? (y/n):')
                    playerinput=input()
                    if playerinput == 'y' or playerinput == 'Y':
                        playAgain=True
                    else:
                        break
        else:
            print('Error, No such command') #If you type in a nonexistent input mode, display this.
    elif input_mode == 'help':
        input_help = input('What Do You Need Help With? commands or manual? Type one!>>')
        if input_help == ('commands'):
            print('Commands: in input A (type and uppercase A into MM>): random_numb=random number 1 to 100, random_numb_2=random number 1 to 1000, note=type a note, note_2=type a second note, show_note=show first note, show_note_2=show second note, in input B, simplegame_battleship=open battleship game (In MM>) passpick=open Password Picker 25')
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
        print('The 3rd Generation of Password Picker')
        print('last upadated: 2/23/2025     last major update: 12/30/2024')
        print('\n\n\n\n')
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
        print('No such input!, Try A, B, or C!')    #Tells you that the input you have put into the main menu does not exist
                
        
