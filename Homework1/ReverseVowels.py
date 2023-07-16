def reverse(og):
    listy = []
    listy2 = list(og)
    for i in range(len(og)):
        if og[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            listy.append(og[i])

    listy.sort(reverse=True)
    print(listy)

    for i in range(len(og)):
        if listy2[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            listy2[i] = listy[0]
            listy.pop(0)

    return ''.join(listy2)


print(reverse("Uber Career Prep"))
