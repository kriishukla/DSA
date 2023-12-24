def modif_kadane(arr):
    for i in range(0,len(arr)):
        arr[i]=-arr[i]
    res=arr[0]
    sum=0
    for i in range(0,len(arr)):
        sum=max(0,sum+arr[i])
        res=max(sum,res)
    return res
def circsum(arr):
    circ=sum(arr)+modif_kadane(arr)
    return circ

print(circsum([8,-4,3,-5,4]))