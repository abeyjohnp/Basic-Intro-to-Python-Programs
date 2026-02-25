class A:
    def f1(self):
        print("A")

class B: 
    def f2(self):
        print("B")

class C(A,B): #C is a subclass of both A and B
    def f3(self):
        print("C")

o=C()
o.f1()
o.f2()
o.f3()
