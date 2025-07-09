import threading

def merge_sort(arr,arr2):
    if len(arr) <= 1:
        return arr
    if len(arr2) <= 1:
        return arr2
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mid2 = len(arr2) // 2
    left2 = arr[:mid2]
    right2 = arr[mid2:]
    # Create threads for sorting left and right halves
    left_thread = threading.Thread(target=lambda: merge_sort(left,left2))
    right_thread = threading.Thread(target=lambda: merge_sort(right,right2))
    # left_thread2 = threading.Thread(target=lambda: merge_sort(left2))
    # right_thread2 = threading.Thread(target=lambda: merge_sort(right2))
    left_thread.start()
    right_thread.start()
    # left_thread2.start()
    # right_thread2.start()
    left_thread.join()
    right_thread.join()
    # left_thread2.join()
    # right_thread2.join()

    return merge(left, right, left2, right2)

def merge(left, right, left2, right2):
    result = []
    i = j = k = l = 0

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while k < len(left2) and l < len(right2):
        if left2[k] < right2[l]:
            result.append(left2[k])
            k += 1
        else:
            result.append(right2[l])
            l += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    result.extend(left2[k:])
    result.extend(right2[l:])
    return result

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    arr2 = [11, 27, 34, 3, 2, 8, 10]
    print("Original array:", arr, arr2)
    sorted_arr = merge_sort(arr, arr2)
    print("Sorted array:", sorted_arr)
