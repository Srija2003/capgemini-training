class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14 * self.radius**2
    
class Square(shape):
    def __init__(self, side):
        self.side=side
    
    def area(self):
        return self.side **2
    
obj=Square(4)
obj1=circle(2)
print("the area of the square is",obj.area())
print("the area of the circle is",obj1.area())
