from ABC import abstractmethod
class SHAPE(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def circumference(self):
        pass
class CIRCLE(SHAPE):
    def __init__(self,r):
        self.radius=r
    def area(self):
        print(3.14*self.radius*self.radius)
    def circumference(self):
        print(2*3.14*self.radius)

class RECTANGLE(SHAPE):
    def __init__(self,w,h):
        self.width=w
        self.height=h
    def circumference(self):
        print(2*(self.width+self.height))
    def area(self):
        print(self.width*self.height)  

R=RECTANGLE(1,2)
#to finish