class Employee:
    def __init__(self,name,salary,allowance,deduction,medicals):
        self._name=name
        self._salary=salary
        self._allowance=allowance
        self._deduction=deduction
        self._medicals=medicals
        
    def set_salary(self,salary):
        self._salary=salary
    
    def set_allowance(self,allowance):
        self._allowance=allowance
    
    def set_deductions(self,deduction):
        self._deduction=deduction
        
    def set_total_salary(self,totalsalary):
        self._totalsalary=totalsalary
    
    def set_medicals(self,medicals):
        self._medicals=medicals
        
    def get_salary(self):
        return self._salary
    
    def get_allowance(self):
        return self._allowance
    
    def get_medicals(self):
        return self._medicals
    
    def get_deduction(self):
        return self._deduction
    
    def get_totalsalary(self):
        return self._salary+self._allowance-self._deduction+self._medicals
    
emp=Employee("alice", 20000, 3000, 1000,200)
print("salary before update:",emp.get_salary())
print("salary after update:",emp.get_allowance())
print("total salary:",emp.get_totalsalary())

