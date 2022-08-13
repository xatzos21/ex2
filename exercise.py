#Task1-ex2

#Your task is to check in action every basic math operators with combination of integers, floating point numbers, complex numbers and booleans. 
# Do at least two calculations for every operator. 
#Also make use of round function to round your floating point results to specific number of decimals.  
#You can mix integer with floats inside given math operation.  

import math


a = 12 + 34 # = 46
b = 43 - 56 # = -13
c = 4 * 4 # = 16
d = 4 / 5 # = 0.8
e = 12 % 5 # = 2
f = 2 ** 4 # = 16
g = 12.2 // 3 # = 4.0
h = True * False # = 0
i = 5 * (2 - 3j) # = (10-15j)

print('12 + 34 =', a)
print('43 - 56 =' ,b)
print('4 * 4 =' ,c)
print('4 / 5 =' , d)
print('12 % 5 =' ,e)
print('2 ** 4 =' ,f)
print('12.2 // 3 =' ,g)
print('True * False =' , round(h))
print('5 * (2 - 3j) =' , i)

#Task2-ex2

#Your task is to check in action every basic math function mentioned earlier
# with combination of integers, floating point numbers, complex numbers and booleans. 
# Do at least two calculations for every function. 

import math

a = max(2, 4, 24)
print('max(2, 4, 24) =' ,a)
b = max(3, 12, 342)
print('max(3, 12, 342) =' ,b)
c = min(3, 54, 65)
print('min(3, 54, 65) =' ,c)
d = min(65, 97, 123)
print('min(65, 97, 123) =' ,d)
e = abs(-21.21)
print('abs(-21.21) =' ,e)
f = abs(-654.32)
print('abs(-654.32) =' ,f)
g = pow(2, 2)
print('pow(2, 2) =' ,g)
h = pow(3, 3)
print('pow(3, 3) =' ,h)
i = max(True, False)
print('max(True, False) =' ,i)
j = abs(4 - 3j)
print('abs(4 - 3j) =' ,j)
from math import *
k = ceil(34/5)
print('ceil(34/5) =' ,k)
l = ceil(12/5)
print('ceil(12/5) =' ,l)
m = floor(34/5)
print('floor(34/5) =' ,m)
n = floor(23/3)
print('floor(23/3) =' ,n)