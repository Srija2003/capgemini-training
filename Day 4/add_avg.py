def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num  
    return total

def calculate_average(numbers):
    if len(numbers) == 0:
        return None  
    total = calculate_sum(numbers)  
    return total / len(numbers)

def main():
   
        user_input = input("Enter a list of numbers separated by spaces: ").strip()
        
        if not user_input:
            print("No numbers entered. Please try again.")
            return
        
        numbers = list(map(float, user_input.split()))
        
        if not numbers:
            print("No valid numbers provided.")
            return
        
        total = calculate_sum(numbers)
        avg = calculate_average(numbers)
        
        print(f"Addition: {total}")
        print(f"Average: {avg:.2f}")  
    

main()
