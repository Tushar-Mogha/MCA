import copy

# Original list with nested list
original_list = [1, 2, 3,[3, 4,5]]

# Create a shallow copy
shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copied_list[3][0] = 10

# Both lists reflect the change in the nested list
print("Original List:", original_list)        # Output: [1, 2, [10, 4]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [1, 2, [10, 4]]
