import copy
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
        pass
    #str for testing
    def string(self):
        return "acc " + str(self.x)

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
         pass
     #str for testing
     def string(self):
         return "jmp " + str(self.lines)

    

#does nothing
class nop:
    def __init__(self,x,pos,runs):
        self.pos = pos
        self.runs = runs
        self.x = x
    #accessors
    def getX(self):
        return self.x
    def getPos(self):
        return self.pos
    def getRuns(self):
        return self.runs
    #settersi
    def incRuns(self):
        self.runs += 1
        pass
    def string(self):
        return "nop " + str(self.x)


def input():
    f = open("/home/dom/Programming/AOC/AOC_2020/Day8/input.txt")
    f = f.read().splitlines()

    instructions = []
    #loop to make a list of the instructions, where each instruction is an object
    for i in f:
        opp = i[0:3]
        if (opp == "nop"):
             #first, gets the value of the change
            sign = i[4]
            if (sign == "+"):
                x = int(i[5:])
            else:
                x = int(i[4:])

            instructions.append(nop(x,len(instructions),0))
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

#finds the broken jmp
def finishes(input):
    inst = copy.deepcopy(input)
    accumulator = 0
    
    i = 0
    while (i < len(inst)): 
        opp = inst[i]
        opp.incRuns()
                        
        if(isinstance(opp,acc)):
            if (opp.getRuns() > 1):
                return False
            else:
                newAcc = opp.setAcc(accumulator)
                accumulator = newAcc
                i+=1
        
        elif(isinstance(opp,jmp)):
            if (opp.getRuns() > 1):
                return False
            else:
                change = opp.getLines()
                i=opp.setPos()
        
        elif(isinstance(opp,nop)):
            if (opp.getRuns() > 1):
                return False
            else:
                i+=1
    return True

def accum(input):
    inst = copy.deepcopy(input)
    accumulator = 0
    
    i = 0
    while (i < len(inst)): 
        opp = inst[i]
        opp.incRuns()
                        
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
    return accumulator

def pt2():
    inst = copy.deepcopy(input())
    print(inst)
    for i in range(len(inst)):
        opp = inst[i]
        if (isinstance(opp,jmp)):
            lines = opp.getLines()
            
            new = copy.deepcopy(inst)
            new[i] = nop(lines,i,0)
            
            #testing
            print(new)
            for j in new:
                print(j.string())
            print(accum(new))
            print("")
            #testing

            if (finishes(new)):
                return accum(new)
            else:
                new[i] = jmp(lines,i,0)
        elif(isinstance(opp,nop)):
            x = opp.getX()

            new = copy.deepcopy(inst)
            new[i] = jmp(x,i,0)
            
            #testing
            print(new)
            for j in new:
                print(j.string())
            print(accum(new))
            print("")
            #testing

            if (finishes(new)):
                return accum(new)
            else:
                new[i] = nop(x,i,0)
    return "failure"


