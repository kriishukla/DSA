def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, d):
    n = len(arr)
    if n == 0:
        return arr

    d %= n  # Adjust rotation count if it exceeds array length

    reverse_array(arr, 0, n - 1)  # Reverse the entire array
    reverse_array(arr, 0, d - 1)  # Reverse the first 'd' elements
    reverse_array(arr, d, n - 1)  # Reverse the remaining elements after 'd'

    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = left_rotate(arr, d)
print(rotated_arr)  # Output: [3, 4, 5, 1, 2]
