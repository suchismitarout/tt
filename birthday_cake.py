def birthday_cake(list1, sum_ele, occ):
    count = 0
    length = len(list1)
    for i in range(0, length-1):
        if list1[i]+list1[i+1] == sum_ele:
            count +=1
            occ -=1
    print(count)


birthday_cake([4], 4, 1)



