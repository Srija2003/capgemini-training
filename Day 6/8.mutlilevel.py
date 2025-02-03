class Movie():
    def __init__(self,*name):
        self.name=name
    def mname(self):
        print("the movie ")
        
    def names(self):
        print("inside the movie")

class Hero(Movie):
    def man(self):
        print("this is hero")
        
class Heroine(Hero):
    def woman(self):
        print("this is  heroine")
        
        
obj=Heroine()
obj.woman()
obj.man()
obj.mname()
obj.names()