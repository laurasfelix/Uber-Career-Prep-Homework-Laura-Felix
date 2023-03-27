def maxmean(nums, k):
    sumy = -10000
    for i in range(len(nums)-k+1):
        if sum(nums[i:i+k]) > sumy:
            sumy = sum(nums[i:i+k])
    return sumy/k


print(maxmean([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))
