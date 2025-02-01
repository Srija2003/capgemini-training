
'''a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))
d = b**2 - 4 * a * c
ans = (-b+(d**0.5))/(2*a)
ans1 = (-b-(d**0.5))/(2*a)

print(f"the ans is {ans} and {ans1}")'''

def get_input():
    a=float(input("enter a:"))
    b=float(input("enter b:"))
    c=float(input("enter c:"))
    
    
    return a,b,c

def discriminant(a,b,c):
    d=b*b-4*a*c
    print("discriminant:")
    return d

def quadratic(d,a,b):
    root1=(-b+d**0.5)/(2*a)
    root2=(-b-d**0.5)/(2*a)
    
        
    return (f"the roots are :{root1},{root2}")

def main():
    a,b,c=get_input()
    d=discriminant(a,b,c)
    print(d)
    ans=quadratic(d,a,b)
    print(ans)
    
main()
    
    
    






