#finds all prime numbers within a number

from itertools import combinations 


def allsubstrings(string):
    string=str(string)
    sstrings=[string[x:y] for x, y in combinations(
        range(len(string) + 1), r = 2)]
    return sstrings

def extractprimes(x):
    primelist=set()
    for i in allsubstrings(x):
        if testprime(int(i)):
            primelist.add(int(i))
    return primelist

def testprime(x):
    y=2
    while y*y < x:
        if x%y==0:
            return False
        y+=1
    return True

print(extractprimes(1717))
