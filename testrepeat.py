#This program takes a string, and tests if it contains a single repeating substring, eg. "AAbAAbAAb" returns true, and "AAbSdsaji" returns false

def findfactors(num):
    x=[]
    for i in range(1,num):
        if int(num/i) == num/i:
            x.append(i) 
    return(x)

def repeated(text): #The main function of the program
    istrue=False
    for stringpart in findfactors(len(text)): #Loops through each possible repeated substring
        testedrepeat=text[0:stringpart]
        timestorepeat=int(len(text)/len(testedrepeat))
        test=""
        for i in range(timestorepeat):
            test=test+testedrepeat
        if test==text:
            istrue=True
    return(istrue)


print(repeated(input("Write a string, and this program will return True if it contains a singular repeating substring")))
