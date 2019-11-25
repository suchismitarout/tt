def feb_seq(num):
    n1 = 0
    n2 = 1
    for i in range(2, num):
        nth = n1+ n2
        n1 = n2
        n2 = nth
        print(n2)

feb_seq(9)
