def miniMaxSum(arr):
    M = sorted(arr,reverse = True)
    m= sorted(arr)
    print(M)
    print(m)
    total_sum = 0
    total = 0
    for i in range(len(M)-1):
        total_sum = total_sum +M[i]
    for k in range(len(m)-1):
        total = total+m[k]
    print(total, total_sum, end=" ")

miniMaxSum([25,21,10,36,11])