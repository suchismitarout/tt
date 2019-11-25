def prime_num_in_range(range1, range2):
    for i in range(range1, range2+1):
        for j in range(2, i):
            if i %j == 0:

                break
        else:
            print(i, "", end= "")

prime_num_in_range(10, 30)