#A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions is equal to the number itself. Some of the other examples of Disarium number are 89, 135, 518
#This program tests if an input number is a disarium number

def isdisarium(x):
    numsum=0
    
    for i in range(len(str(x))):
        numsum+=int(str(x)[i])**(i+1)
        
    if x == numsum:
        return True
    return("False, sum was actually "+str(sum_))


print(isdisarium(int(input())))
