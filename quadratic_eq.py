import cmath
a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))
d = b**2 - 4 * a * c
ans = (-b+(d**0.5))/(2*a)
ans1 = (-b-(d**0.5))/(2*a)

print(f"the ans is {ans} and {ans1}")