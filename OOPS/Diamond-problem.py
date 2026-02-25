#method overriding
class A:
    def fun(self):
        print("In class A")

class B:
    def fun(self):
        print("In class B")

class C(A):
    def fun(self):
        print("In class C")

class D(B,C):
    pass

a=D()
a.fun() #it checks if it is in D, if not go to immediate parent
        #if in B okay, if not go to C, (Left to right in each level)