# 2048 by Mara Dekkers & Willem Thieme (copyright (c) 2017)
# LSC213 Computer Science II - Final assignment (All code is written by Mara and Willem)

import tkinter as tk  # import the tkinter module as tk
import random as rand  # import the random module as rand


def startGame():  # start a new game
    global score, matrix  # make sure we selected the global variables for score and matrix
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # set the matrix to contain zeros
    score = 0  # set the score to 0
    plaatsNummer()  # place the first number in concordance with the 2048 game rules
    plaatsNummer()  # place the second number
    drawScreen()  # draw the screen


def openHelp():  # open the help screen and hide the main screen
    screen.withdraw()  # hide the main screen
    screen2.deiconify()  # show the help screen


def hideHelp():  # hide the help screen and open the main screen
    screen2.withdraw()  # hide the help screen
    screen.deiconify()  # show the main screen


def quitQuit():  # quit the application
    screen.destroy()  # destroy the main screen
    screen2.destroy()  # destroy the help screen


def plaatsNummer():  # place a number on the grid (either a 4 or a 2)
    if len(vindNul()) == 0: return  # check if there are still empty spaces on the board
    randnum = rand.randint(1, 10)  # get a random number from 1 to 10
    vier = False  # this variable will determine whether we will place a 4 or a 2.
    if (randnum == 1):  # one out of 10 times we will place a 4.
        vier = True  # set this variable to true so we know we are going to place a four
    vakje = rand.choice(vindNul())  # find a random empty square
    if vier:  # if we decided to place a four
        matrix[vakje[0]][vakje[1]] = 4  # place the four
    else:  # else
        matrix[vakje[0]][vakje[1]] = 2  # place a two


def drawScreen():  # redraw the screen
    canvas.delete("all")  # clear the cavas
    scoretext = "Score: " + str(score)  # create a string for the score
    canvas.create_text(240, 18, text=scoretext, font=('Helvetica', 24), fill='gray30')  # create a text for the score
    canvas.create_rectangle(35, 35, 445, 445, fill='ivory3', outline='ivory3')  # creat the background
    n = 0  # these three variable are to count which square we are currently evaluating
    x = 0
    y = 0
    while n < 16:
        outlinecolor = 'seashell4'  # set the outline color
        if matrix[y][x] == 0:  # all these Ifs will set the square color for the different values.
            squarecolor = 'ivory2'
        elif matrix[y][x] == 2:
            squarecolor = 'ivory'
        elif matrix[y][x] == 4:
            squarecolor = 'light yellow'
        elif matrix[y][x] == 8:
            squarecolor = 'sandy brown'
        elif matrix[y][x] == 16:
            squarecolor = 'coral'
        elif matrix[y][x] == 32:
            squarecolor = 'tomato'
        elif matrix[y][x] == 64:
            squarecolor = 'orange red'
        elif matrix[y][x] == 128:
            squarecolor = 'LightGoldenrod1'
        elif matrix[y][x] == 256:
            squarecolor = 'khaki'
        elif matrix[y][x] == 512:
            squarecolor = 'goldenrod1'
        elif matrix[y][x] == 1024:
            squarecolor = 'gold2'
        elif matrix[y][x] == 2048:
            squarecolor = 'orange2'
        elif matrix[y][x] == 4096:
            squarecolor = 'seagreen2'
        elif matrix[y][x] == 8192:
            squarecolor = 'seagreen3'
        elif matrix[y][x] == 16384:
            squarecolor = 'aquamarine2'
        elif matrix[y][x] == 32768:
            squarecolor = 'turquoise2'
        elif matrix[y][x] == 65536:
            squarecolor = 'turquoise3'
        elif matrix[y][x] == 131072:
            squarecolor = 'mediumpurple1'
        canvas.create_rectangle(x * 100 + 45, y * 100 + 45, x * 100 + 135, y * 100 + 135, fill=squarecolor,
                                outline=squarecolor)  # draw a square
        if matrix[y][x] != 0:  # set text color for the number in the squares.
            if matrix[y][x] < 5:
                textcolor = 'gray30'
            else:
                textcolor = 'white'
            canvas.create_text(x * 100 + 90, y * 100 + 90, text=matrix[y][x], fill=textcolor,
                               font=('Helvetica', 36))  # write the text in the square
        n += 1  # set our counter +1
        x += 1  # set the x-coord +1
        if x == 4:  # if we're at the end of the row of the matrix we move down one row
            x = 0
            y += 1
    if not (moveUpPossible()) and not (moveDownPossible()) and not (moveLeftPossible()) and not (
    moveRightPossible()):  # if there are no moves possible
        canvas.create_text(240, 190, text="Game", font=('Helvetica', 64), fill='gray30')  # set the game over text
        canvas.create_text(240, 290, text="Over", font=('Helvetica', 64), fill='gray30')  # ^^


