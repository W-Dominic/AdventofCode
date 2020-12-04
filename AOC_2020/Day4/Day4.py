import helper

def foo():
    f=open("/home/dom/Programming/AOC/AOC_2020/Day4/input.txt")
    f = f.read()
    L= []
    s= ""
    for i in f:
        if(i == "\n"):
            L.append(s)
            s = ""
        else:
            s += i

#ok now we do something
#see helper.py for helper function docstrings
    fieldscnt = 0
    fields = []
    fieldsval = []
    valid = 0
    """loops through each element in L until a blank line is found"""
    for i in L:
        if (i == ""):
            fieldsval = ignoreCid(fieldsval)
            bool = check7(fieldsval)
            if bool:
                valid +=1
                fieldsval=[]
            else:
                fieldsval=[]
        else:
            new = i.split(" ")
            for x in new:
                fieldsval.append(x)
    return valid



        
