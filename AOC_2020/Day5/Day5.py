import math

def pt1():
    """gets input and puts it into array passes"""
    f= open("/home/dom/Programming/AOC/AOC_2020/Day5/input.txt")
    f= f.read()
    passes = []
    s=""
    for i in f:
        if(i=="\n"):
            passes.append(s)
            s=""
        else:
            s+= i
    #ok now we do something
    seatIDs = []
    for i in passes:
        r = row(i[0:7])
        c = column(i[7:])
        seatID = r*8 + c
        seatIDs.append(seatID)
    """
    pt1: return max(seatIDs)
    """
    return pt2(seatIDs)

def row(board):
    ran=[0,127]
    c = 0
    for i in board:
        if(c == len(board)-1):
            if (i == "F"):
                return ran[0]
            else:
                return ran[1]
        elif (i == "F"):
            ran[1] = ran[1]-math.floor((ran[1]-ran[0])/2)-1
        elif (i == "B"):
            ran[0] = ran[0] + math.floor((ran[1]-ran[0])/2)+1
        c += 1
def column(board):
    ran = [0,7]
    c = 0
    for i in board:
        if (c == len(board)-1):
            if (i == "R"):
                return ran[1]
            else:
                return ran[0]
        elif (i=="R"):
            ran[0] = ran[0] + math.floor((ran[1]-ran[0])/2)+1
        elif (i=="L"):
            ran[1] = ran[1]-math.floor((ran[1]-ran[0])/2)-1
        c += 1

def pt2(seatIDs):
    seatIDs.sort()
    c = 0
    while (c < (len(seatIDs)-3)):
        i = seatIDs[c]
        j = seatIDs[c+1]
        if not((i+1) == j):
            return (i+1)
        c +=1



