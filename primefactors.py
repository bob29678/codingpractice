import math

def findprimefactors(x):
    factorlist=[]
    limit=math.ceil(math.sqrt(x))
    while x != 1:
        y=2
        while True:
            if x % y == 0:
                x=x/y
                factorlist.append(y)
                break
            else:
                y+=1
    return factorlist

print(findprimefactors(99999999999991))
