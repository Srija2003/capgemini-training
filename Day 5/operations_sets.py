def union():
    set_a={23,'apple'}
    set_b={24,'banana'}
    u=set_a|set_b
    return u

def intersection():
    set_a={25,'ball'}
    set_b={43,25}
    i=set_a&set_b
    return i

def difference():
    set_a={'mango',456,23}
    set_b={456,89}
    q=set_a-set_b
    return q

def sym_difference():
    set_a={34,'cat'}
    set_b={'mammal',66,34}
    s=set_a^set_b
    return s

def subsets():
    set_a={'monkey',67}
    set_b={'monkey',67,90}
    c=set_a<=set_b
    d=set_a>=set_b
    return c,d
def disjoint():
    set_a={12,34,'kite'}
    set_b={23,12,'queen'}
    return set_a.isdisjoint(set_b)
    
    
def main():
    u=union()
    i=intersection()
    q=difference()
    s=sym_difference()
    c,d=subsets()
    o=disjoint()
    print("the union:",u)
    print("intersection:",i)
    print("difference is:",q)
    print("symmetric difference:",s)
    print("substes:",c,d)
    print("disjoint:",o)
    
    
main()