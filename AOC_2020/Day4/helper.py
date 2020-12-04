""" This will be used to store helper functions"""
def isHex(s):
    try:
        int(s,16)
        return True
    except ValueError:
        return False

"""is... functions check if a critereia ... is valid"""
def isbyr(y):
    val=y[4:]
    if (len(val) == 4) and ((int(val)>=1920) and (int(val)<= 2002)):
        return True
    else:
        return False

def isiyr(y):
    val = y[4:]    
    if (len(val) == 4) and ((int(val)>=2010) and (int(val)<= 2020)):
        return True
    else:
        return False

def iseyr(y):
    val = y[4:]    
    if (len(val) == 4) and ((int(val)>=2020) and (int(val)<= 2030)):
        return True
    else:
        return False
                                                                                                                              
def ishgt(y):
    val = y[4:]    
    if (val[-2:] == "cm") and (int(val[:-2])>=150 and int(val[:-2])<=193):
        return True
    elif (val[-2:] == "in") and (int(val[:-2])>=59 and int(val[:-2])<=76):
        return True
    else:
        return False

def ishcl(y):
    val = y[4:]    
    if (val[0] == "#") and (len(val[1:]) == 6):
        if (isHex(val[1:])):
            return True
        else:
            return False

def isecl(y):
    val = y[4:]
    eye = ["amb","blu","brn","gry","grn","hzl","oth"]
    for a in eye:
        if(val == a):
            return True
    return False

def ispid(y):
    val = y[4:]
    if (len(val)==9) and (int(val) >= 0) and (int(val) < 1000000000):
        return True
    else: 
        return False

"""checks if all the requirements excluding cid are present and met"""
def check7(fieldsval):
    bool = True
    c = 0
    fieldcnt = 0
    while(bool == True) and (c < len(fieldsval)):
        y = fieldsval[c]
        if ((y.find("byr"))>=0):
            if not(isbyr(y)):
                bool = False
        
        elif ((y.find("iyr")) >=0): 
            if not(isiyr(y)):
                bool = False

        elif ((y.find("eyr")) >=0):
            if not(iseyr(y)):
                bool = False
        
        elif ((y.find("hgt")) >=0):
            if not(ishgt(y)):
                bool = False
        
        elif ((y.find("hcl")) >=0):
            if not(ishcl(y)):
                bool = False    
        
        elif ((y.find("ecl")) >=0):  
            if not(isecl(y)):                                                                                                                                           
                bool = False

        elif ((y.find("pid")) >=0):                                                                                                                                             
            if not(ispid(y)):                                                                                               
                bool = False
        else:
            bool = False
        c+=1
        fieldcnt +=1
    if bool and (fieldcnt == 7):
        return True
    else:
        return False

"""takes a fieldsval list and removes the cid category"""
def ignoreCid(fieldsval):
    for i in fieldsval:
        if "cid" in i:
            fieldsval.remove(i)
    return fieldsval
