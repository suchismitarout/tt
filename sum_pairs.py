list1=[2, 4, 7]
n=len(list1)
sum=0
for i in range(n):
    for j in (i+1, n):
        sum = sum + list1[i]*list1[j]
    print(sum)
