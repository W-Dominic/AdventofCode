import re

def input():
    f = open("/home/dom/Programming/AOC/AOC_2020/Day7/input.txt")
    f = f.read().splitlines()
    return f

def pt1():
    L = input()
    #splits into individual colors
    for i in range(len(L)):
        L[i]=L[i].replace("contain","").replace("bag", "").replace(" s ","").replace(" s.","").replace(" s,","").replace(",","").replace(" ", "").replace("noother","").replace(".","")
        L[i]= re.split('1|2|3|4|5|6|7|8|9|0',L[i])
    
    #utilizes the find method
    l= set(chain(L,["shinygold"]))
    return l
    #return len(l)

#recursively finds the parents of the elements given
def find(input,lst):
    if (len(lst) == 0):
        return []    
    ele = lst[0]
    found = []
    for i in input:
        for j in range(len(i)):
            if (i[j] == ele)and(not(j == 0)):
                found += [i[0]]
    return found + find(input,lst[1:])

#chains together find until no parent is found
def chain(input,lst):
    l = find(input,lst)
    if (len(l) == 0):
        return []
    else:
        return l + chain(input, l)
    
