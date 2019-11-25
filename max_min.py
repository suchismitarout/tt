def miniMaxSum(arr):
    n = len(arr)
    min_ele = 0
    max_ele = 0
    for i in range(0,n-1):
        # print(i)
        min_ele= min_ele + arr[i]
    for i in range(1,n):
        # print(i)
        max_ele = max_ele + arr[i]

    print(max_ele)
    print(min_ele)

miniMaxSum([7,69,2,221,8974])