def get_input():
    nums = [int(input(f"Enter number {i + 1}: ")) for i in range(int(input("Enter the size of nums: ")))]
    return nums

def small_bigg(nums):
    small = nums[0]
    big = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < small:
            small = nums[i]
        if nums[i] > big:
            big = nums[i]
    return small, big

def main():
    nums = get_input()
    small, big = small_bigg(nums)
    print("Smallest Number:", small)
    print("Biggest Number:", big)

main()
