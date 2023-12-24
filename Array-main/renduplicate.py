def remove_duplicates(arr):
    n = len(arr)
    res = 1

    for i in range(1, n):
        if arr[res - 1] != arr[i]:
            arr[res] = arr[i]
            res += 1

    return res
arr = [1, 2, 2, 3, 4, 4, 4, 5]
new_length = remove_duplicates(arr)
print(arr[0:new_length:1]) 
