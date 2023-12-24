def stock(arr):
    profit =0
    for i in range(0,len(arr)):
        if arr[i]>arr[i-1]:
            profit= profit+arr[i]-arr[i-1]
    return profit

print(stock([1,5,3,8,12]))