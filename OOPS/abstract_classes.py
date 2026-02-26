"""
a class that can contain abstract method, no definition, only function header.
if a class consist of abstract method, it is called abstract class.
it can have concrete methods.
to write an abstract class in python, import ABC class from ABC module.
from abc import ABC.abstractmethod
    #whenever u write a class subclass of ABC, that class becomes abstract class.
    abstract method - in java it is abstract void fn()
    here - @abstractmethod
        #inside function, since no definition, give pass
    abstract class definition implemeneted by child class
    
"""

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def function(self):
        pass #no executable statement here!

class B(A):
    def function(self):
        print("In B")

#o=A() #you cannot create an object of Abstract class!
o=B()
o.function()