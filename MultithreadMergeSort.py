def merge_sort(arr, key_index=0):
    # Base case: if the array has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], key_index)
    right_half = merge_sort(arr[mid:], key_index)

    # Merge the sorted halves
    return merge(left_half, right_half, key_index)

def merge(left, right, key_index):
    sorted_array = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i][key_index] <= right[j][key_index]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append any remaining elements from the left or right half
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example usage
multi_array = [
    [3, 2, 5],
    [1, 4, 9],
    [2, 8, 6],
    [0, 7, 3]
]

sorted_array = merge_sort(multi_array, key_index=0)  # Sort by the first column
print("Sorted Array:", sorted_array)
