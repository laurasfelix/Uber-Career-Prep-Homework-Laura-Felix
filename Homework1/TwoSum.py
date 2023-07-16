def twosum(nums, k):
    total = 0
    for k, i in enumerate(nums):
        for p, j in enumerate(nums):
            if k-j == i and p != k:
                total += 1
    return int(total/2)


print(twosum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))
