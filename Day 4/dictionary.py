D1={}
print("empty dictionary:",D1)

D2={'apple':4, 'eggs':3}
print("two term dictionary:",D2)

D3={'dept':{'A':34,'B':345}}
print("nested dictionary:",D3)

D4=dict(name='srija',age=21)
print("alternative construction techniques:",D4)

D5=dict(zip(['hii','hello'],[23,34]))
print("D5:",D5)

D6=dict.fromkeys(['a','b'],[20,30])
print("D6:",D6)

D7=D4.items()
print("D7:",D7)

D4.update(D6)
print("D:",D4)

D4.copy()
print(D3)
print(D4)

# Define a dictionary
D = {'a': 1, 'b': 2, 'c': 3}

# Using keys()
print("Keys:", D.keys())  

# Using values()
print("Values:", D.values())  

# Using items()
print("Items:", D.items())  

# Using copy()
D_copy = D.copy()
print("Copy of Dictionary:", D_copy)  

# Using get() method
print("Get 'b':", D.get('b', 0))  
print("Get 'x' (default value 0):", D.get('x', 0))  


# d.keys(), D.values(),D.items(),D.copy(),D.get(key,default)