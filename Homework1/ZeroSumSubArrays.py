def zerosub(nums):
    total = 0
    for i in range(len(nums)):
        for k in range(i, len(nums)):
            if sum(nums[i:k+1]) == 0 and len(nums[i:k+1]) != 0:
                total += 1
    return total


print(zerosub([8, -5, 0, -2, 3, -4]))
