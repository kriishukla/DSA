def max_sum(arr, n, k):
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum


arr = [1, 8, 30, -5, 20, 7]
n = 6
k = 3

print(max_sum(arr, n, k))
