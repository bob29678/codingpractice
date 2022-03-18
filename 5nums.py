from itertools import permutations

numlist=[1,2,3,4,5]
alllists=list(permutations(numlist))

workinglists=[]

for trylist in alllists:
    lastnum=-1
    listgood=True
    
    for i in range(len(numlist)):
        
        if numlist[i]==trylist[i]:
            listgood=False
        
        elif lastnum==trylist[i]+1 or lastnum==trylist[i]-1:
            listgood=False
            
        lastnum=trylist[i]
        
        if listgood:
            workinglists.append(trylist)
            
print(workinglists)
