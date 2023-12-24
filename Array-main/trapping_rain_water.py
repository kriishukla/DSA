def get_water(arr, n):
    res = 0

    l_max = [0] * n
    r_max = [0] * n

    l_max[0] = arr[0]
    for i in range(1, n):
        l_max[i] = max(arr[i], l_max[i - 1])

    r_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        r_max[i] = max(arr[i], r_max[i + 1])

    for i in range(1, n - 1):
        res += min(l_max[i], r_max[i]) - arr[i]

    return res


arr = [5, 0, 6, 2, 3]
n = 5

print(get_water(arr, n))
