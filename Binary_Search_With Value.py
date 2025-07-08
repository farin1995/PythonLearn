def binary_search(arr, target):

    arr.vals = []
    arr.index = 0

    if arr[0] == target:
        return 0
    elif arr[0] < target:
        return binary_search(arr, target)

    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11]
target = 7

# Iterative
result = binary_search(arr, target)
print("Iterative: Found at index", result)

# Recursive
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print("Recursive: Found at index", result)