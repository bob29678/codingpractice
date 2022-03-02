#This program finds the perimeter of a given triangle
#This may be changed in the future to find other properties such as area, or perimeter of other polygons

import math

def perimeter(a,b,c):
    return(pointdistance(a,b)+pointdistance(a,c)+pointdistance(b,c))


def pointdistance(point1,point2): #Finds distance between two input points
    x=point1[0]-point2[0]
    y=point1[1]-point2[1]
    return math.sqrt(x**2+y**2)


print(perimeter([15, 7], [5, 22], [11, 1]))
