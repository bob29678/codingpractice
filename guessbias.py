import random
bias = 3

def average(lst):
    return sum(lst) / len(lst)

def pickoptionflip(remainingflips,totals,bias):
    if totals[0]+totals[1]>9:
        return 2
    else:
        return 1

def pickoptionguess(remainingflips,totals,bias):
    if totals[1]>totals[0]:
        return 2
    else:
        return 1
    

def doround():
    global remainingflips
    global score
    
    opponentType=random.randint(1,2) # 1 = fair, 2 = unfair 
    totals=[0,0] #[heads,tails]

    #player flips coins until satisfied
    while remainingflips > 0:
        choice = pickoptionflip(remainingflips,totals,bias)
        if choice == 1:
            flip = flipcoin(opponentType)
            totals[flip]+=1
            remainingflips -= 1
            #print(str(flip)+"    "+str(totals[0])+" heads "+str(totals[1])+" tails, and "+str(remainingflips)+" flips left!")
            
            
        else:
            break
    if remainingflips == 0:
        return("lose")
    
    #player guesses if coin is biassed or not
    guess=pickoptionguess(remainingflips,totals,bias)
    if guess==opponentType:
        #print("correct!")
        remainingflips += 15
        score+=1
    else:
        #print("wrong!")
        remainingflips -= 30
    #print("remaining flips: " + str(remainingflips))

    
def flipcoin(fair): #function that flips coin or biassed coin depending on input
    if fair==1:
        return random.choice([0]+[1])
    else:
        return random.choice([0]+[1]*bias)

scorelist=[]

for i in range(1,10000):
    score=0
    remainingflips = 100
    while True:
        
        if doround() == "lose":
            break
        if remainingflips <= 0:
            break
    scorelist.append(score)

print(average(scorelist))

    
