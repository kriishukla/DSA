def max_diff(arr):
    res= arr[1]-arr[0]
    minv=arr[0]
    for i in range(1,len(arr),1):
        res=max(res,arr[i]-minv)
        minv=min(arr[i],minv)
    return res

print(max_diff([3,4,7,9,100,103,122]))