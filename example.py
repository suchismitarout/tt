def arrangeOddAndEven(arr,  n):
    odd_ind = 1
    even_ind = 0
    while True:
        while (even_ind < n and list1[even_ind] % 2 == 0):
            even_ind +=2
        while (odd_ind < n and list1[odd_ind] % 2 != 0):
            odd_ind +=2
        if (even_ind < n and odd_ind < n):
            temp = list1[even_ind]
            list1[even_ind] = list1[odd_ind]
            list1[odd_ind] = temp
        else:
            break


if __name__ =='__main__':
    list1= [2, 5, 1, 5, 6, 8, 9, 4]
    n = 8
    arrangeOddAndEven(list1, n)
    for i in range(0, n):
        print(list1[i], "",end="")





