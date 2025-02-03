def get_input():
    start_range = int(input("Enter the start range: "))
    end_range = int(input("Enter the end range: "))
    return start_range, end_range

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # Check divisors from 2 to n-1
        if n % i == 0:
            return False
    return True

def find_lowest_and_largest_prime(lst):
    primes = [x for x in lst if is_prime(x)]  # Filter primes from the list
    if primes:
        lowest_prime = min(primes)
        largest_prime = max(primes)
        return lowest_prime, largest_prime
    else:
        return None, None

def main():
    start, end = get_input()
    numbers = list(range(start, end + 1))  # Generate numbers in the input range
    lowest, largest = find_lowest_and_largest_prime(numbers)
    if lowest is None:
        print("There are no prime numbers in the specified range.")
    else:
        print(f"The lowest prime number is: {lowest}")
        print(f"The largest prime number is: {largest}")


main()
