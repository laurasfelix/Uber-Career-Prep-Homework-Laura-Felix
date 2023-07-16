def missing(nums, n):
    prev = 0
    for i in nums:
        if i-1 != prev:
            return i-1
        else:
            prev = i
    if n == 2:
        return 2


print(missing([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))
