def second(arr):
    res=-1
    largest=0
    for i in range(1,len(arr)):
        if arr[i]>arr[largest]:
            res=largest
            largest =i
        elif arr[i]<arr[largest]:
            if res ==-1 or arr[i]>arr[res]:
                res=i

    return arr[res]
arr=[2,3,4,5,6,999,111,0,8]
print(second(arr))
