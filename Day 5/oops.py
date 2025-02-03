class employee:

    def __init__(self,name,emp_id, emp_add):
        self.name=name
        self.emp_id=emp_id
        self.emp_add=emp_add
    
    def emp_details(self):
        print(f"employee name is:{self.name}   employee id is:{self.emp_id}  employee add is:{self.emp_add}")
        
    
e1=employee(input("enter name:"),input("enter id:"),input("enter add:"))
e2=employee(input("enter name:"),input("enter id:"),input("enter add:"))
e3=employee(input("enter name:"),input("enter id:"),input("enter add:"))

e1.emp_details()
e2.emp_details()
e3.emp_details()
                      
   
