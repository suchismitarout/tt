def oddevenindex(list1):
    odd_index = []
    even_index = []
    for i in range(0, len(list1)):
        if i % 2 == 0:
            even_index.append(list1[i])
        else:
            odd_index.append(list1[i])
    print(odd_index + even_index)


list1 = [3, 1, 5, 7, 6, 6, 4, 8, 2, 3]
oddevenindex(list1)
