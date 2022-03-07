vowels=["a","e","i","o","u"]

def consecvowels(word):
    streak=0
    beststreak=0
    lastletter=""
    for letter in word:
        if letter in vowels and lastletter in vowels:
            streak+=1
            if streak > beststreak:
                beststreak=streak
        else:
            streak=0
        lastletter=letter
    beststreak+=1
    return beststreak
    
wordlist=[]

vowelcount=0

for word in wordlist:
    for letter in word:
        if letter in vowels:
            vowelcount+=1
