def k(one, two, k):
    total = 0
    listy = []
    for i in range(len(one)):
        if one.count(one[i]) != two.count(one[i]) and one[i] not in listy:
            total += 1
            listy.append(one[i])
    if total != k:
        return False
    else:
        return True


print(k("baseball", "basketball", 1))
