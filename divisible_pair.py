def divisible_sum_pair(n,k,ar):
    n = len(ar)
    count = 0
    for i in range(0, n):
        for j in range(0, i):
             if ((ar[i]+ar[j]) % k == 0):
                 count +=1

    return count
        # for j in range(n):
        #     if (ar[i]+ar[j])% n == 0:
        #         print([ar[i],ar[j]])
        #
        #


p = divisible_sum_pair(6,5,[1,2,3,4,5,6])
print(p)