def sort_descending(list1):
    n = len(list1)
    for i in range(n):
        for j in range(1, n-i):
            if list1[j-1] < list1[j]:
                list1[j-1],list1[j] = list1[j],list1[j-1]
    print(list1)


sort_descending([5, 3, 7, 2, 8, 4])