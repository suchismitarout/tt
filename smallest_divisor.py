def smallest_divisor(num):
    result_list = []
    for i in range(2, num+1):
        if (num % i == 0):
            result_list.append(i)
    result_list.sort()
    print(result_list[0])


smallest_divisor(75)

