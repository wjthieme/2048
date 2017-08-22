import tkinter
import random


def printMatrix():
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
    print("")


def plaatsNummer():
    rand = random.randint(1,5)
    vier = False
    if (rand == 1):
        vier = True
    vakje = random.choice(vindNul())
    if vier:
        matrix[vakje[0]][vakje[1]] = 4
    else:
        matrix[vakje[0]][vakje[1]] = 2


def vindNul():
    nullen = []
    x = 0
    y = 0
    for list in matrix:
        for vakje in list:
            if vakje == 0:
                nullen.append([y,x])
            x += 1
        y += 1
        x = 0
    return nullen

def vindNietNul(omgekeerd = False):
    nietNullen = []
    x = 0
    y = 0
    for list in matrix:
        for vakje in list:
            if vakje != 0:
                nietNullen.append([y,x])
            x += 1
        y += 1
        x = 0
    if omgekeerd:
        nietNullen.reverse()
    return nietNullen


def loose():
    if (matrix.count(0) == 0):
        print("loser")


def up(index):
    if (index[0] == 0): return
    if (matrix[index[0]-1][index[1]] != 0):
        if (matrix[index[0]-1][index[1]] == matrix[index[0]][index[1]]):
            matrix[index[0]-1][index[1]] += matrix[index[0]-1][index[1]]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0]-1][index[1]] == 0):
        matrix[index[0]-1][index[1]] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        up([index[0]-1,index[1]])


def down(index):
    if (index[0] == len(matrix)-1): return
    if (matrix[index[0]+1][index[1]] != 0):
        if (matrix[index[0]+1][index[1]] == matrix[index[0]][index[1]]):
            matrix[index[0]+1][index[1]] += matrix[index[0]+1][index[1]]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0]+1][index[1]] == 0):
        matrix[index[0]+1][index[1]] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        down([index[0]+1,index[1]])


def left(index):
    if (index[1] == 0): return
    if (matrix[index[0]][index[1]-1] != 0):
        if (matrix[index[0]][index[1]-1] == matrix[index[0]][index[1]]):
            matrix[index[0]][index[1]-1] += matrix[index[0]][index[1]-1]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0]][index[1]-1] == 0):
        matrix[index[0]][index[1]-1] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        left([index[0],index[1]-1])


def right(index):
    if (index[1] == len(matrix)-1): return
    if (matrix[index[0]][index[1]+1] != 0):
        if (matrix[index[0]][index[1]+1] == matrix[index[0]][index[1]]):
            matrix[index[0]][index[1]+1] += matrix[index[0]][index[1]+1]
            matrix[index[0]][index[1]] = 0
            return
    if (matrix[index[0]][index[1]+1] == 0):
        matrix[index[0]][index[1]+1] = matrix[index[0]][index[1]]
        matrix[index[0]][index[1]] = 0
        right([index[0],index[1]+1])


def key(event):
    if (event.char == ''):
        for index in vindNietNul():
            up(index)
    elif (event.char == ''):
        for index in vindNietNul(True):
            down(index)
    elif (event.char == ''):
        for index in vindNietNul():
            left(index)
    elif (event.char == ''):
        for index in vindNietNul(True):
            right(index)
    else:
        return
    plaatsNummer()
    printMatrix()



matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
plaatsNummer()
plaatsNummer()
printMatrix()


screen = tkinter.Tk()
screen.wm_title("2048")

screen.bind("<Key>", key)

screen.attributes("-topmost", True)
screen.mainloop()
