def duplicate(nums):
    dicty = {}
    for i in nums:
        if i not in dicty:
            dicty[i] = 1
        else:
            dicty[i] += 1
    return list(dicty.keys())


print(duplicate([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
