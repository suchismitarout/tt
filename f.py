def birthday(s, d, m):
    count = 0
    n = len(s)
    for i in range(0, n):
        total = sum(s[i:m + i])
        print(total)
        if total == d:
            count += 1
    return count

g = birthday([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1], 18, 7)
print(g)
