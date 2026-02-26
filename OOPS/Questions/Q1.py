class Shape:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
class Rectangle(Shape):
    def area(self):
        return (2*(self.width+self.height))
    
class Triangle(Shape):
    def area(self):
        return (1/2*(self.width*self.height))
    
r=Rectangle(1,3) #this will invoke the constructor of Shape (the parent class)
print("Area of the rectangle : ",r.area())
t=Triangle(3,4)
print("Area of the Triangle : ",t.area())   
