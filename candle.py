def birthdayCakeCandles(ar):
    max_ele = ar[0]
    count = 0
    for i in range(len(ar)):
        if ar[i] > max_ele:
           max_ele = ar[i]
    for j in ar:
        if j == max_ele:
            count +=1


           # for j in ar:
           #     if j == max_ele:
           #         count +=1


    return count

candle = birthdayCakeCandles([44,53,31,27,77,60,66,77,26,36])
print(candle)