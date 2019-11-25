def ascending(list1):
    n=len(list1)
    for i in range(n):
        for j in range(1, n-i):
            if list1[j-1] > list1[j]:
                list1[j-1],list1[j] = list1[j],list1[j-1]

    print(list1)

ascending([5, 2, 4, 1, 3, 7])


