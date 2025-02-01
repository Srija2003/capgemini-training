def display(res):
    print(f"the max number is: {res}")
    
def get_input():
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = int(input("enter c:"))
    d = int(input("enter d:"))
    
    return(a, b, c, d)
def max_num(a, b, c, d):
    if a > b and a > c and a > d:
      print(f"the largest number is a:{a}")
    elif b>c and b>d:
      print(f"the largest number is b:{b}")
    elif c>d:
      print(f"the largest number is c:{c}")
    else:
      print(f"the largest number is d:{d}")
    return(max_num)
def main():
    a,b,c,d = get_input()
    res = max_num(a,b,c,d)
    display(res)
    
main()