def vindNul():  # find each square that doesn't have a block in it
    nullen = []  # intialize variable nullen
    x = 0  # set our coordinates to 0.
    y = 0
    for list in matrix:  # our matrix is actually a list of lists so in order to run through each single item we must have two for loops.
        for vakje in list:  # this for loop runs through each single square
            if vakje == 0:  # if the value of the square is 0.
                nullen.append([y, x])  # add the coordinates to the variable nullen
            x += 1  # up the coordinates
        y += 1  # up the y coordinate
        x = 0  # set x back to 0 to start on the first square of the next row
    return nullen  # return the variable nullen


def vindNietNul(
        omgekeerd=False):  # find all the squares that do have a block in it (look at the comments for the function above)
    nietNullen = []  # this function does pretty much the same as the previous one except that it returns all the squares that have a block in it
    x = 0
    y = 0
    for list in matrix:
        for vakje in list:
            if vakje != 0:
                nietNullen.append([y, x])
            x += 1
        y += 1
        x = 0
    if omgekeerd:  # if we want the list of coordinates to be reversed we do that here.
        nietNullen.reverse()  # reverse the list of coordinates
    return nietNullen


def addScore(number):  # add a number to score
    global score  # make sure we selected the global score
    score += number  # add number to score


def up(index):  # move a block upwards (nested function)
    if (index[0] == 0): return  # if the square is on the edge we can't move it upwards so we return.
    if (matrix[index[0] - 1][index[1]] != 0):  # check whether the square above is not a zero
        if (matrix[index[0] - 1][index[1]] == matrix[index[0]][
            index[1]]):  # if the square above is the same as the square we are looking at.
            addScore(matrix[index[0]][index[1]] * 2)  # we add a number to the score
            matrix[index[0] - 1][index[1]] += matrix[index[0] - 1][index[1]]  # we add the two squares together
            matrix[index[0]][index[1]] = 0  # and remove the initial square
            return  # exit the function because we have moved the square
    if (matrix[index[0] - 1][index[1]] == 0):  # check whether the square above is empty
        matrix[index[0] - 1][index[1]] = matrix[index[0]][index[1]]  # move the square one up
        matrix[index[0]][index[1]] = 0  # remove the initial square
        up([index[0] - 1, index[1]])  # check whether we can move the square up again.


def down(index):  # move a block downwards (nested function) (look at the comments for the function above)
    if (index[0] == len(matrix) - 1): return
    if (matrix[index[0] + 1][index[1]] != 0):
        if (matrix[index[0] + 1][index[1]] == matrix[index[0]][index[1]]):
            addScore(matrix[index[0]][index[1]] * 2)
            matrix[index[0] + 1][index[1]] += matrix[index[0] + 1][index[1]]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0] + 1][index[1]] == 0):
        matrix[index[0] + 1][index[1]] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        down([index[0] + 1, index[1]])


def left(index):  # move a block left (nested function) (look at the comments for the function above)
    if (index[1] == 0): return
    if (matrix[index[0]][index[1] - 1] != 0):
        if (matrix[index[0]][index[1] - 1] == matrix[index[0]][index[1]]):
            addScore(matrix[index[0]][index[1]] * 2)
            matrix[index[0]][index[1] - 1] += matrix[index[0]][index[1] - 1]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0]][index[1] - 1] == 0):
        matrix[index[0]][index[1] - 1] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        left([index[0], index[1] - 1])


def right(index):  # move a block right (nested function) (look at the comments for the function above)
    if (index[1] == len(matrix) - 1): return
    if (matrix[index[0]][index[1] + 1] != 0):
        if (matrix[index[0]][index[1] + 1] == matrix[index[0]][index[1]]):
            addScore(matrix[index[0]][index[1]] * 2)
            matrix[index[0]][index[1] + 1] += matrix[index[0]][index[1] + 1]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0]][index[1] + 1] == 0):
        matrix[index[0]][index[1] + 1] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        right([index[0], index[1] + 1])


def moveUpPossible():  # find out if it is possible to move a block upwards
    for index in vindNietNul():  # find all the squares and exectute the next piece for each square
        if (index[0] == 0): continue  # if the square is on the border: Continue
        if (matrix[index[0] - 1][index[1]] == 0 or matrix[index[0] - 1][index[1]] == matrix[index[0]][
            index[1]]):  # if the square above is empty or the same as the square we are currently evaluating
            return True  # that means we can still move upwards so we return true.
    return False  # else when there is no move possible we return false.


def moveDownPossible():  # find out if it is possible to move a block downwards (look at the comments for the function above)
    for index in vindNietNul(True):
        if (index[0] == len(matrix) - 1): continue
        if (matrix[index[0] + 1][index[1]] == 0 or matrix[index[0] + 1][index[1]] == matrix[index[0]][index[1]]):
            return True
    return False


def moveLeftPossible():  # find out if it is possible to move a block left (look at the comments for the function above)
    for index in vindNietNul():
        if (index[1] == 0): continue
        if (matrix[index[0]][index[1] - 1] == 0 or matrix[index[0]][index[1] - 1] == matrix[index[0]][index[1]]):
            return True
    return False


