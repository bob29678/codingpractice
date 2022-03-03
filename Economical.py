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
    return simplifylist(factorlist)

def simplifylist(x): #Simplifies a list of numbers, eg. 4*4*4*4 -> 4^4
    simplifiedlist=[]
    for i in x:
        simplifiedlist.append([i,x.count(i)])
        x.remove(i)
    return simplifiedlist


def isEconomical(x):
    primefactors=findprimefactors(x)
    total=0
    for i in primefactors:
        total+=len(str(i[0]))
        if i[1]!= 1:
            total+=len(str(i[1]))
    if total == len(str(x)):
        return("Perfectly economical")
    elif total < len(str(x)):
        return("More than economical")
    else:
        return("Expensive!")

print(isEconomical(54))
