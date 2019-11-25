def plusMinus(arr):
    count = 0
    count1 =0
    count2 = 0
    l = len(arr)
    new = []
    for i in arr:
        if (i < 0):
            count += 1
        if (i > 0):
            count1 +=1
        if (i == 0):
            count2 +=1
    p = count/l
    q = count1/l
    r = count2/l
    q = "{0:.6f}".format(q)
    p = "{0:.6f}".format(p)
    r = "{0:.6f}".format(r)
    new.append(q)
    new.append(p)
    new.append(r)


        # if (i > 0):
        #     count += 1
        # q = count/l
        # new.append(q)
        # if (i == 0):
        #     count += 1
        # m = count/l
        # new.append(m)

    print(new)


plusMinus([-4,3,-9,0,4,1])