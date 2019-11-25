st = [23, 56, 12, 45, 13, 11, 15]
sum=0
even_sum=0
odd_sum=0
even=[]
odd=[]
n=len(st)
for i in range(n):
    if i % 2 == 0:
        even.append(st[i])
        even_sum = even_sum + st[i]
    else:
        odd.append(st[i])
        odd_sum=odd_sum + st[i]
print("even = ", even)
print("odd = ", odd)
print("even_sum=", even_sum)
print("odd_sum=", odd_sum)