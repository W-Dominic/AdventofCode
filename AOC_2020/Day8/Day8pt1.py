#changes the value of the accumulator
class acc:
    def __init__(self,x,pos,runs):
        self.x = x
        self.pos = pos
        self.runs = runs
    #accessors
    def getX(self):
        return self.x
    def getPos(self):
        return self.pos
    def getRuns(self):
        return self.runs
    #setters
    def setAcc(self,acc):
        acc += self.x
        return acc
    def incRuns(self):
        self.runs += 1

#jumps x lines given
class jmp:
     def __init__(self,x,pos,runs):
         self.lines = x
         self.pos = pos
         self.runs = runs
     #accessors
     def getLines(self):
         return self.lines
     def getPos(self):
         return self.pos
     def getRuns(self):
         return self.runs
     #setters
     def setPos(self):
         self.pos += self.lines
         return self.pos
     def incRuns(self):
         self.runs += 1

#does nothing
class nop:
    def __init__(self,pos,runs):
        self.pos = pos
        self.runs = runs
    #accessors
    def getPos(self):
        return self.pos
    def getRuns(self):
        return self.runs
    #settersi
    def incRuns(self):
        self.runs += 1


def input():
    f = open("/home/dom/Programming/AOC/AOC_2020/Day8/input.txt")
    f = f.read().splitlines()

    instructions = []
    #loop to make a list of the instructions, where each instruction is an object
    for i in f:
        opp = i[0:3]
        if (opp == "nop"):
            instructions.append(nop(len(instructions),0))
        elif (opp == "acc"):
            #first, gets the value of the change
            sign = i[4]
            if (sign == "+"):
                x = int(i[5:])
            else:
                x = int(i[4:])
            #now create an instance
            instructions.append(acc(x,len(instructions),0))
        elif (opp == "jmp"):
            #first, gets the value of the change
            sign = i[4]
            if (sign == "+"):
                x = int(i[5:])
            else:
                x = int(i[4:])
            #now create an instance
            instructions.append(jmp(x,len(instructions),0))
    return instructions

def pt1():
    inst = input()
    accumulator = 0
    
    i = 0
    while (i < len(inst)): 
        opp = inst[i]
        opp.incRuns()
        print("index",i," runs:",opp.getRuns())
                        
        if(isinstance(opp,acc)):
            if (opp.getRuns() > 1):
                return accumulator
            else:
                newAcc = opp.setAcc(accumulator)
                accumulator = newAcc
                i+=1
        
        elif(isinstance(opp,jmp)):
            if (opp.getRuns() > 1):
                return accumulator
            else:
                change = opp.getLines()
                i=opp.setPos()
        
        elif(isinstance(opp,nop)):
            if (opp.getRuns() > 1):
                return accumulator
            else:
                i+=1







