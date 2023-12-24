sum=0
maxi=0
arr= list(map(int, input().split()))
for i in range(len(arr)):
    sum=sum+arr[i]
    sum=max(0,sum)
    maxi=max(sum,maxi)
print(maxi)