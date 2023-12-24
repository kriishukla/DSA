def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

    return arr

arr = list(map(int,input().split()))
low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] == 1:
        mid += 1
    elif arr[mid] == 2:
        swap(arr, mid, high)
        high -= 1
    elif arr[mid] == 0:
        swap(arr, mid, low)
        low += 1

print(arr)