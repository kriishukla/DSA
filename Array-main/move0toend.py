def move_zeros_to_end(arr):
    cnt=0   
    for i in range(0,len(arr)):
        if arr[i]!=0:
            temp = arr[i]
            arr[i] = arr[cnt]
            arr[cnt] = temp
            cnt=cnt+1
    return arr

arr = [0, 0, 0, 0, 2, 4, 3, 3, 30, 1, 2, 0, 0, 2]
print(move_zeros_to_end(arr))