import itertools

numberlist = list(itertools.permutations([i+1 for i in range(6)]))

def checknumvalid(number):
    lastnum=-1
    numvalid=True
    for i in range(len(number)):
        if number[i] == i + 1:
            numvalid=False
        
        if number[i] == lastnum + 1 or number[i] == lastnum - 1:
            numvalid=False
        lastnum = number[i]
    return numvalid

for number in numberlist:
    if checknumvalid(number):
        print(number)