def moveRightPossible():  # find out if it is possible to move a block right (look at the comments for the function above)
    for index in vindNietNul(True):
        if (index[1] == len(matrix) - 1): continue
        if (matrix[index[0]][index[1] + 1] == 0 or matrix[index[0]][index[1] + 1] == matrix[index[0]][index[1]]):
            return True
    return False


def key(
        event):  # this function handles what happens when a key is pressed. (on windows the arrow keys don't work so you need to use the wasd.
    if (event.char == '' or event.char == 'w'):  # check whether the key that is pressed is a w or up arrow
        if not (moveUpPossible()): return  # if we can't move upwards we do nothing.
        for index in vindNietNul():  # for each square that is currently on the board:
            up(index)  # we move it up.
    elif (event.char == '' or event.char == 's'):  # check whether the key that is pressed is a s or down arrow
        if not (moveDownPossible()): return  # if we can't move downwards we do nothing.
        for index in vindNietNul(
                True):  # for each square that is currently on the board: (for moving down we reverse the list of coordinates because we want to evaluate the squares in a reversed order)
            down(index)  # we move it down.
    elif (event.char == '' or event.char == 'a'):  # check whether the key that is pressed is a a or left arrow
        if not (moveLeftPossible()): return  # if we can't move left we do nothing.
        for index in vindNietNul():  # for each square that is currently on the board:
            left(index)  # we move it left.
    elif (event.char == '' or event.char == 'd'):  # check whether the key that is pressed is a d or right arrow
        if not (moveRightPossible()): return  # if we can't move right we do nothing.
        for index in vindNietNul(
                True):  # for each square that is currently on the board: (for moving down we reverse the list of coordinates because we want to evaluate the squares in a reversed order)
            right(index)  # we move it right.
    else:  # if the button that is not an arrow key or wasd
        return  # then we do nothing.
    plaatsNummer()  # place a new number on the board
    drawScreen()  # redraw the screen on the gui


score = 0  # set the score to 0
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # set the matrix to contain zeros

screen = tk.Tk()  # create a screen for the game
screen.wm_title("2048")  # set the title of the screen
screen.bind("<Key>", key)  # set the keylistener for the frame
screen.geometry('%dx%d+%d+%d' % (500, 500, (screen.winfo_screenwidth() / 2) - 250,
                                 (screen.winfo_screenheight() / 2) - 300))  # set the position and size of the frame
screen.protocol('WM_DELETE_WINDOW', quitQuit)  # set what happens when the window is closed
screen.attributes("-topmost", True)  # set the window to be always on top

gameScherm = tk.Frame(screen, borderwidth=10)  # create a frame which we will add the widgets to
gameScherm.pack()  # pack the frame

canvas = tk.Canvas(gameScherm, width=500, height=450)  # add a canvas to draw the board
canvas.pack(anchor='center')  # pack the canvas

quitButton = tk.Button(gameScherm, text="Quit", bd=5, command=lambda: quitQuit())  # add a quit button
quitButton.pack(side='right')  # pack the quit button

restartButton = tk.Button(gameScherm, text="Restart", bd=5, command=lambda: startGame())  # add a restart button
restartButton.pack(side='left')  # pack the restart button

helpButton = tk.Button(gameScherm, text="Help", bd=5, command=lambda: openHelp())  # add a help button
helpButton.pack(anchor='center')  # pack the help button

screen2 = tk.Tk()  # create a second screen for the help window
screen2.wm_title("Help")  # set the title
screen2.attributes("-topmost", True)  # make sure the screen is always on top
screen2.geometry('%dx%d+%d+%d' % (
250, 105, (screen.winfo_screenwidth() / 2) - 125, (screen.winfo_screenheight() / 2) - 100))  # set the location and size
screen2.protocol('WM_DELETE_WINDOW', hideHelp)  # set what happens when you close the window
screen2.configure(background="ivory2")  # set the background color
screen2.withdraw()  # hide the help button because we start on the main window

helpScherm = tk.Frame(screen2, borderwidth=10)  # add a frame to the help screen
helpScherm.configure(background="ivory2")  # set the background color
helpScherm.pack()  # pack the frame

label = tk.Label(helpScherm, bd=5, font=('Helvetica', 14))  # add a label
label.configure(
    text="Hi! Welcome to 2048. \n Move the arrows or the \"wasd\" keys. \n Swipe the numbers and get to 2048!")  # set the helptext on the label
label.configure(background="ivory2", highlightcolor="ivory2", highlightbackground="ivory2")  # set the background color
label.pack()  # pack the label

quitHelpButton = tk.Button(helpScherm, text="Quit", bd=5, command=lambda: hideHelp())  # add a button to the help screen
quitHelpButton.configure(background="ivory2", highlightcolor="ivory2",
                         highlightbackground="ivory2")  # set the background color
quitHelpButton.pack(anchor="s")  # pack the button

startGame()  # call the function start game
screen.mainloop()  # call the method that starts the screen
screen2.mainloop()  # call the method that starts the helpscreen. Remember, we've hidden this screen so it won't show up yet.
