class employee():
    def __init__(self,name,id,position):
        self.name=name
        self.id=id
        self.position=position
    def display(self):
        print(f"the details of the employee are:{self.name}, {self.id},{self.position}")
class student():
    def __init__(self,name,rollno,location):
        self.name=name
        self.rollno=rollno
        self.location=location
    def display(self):
        print(f"the student details are:{self.name},{self.rollno},{self.location}")
        
Em=[]
# Create an empty list to store Employee objects

# Get the number of employees from the user
num_employees = int(input("Enter the number of employees: "))

# Loop to take dynamic input for each employee
for i in range(num_employees):
    print(f"\nEnter details for Employee {i + 1}:")
    name = input("Enter name: ")
    salary = float(input("Enter id: "))
    position=input("enter the position:")
    Em.append(employee(name, salary,position))  # Add the Employee object to the list



stu=[student('student1',6677,'add1'),student('stu2',7890,'add2')]

print("employee details")
for em in Em:
    em.display()
    
print("student details:")
for s in stu:
    s.display()