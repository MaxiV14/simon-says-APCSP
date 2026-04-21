import random
# Function To Create A Circle
def rect(radius, color, x , y):
    rectangle = Rectangle(radius,radius)
    rectangle.set_position(x,y)
    rectangle.set_color(color)
    add(rectangle)
    rectList.append(rectangle)
    
# Function To Create A Text 
def txt(message, x , y):
    word = Text(message)
    word.set_position(x,y)
    add(word)
    wordList.append(word)
    
# Variables
W = get_width()
H = get_height()
rounds, guesses, i = 0, 0, 0
win = True
finish = False
delay = 1000
rightTime = 1000
rightCount = 2
# Dictionaries
colors = {"red": "#D92121","blue": "#305CDE", "yellow": "#FFDE21", "green": "#2e6930"}

#Lists
randomColors = ["red","blue","yellow","green"]
guessing = []
wordList = []
rectList = []
newPattern = []
# Code
# Title, Rounds And Right Message
txt(f"Simon Says", W/2-70, H/2 - 200)
txt(f"Round: {rounds}",145, H/2-150)

def removeRight():
    global rightCount
    remove(wordList[rightCount])
    rightCount += 1
    return rightCount
    
def appearRight():
    global rightTime
    txt(f"Right!", 170,H/2-100)
    timer.set_timeout(removeRight,rightTime)
    
# Rectangles To Click
rect(70,colors["red"], 35, H/2)
rect(70,colors["blue"],125,H/2)
rect(70,colors["yellow"],215,H/2)
rect(70,colors["green"],305,H/2)

# Create the Colors to Guess
def sequence():
    global guessing
# This is the loop for the function with parameters, iteration, selection and sequencing
    guessing = [random.choice(randomColors) for i in range(4)] 
    return(guessing)
newPattern = sequence()

# Show the pattern created by sequence
def rectangleColors():
    global i
    if newPattern[i] == "red":
        rect(70, colors["red"],170,340)
    elif newPattern[i] == "blue":
        rect(70, colors["blue"], 170,340)
    elif newPattern[i] == "yellow":
        rect(70, colors["yellow"], 170, 340)
    else:
        rect(70, colors["green"], 170, 340)
    i += 1
    return i
    
def rectangleWhite():
    rect(70, "white",170,340)

def finishTrue():
    global finish
    finish = True

def pattern():
    global finish, delay
    whiteInterval = delay + 400
    for i in range(4):
        timer.set_timeout(rectangleColors,delay)
        timer.set_timeout(rectangleWhite,whiteInterval)
        whiteInterval = delay + 400
        delay += 1500
    timer.set_timeout(finishTrue,delay)
    timer.set_timeout(rectangleWhite, delay)

pattern()
# Check For Game over or Correctness 
def check_guess(index,color):
    global guesses, rounds, wordList, delay, finish, i, newPattern, rightTime
    if guessing[index] != color:
        win = False
        remove_all()
        txt(f"GameOver!", W/2-75, H/2)
    else:
        if index == 3:
            rounds += 1 
            wordList[1].set_text(f"Round: {rounds}")
            newPattern = sequence()
            guesses = 0
            finish = False
            delay = 100
            i = 0
            pattern()
        else:
            appearRight()
            guesses += 1
            rightTime = 1000
    return guesses
    
# Click Handling 
def clickCheck(x,y):
    rectY = H/2+70 >= y >= H/2
    global guesses
    if guesses != 4 and win == True and finish == True: 
        #Red
        if (105 >= x >=35) and rectY:
            check_guess(guesses, "red")
        #Blue
        elif (195 >= x >= 125)  and rectY:
            check_guess(guesses,"blue")
        #Yellow
        elif (285 >= x >= 215) and rectY:
            check_guess(guesses, "yellow")
        #Green
        elif (375 >= x >= 305) and rectY:
            check_guess(guesses, "green")
        

add_mouse_click_handler(clickCheck)