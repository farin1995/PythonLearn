def quick_sort(arr):
    """
    Sorts a list using the Quicksort algorithm.
    This implementation uses a simple approach with list comprehensions.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage:
my_list = [10, 7, 8, 9, 1, 5]
sorted_list = quick_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")

another_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_another_list = quick_sort(another_list)
print(f"Original list: {another_list}")
print(f"Sorted list: {sorted_another_list}")
