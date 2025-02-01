import dis
def data():
    a=int(input())
    b=int(input())
    return(a, b)
def add(a, b):
    res=a+b
    return res

def sub( a , b):
    r=a-b
    return r
def main():
    a, b=data()
    v = add(a,b)
    w = sub(a,b)
    print(v)
    print(w)
    dis.dis(add)
    dis.dis(sub)
    
main()