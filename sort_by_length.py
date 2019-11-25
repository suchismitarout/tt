def sort_by_length(l):
    for i in range(len(l)):
        for j in range(1, len(l)-i):
            if len(l[j-1]) < len(l[j]):
                l[j-1],l[j] = l[j],l[j-1]
    print(l)

sort_by_length(["rain", "queen", "forest", "pig"])