from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("concrete method")
 
class son(father):
    def disp(self):
        pass
    def show(self):
        print("implementing abstract method")
        
class daughter(son):
    def disp(self):
        pass
    def show(self):
        print("the last class")
               
obj=daughter()
obj.show()

obj1=son()
obj1.show()