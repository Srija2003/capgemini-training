array =[]
print("enter the size of array:")
size= int(input())
print("enter the array")
for i in range(size):
    array.append(int(input(f"enter the element {i}:")))
    
print(array)