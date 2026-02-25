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