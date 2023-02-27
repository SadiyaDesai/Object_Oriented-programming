"""
Encapsulation in python:
Wrapping of variables and methods together in a single container
which is class

In simple words, its a Data hiding
==========================================

class Sample:
    x = 10

    def m1(self):
        print('m1')

print(x) # x and m1 is hidden from outside world
m1()
==========================
public string place = 'pune'

private int pin = 4545

In other programming languages they have access modifiers to
implement Encapsulation
Example
public [available to all]
private [available only inside a class]
protected [ available to the class and to its child class]
---------------------------------------
In python we don't have access modifiers
But we can implement above properties using
_ underscore convention

public means : a variable or a method without _
protected means: a variable or method with _
private means : a var. or a method with __ double underscore
------------------------------------------------------------
class Bank:
    #public var. place
    place = 'Pune'

    #protected var. IFSC
    _ifsc = 'SBI223344'

    # private var. password
    __password = '1234'

b =  Bank()
print(b.place)
print(b._ifsc)
#print(b.__password)
print(dir(b))
# private member will be available only inside a class
# or within a class we can access private member
# BUT if we want to access a private member using a an object
# use Name Mangling technique: we use a class in protected mode with
# desired __variable
print(b._Bank__password)
==================================

class Sample:
    def m1(self):
        print('Public method')

    def _m2(self):
        print('Protected method')

    def __m3(self):
        print('Private method')

s = Sample()
s.m1()
s._m2()
#s.__m3()
print(dir(s))
s._Sample__m3()
============================================
Method overriding:
When we have a parent child relationship
means simply we have inheritance
and
Parent class + child class contains a method with same name
Then
A method of a child overrides a method in Parent
-----------------------------------
class Father:
    def money(self):
        print('Money from Father')


class Child(Father):
    def money(self):
        print('My own salary')

c = Child()
c.money()
-------------------------------
"""





















