class Example:
    def __init__(self,name):
        print(f"first constructor:hello {name}")
        
    def __init__(self,age):
        
        print(f'second constructor: age is {age}')
        
        
obj=Example(20)

class Example:
    def __init__(self, *args):
        if len(args)==1:
            print(f"hello{args[0]}")
        elif len(args)==2:
            print(f"hello {args[0]} age is {args[1]} yeras old")

e=Example("bob")
e=Example("hello",23)
            

class Example:
    def __init__(self,studentName, **kwargs):
        self.studentName=studentName
        if "name" in kwargs and "age" in kwargs:
            print(f"hello {kwargs['name']},you are {kwargs['age']}")
        elif "name" in kwargs:
            print(f"hello {kwargs['name']}")
        self.xfield=kwargs['name']
            
obj1=Example("stu1",name="alice")
obj2=Example("stu2",name="bob")
print(obj1.studentName)
print(obj2.studentName)

class DeconstructorExample:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
    
    def __del__(self):
        print(f"object {self.name} is deleted")


#create and delete an object
obj=DeconstructorExample("sample")
del obj