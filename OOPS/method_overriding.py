#creating one function in parent class and providing the same function in the child class.
class A:
    def f1(self):
        print("Hello, from A")
class B(A):
    def f1(self):
        print("Hello, from B")

o=B()
o.f1()

