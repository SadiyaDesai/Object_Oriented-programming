"""
Abstraction means: Information hiding
# To do abstraction follow some rules:
- Create a normal class and inherit an ABC class in it
- ABC means ABSTRACT BASE CLASS
- This ABC is available in abc module
- second rule is: abstract class contains abstract or non abstract methods
- Ur normal class becomes a full abstract class only when it has at least one abstract method
- How to create an abstract method?
- use @abstractmethod decorator above non abstract method
- above decorator we can import from abc module

"""
from abc import ABC,abstractmethod

class Bank(ABC):

    @abstractmethod
    def trasaction(self): #abstract method
        pass


    def details(self): # non abstract method/ instance method
        print('This is RBI console')
        print('Secured one')


"""
Once we have an abstract class,
implementation of its method is must
means compulsory we need provide an implementation of abbstract method 
into a child class
wherever it may b inherited.
--------------------------------
We cant instantiate abstract class==> Hum abstract class ka object nahi ban sakte
b = Bank()
"""


