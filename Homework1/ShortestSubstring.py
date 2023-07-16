def myFunc(e):
    return len(e)


def shortest(og, req):
    listy = []
    for i in range(len(og)):
        for k in range(i, len(og)):
            total = 0
            for p in req:
                if p in og[i:k+1] and req.count(p) <= og[i:k+1].count(p):
                    total += 1
            if total == len(req):
                listy.append(og[i:k+1])
    listy.sort(key=myFunc)
    return len(listy[0])


print(shortest("abracadabra", "abc"))
