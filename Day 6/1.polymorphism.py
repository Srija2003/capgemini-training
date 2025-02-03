class cat:
    def sound(self):
        print("Meow")
    def colour(self):
        print("cat color")
        
class dog:
    def sound(self):
        print("bark")
    def colour(self):
        print("dog color")
        
class hen:
    def sound(self):
        print("chick")
    def colour(self):
        print("hen color")
        
        
for animal in [cat(),dog(),hen()]:
    animal.sound()
    animal.colour()
    