class Bird:
    def fly(self):
        return "This bird can fly"
    
class Mammal:
    def walk(self):
        
        return "This mammal can walk"
    
class Animal():
    def run(self):
        return "this can run"
    
class Bat(Bird,Mammal,Animal):
    def dance(Self):
        return "natuuu"
    
    pass  #used if there are no statemnets in a method

bat=Bat()
print(bat.fly())
print(bat.walk())
print(bat.run())
print(bat.dance())