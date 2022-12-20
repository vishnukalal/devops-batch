# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 2
b = 6.0
c = "vishnu"

print(a, b, c)

l = [1,2,3,4,8,4,6,3]
t = (12,3,8,205,12,8)
s = {1,3,5,7,3,5,9}
d = {1:1, 2:2, 2:4, 3:5, 3:7, 4:5, 4:7}

print(l)
print(t)
print(s)
print(d)


l = [1,2,5,8,9,12,15,85,42,65,98,8,5,12]

print(l)
print(l.index(85))
print(l[5])
print(l[8])
print(len(l))


a = [1,2,3,4,5,6,7,8,9,10]
a[1] = 5
print(a)
b = 6
c = a.index(b)
print(c)


t = (1,2,2,3,4,5)
print(t)

# assigning the tuple values
'''assigning the tuple values'''

d = {1:2, 'a':5, 'b':4}
print(d)
print(d.keys())
print(d.values())
print(d.items())

d[1] = 10
print(d)
d[0] = 4
print(d)
d[2] = 7
print(d)


# _________________________________________________________________
a = 8
b = 5

if a == b:
    print('both the numbers are same')
elif a > b:
    print('a is greater than b')
else:
    print('b is greater than a')
    
a = 3
b = 7
c = 7

if a>b and a>c:
    print('a is gratest')
elif b>a and b>c:
    print('b is greatest')
elif c>a and c>b:
    print('c s greatest')
elif a == b:
    print('a and b are equal')
elif a == c:
    print('a and c are equal')
elif b == c:
    print('b and c are equal')
else:
    print('all the numbers are equal')
    
# __________________________________________________________________________
l = [1,2,3,4,5,6]
for i in l:
    print(i)
    
n = len(l)
print(n)

for i in range(n):
    print(l[i])
    
a = 5
b = 2

while a>=b:
    print(a,b)
    b+=1
    
# ____________________________________________________________________
# functions are resuable piece of code which we can define and call whenever we need

def mul(a, b):
    print(a*b)
    
mul(4, 3)

print(5//2)


# + ---> addition
# - ---> sub
# * ---> multi
# / ---> division (float)
# // ---> dicision (integer)
# % ---> reminder from division


def abc(a, b):
    def subtract(a,b):
        return a-b
    return subtract(a,b)

a = 2
b = 1
print(abc(a, b))


class math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a//self.b
    def reminder(self):
        return self.a%self.b
        
mat = math(5, 2)
s = mat.multiply()
print(s)
t = mat.divide()
print(t)
u = mat.reminder()
print(u)

class ABC(math):
    print('inside abc')
    
abc = ABC(8,2)
print(abc.subtract())

class A:
    a = 10
    _b = 20
    __c = 30
    print(a+_b+__c)
    
d = A
print(d.a)
print(d._b)

import datetime

today = datetime.date.today()
print(today)

time = datetime.datetime.now()
print(time)