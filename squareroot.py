import math     #math is a module without building we willuse already defined one
n=int(input())
print(math.sqrt(n))    #this will return the sqrt with the help of math function
#another technic
from math import sqrt
num=int(input())
print(sqrt(num))
#floor means it will return the nearest integer value which is less than or equal to the given number
#ceil means it will return the nearest integer value which is greater than or equal to the given number
print(math.floor(5.9))  #it will return 5
print(math.ceil(5.1))   #it will return 6
#pow means it will return the power of the given number
print(math.pow(5,3))  #it will return 125
print(math.ceil(-10.7))
print(math.fabs(-8.8))