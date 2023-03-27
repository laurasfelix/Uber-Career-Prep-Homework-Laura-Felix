def backspace(one, two):

    listy1 = list(one)
    listy2 = list(two)

    for k, i in enumerate(listy1):
        if i == "#":
            listy1.pop(k)
            listy1.pop(k-1)

    for k, i in enumerate(listy2):
        if i == "#":
            listy2.pop(k)
            listy2.pop(k-1)

    after_one = "".join(listy1)
    after_two = "".join(listy2)

    return after_one == after_two


print(backspace("Uber Career Prep", "u#Uber Careee#r Prep"))
