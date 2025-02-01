
def get_input():
    n=int(input("enter n:"))
    return n

def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i <= int(num**0.5):  
        if num % i == 0:
            return False
        i += 1  
    return True

def print_primes(n):
    num = 2  
    while num <= n:  
        if is_prime(num):
            print(num)
        num += 1  
def main():
    n=get_input()
    
    print_primes(n)
    
main()
