# 1>2
# 2>3
# 3>4
# 4>5
# 1>2>3>4>5
def is_sorted(arr):
    for i in range (1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    return True