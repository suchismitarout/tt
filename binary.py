def binary_num(list1):
    large = list1[0]
    for i in range(len(list1)):
        if i > large:
            large = i
