def display(data):
    print(f"the avg of 4 numbers is {data} ")
    
def get_input():
    a = int(input("enter a:"))      #taking inputs
    b = int(input("enter b:"))
    c = int(input("enter c:"))
    d = int(input("enter d:"))
    n = int(input("enter n:"))
    return (a, b, c, d, n)
    
def add_num(a, b, c, d,):     #creating a function which adds the 4 numbers
    result = (int(a) + int(b) + int(c) + int(d))      #adding the numbers
    return (result)         

def ave(result, n):        
    
    averag = int(result) / int(n)
    return (averag)

def main():
    a,b,c,d,n =get_input()
    result = add_num(a,b,c,d)
    averag = ave(result,n)
    display(averag)  
main()