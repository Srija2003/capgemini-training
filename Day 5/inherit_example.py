class School:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def details(self):
        self.name = input("Enter the name: ")
        print("Name:", self.name)
        self.marks = int(input("Enter the marks: "))
        print("Marks:", self.marks)
        
class College(School):
    def __init__(self, name, marks, Dept):
        super().__init__(name, marks)  # Call the parent constructor
        self.Dept = Dept
        
    def PG(self):
        print("PG Dept:", self.Dept)
        self.marks = int(input("Enter the PG marks: "))
        print("PG Marks:", self.marks)
        
    def UG(self):
        self.marks = int(input("Enter the UG marks: "))
        print("UG Marks:", self.marks)

# Create an instance of College with initial values
c = College("Default Name", 0, "Computer Science")

# Call methods
c.details()
c.UG()
c.PG()
