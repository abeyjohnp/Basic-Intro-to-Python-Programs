class A:
    def f(self):
        print("A")
class B(A):
    def f1(self):
        self.f()

d=B()
d.f1()  #calling f1, and within it calls f() of parent.
        #in python, no direct access WITHOUT self,  you have to use self to access functions of other classes.
        #either use self.f() or super().f()

#or

class A:
    def f(self):
        print("A")
class B:
    def f1(self):
        super().f()

d=B()
d.f1()

#but if variables are there

#methods and class variables can be accessed using super, but if it is instance variable only we can use self and access.

#when a parent class and child class has a constructor.

class A:
    def __init__(self):
        print("Parent class")

class B(A):
    def __init__(self):
        print("Child class")
    
obj=B()
#B constructor invoked, A construtor not invoked.

#or
class A:
    def __init__(self):
        print("Parent class")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child class")
    
obj=B()

#or
class A:
    def __init__(self):
        print("Parent class")

class B(A):
    pass #if pass is mentioned here, it will only print Parent Class message.
    
obj=B()