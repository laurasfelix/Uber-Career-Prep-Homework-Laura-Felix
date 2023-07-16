def merge(nums):
    nums.sort()
    listy = []
    for i in nums:
        if nums.index(i) == 0:
            listy.append((i[0], i[1]))
            prev = i
        else:
            if i[1] > prev[0] and i[0] == prev[1]:
                listy.append((prev[0], i[1]))
                prev = listy[-1]
            elif i[1] < prev[1] and i[0] > prev[0]:
                listy.append((prev[0], prev[1]))
                prev = listy[-1]
            elif prev[0] < i[0] < prev[1]:
                listy.append((prev[0], i[1]))
                prev = listy[-1]
            else:
                listy.append((i[0], i[1]))
                prev = listy[-1]
    if listy[1][0] < listy[0][1] < listy[1][1]:
        listy.pop(0)
    listy = list(set(listy))
    listy.sort()

    lisp = listy[:]

    for k, i in enumerate(listy):
        if listy[-1][1] > i[1] and listy[-1][0] == i[0]:
            lisp.pop(lisp.index(i))

    return lisp


print(merge([(5, 8), (6, 10), (2, 4), (3, 6)]))
print(merge([(10, 12), (5, 6), (7, 9), (1, 3)]))
print(merge([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
