#types of inheritance
    #single inheritance
    #multi-level inheritance
    #heirarchical inheritance
    #multiple inheritance - not supported in java, but okay in python
#multi-level inheritance
class A:
    def f1(self):
        print("A")

class B(A): #Class B is a subclass of Class A
    def f2(self):
        print("B")

class C(B):
    def f3(self):
        print("C")

o=C()
o.f1()
o.f2()
o.f3()