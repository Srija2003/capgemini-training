class Parent:
    def __init__(self):
        self.bigNose = "7cm"
        
    def display_parent(self):
        print("This is a parent class")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
    def display_child(self):
        print("This is the child class")
 
        
child=Child()
child.display_child()
child.display_parent()
print(child.bigNose)

