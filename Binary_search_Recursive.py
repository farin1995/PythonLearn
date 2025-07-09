def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Target not found
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11,0,55,0,9]
target = 9


# Recursive
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print("Recursive: Found at index", result)