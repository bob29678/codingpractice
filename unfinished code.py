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

def simplifylist(x): #Simplifies a list of numbers, eg. 4*4*4*4 -> 4^4
    simplifiedlist=[]
    for i in x:
        simplifiedlist.append([i,x.count(i)])
        x.remove(i)
    return simplifiedlist


def isEconomical(x):
    return(x)

print(simplifylist(findprimefactors(54)))

