class A:
    def f1(self):
        print("A")

class B(A): #Class B is a subclass of Class A
    def f2(self):
        print("B")

class C(A):
    def f3(self):
        print("C")

o=B()
#using object of A you can access f1 and f2
o.f1()
o.f2()

o=C()
#using object of C you can access f1 and f3
o.f1()
o.f3()
