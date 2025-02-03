def list_operations():
    print("### LIST OPERATIONS IN PYTHON ###\n")

    # Creating Lists
    my_list = [10, 20, 30, 40, 50]
    print(f"Original List: {my_list}")

    # Accessing Elements
    print(f"First Element: {my_list[0]}")
    print(f"Last Element: {my_list[-1]}")
    print(f"Slice [1:4]: {my_list[1:4]}")

    # Modifying List
    my_list[1] = 25  # Changing element at index 1
    print(f"After Modification: {my_list}")

    # Adding Elements
    my_list.append(60)  # Append at end
    my_list.insert(2, 100)  # Insert at index 2
    print(f"After Append & Insert: {my_list}")

    # Removing Elements
    my_list.pop()  # Remove last element
    my_list.pop(2)  # Remove element at index 2
    my_list.remove(25)  # Remove specific value
    del my_list[0]  # Delete first element
    print(f"After Removals: {my_list}")

    # List Operations
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b  # Concatenation
    print(f"Concatenated List: {c}")
    c *= 2  # Repeat elements
    print(f"Repeated List: {c}")

    # List Comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares (List Comprehension): {squares}")

    # Sorting & Reversing
    my_list = [3, 1, 4, 2, 5]
    my_list.sort()  # Ascending sort
    print(f"Sorted List: {my_list}")
    my_list.reverse()  # Reverse order
    print(f"Reversed List: {my_list}")

    # Checking Membership
    print(f"Is 3 in List? {'Yes' if 3 in my_list else 'No'}")

    # Copying a List
    copied_list = my_list.copy()
    print(f"Copied List: {copied_list}")

    # Clearing a List
    my_list.clear()
    print(f"Cleared List: {my_list}")

# Run the function
list_operations()
