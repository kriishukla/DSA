def largest_elem(arr):
    max=-1
    for i in range(0,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max

arr=[2,3,4,5,6,999,111,0,-4]
print(largest_elem(arr))