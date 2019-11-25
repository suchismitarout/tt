def second_large(list1):
    large_ele = max(list1[0], list1[1])
    second_large_ele = min(list1[0], list1[1])
    for i in range(2, len(list1)):
        if list1[i] > large_ele:
            second_large_ele = large_ele
            large_ele = list1[i]
        else:
            if list1[i] > second_large_ele:
                second_large_ele = list1[i]
    print(second_large_ele)

second_large([14, 2, 25, 50, 81, 62])