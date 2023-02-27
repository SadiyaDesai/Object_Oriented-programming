"""
Polymorphism:
Poly: Many
Morph: forms

One Norm shows multiple forms then its a Polymorphism
It follows Duck typing Philosophy

Best example of a Polymorphism : Human nature
Example of a string
=====================================
a = '123'
b = '456'
print(a + b)
# perform concatenation
c = 3
print(a * c)
# peforms repetition

print(123 + 456)
#performs addition
============================

class Sample:
    def m1(self):
        print('Empty')
    def m1(self,a,b):
        print('with 2 vars.')
    def m1(self,x,y,z):
        print('With 3 args')

s = Sample()
s.m1(1,2,4)
------------------------
class Sample:
    def m1(self,*args):
        print(sum(args))

s = Sample()
s.m1()
s.m1(10,20)
s.m1(10.2,45.55)
s.m1(1,2,3,4,5,6)
========================================
Overloading:
def add(a,b):
    print(a+b)
def add(x,y,z):
    print(x+y+z)

add(10,20,9) #allowed bcz of last recent call
add(1,2) # not allowed bcz of last recent call in which 3 args values required

Types of Polymorphism:
1. Method level poly./ Method overloading:
A method with same name and different arguments

Example:

class Sample:
    def m1(self):
        print('Empty')
    def m1(self,a,b):
        print('with 2 vars.')
    def m1(self,x,y,z):
        print('With 3 args')
------------------------
In above, only last m1 with x,y,z will be available to use
bcz its recent one
======================================
Constructor Overloading: is also not possible in python

class Sample:
    def __init__(self):
        print('Empty')
    def __init__(self,a,b):
        print('with a , b')

#Sample() # this is not possible
Sample(1,2)
================================
Operator overloading:
It is the only possible type of overloading

a = '123'
b = '456'
print(a + b)
# perform concatenation
c = 3
print(a * c)
# peforms repetition

print(123 + 456)
#performs addition

In above case + operator shows different behaviour
=============================
a = '123'
b = '456'
c = 3
d = 4

print(a * 3)# repetition

print(d * 2.) # multiplication

+++++++++++++++++++++++++++++++
Q. What is Polymorphism
Q. What are different types in it?
Q. what is Method level poly./Method overloading?
Q. what is Constructor level poly./Constructor overloading?
Q. Is above 2 overloading are possible?
Q. What is Operator poly? Operator overloading?
==========================================
"""








