def subArraySum(arr, n, target_sum):
    curr_sum = arr[0]
    start = 0

    for i in range(1, n + 1):
        while curr_sum > target_sum and start < i - 1:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == target_sum:
            print("Sum found between indexes", start, i - 1)
            return True

        if i < n:
            curr_sum += arr[i]
    return False

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
target_sum = 23
subArraySum(arr, n, target_sum)
