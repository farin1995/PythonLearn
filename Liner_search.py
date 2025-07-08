def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
