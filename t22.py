from collections import Counter
c = Counter()
with open("foo.txt", 'r') as fp:
    for line in fp:
        c.update(line.split())
    print(c)



num_list = [0, 2, 3, 4, 0, 6, 7, 10]
x = [i for i in num_list if i != 0]
a = [0 for i in range(num_list.count(0))]
x.extend(a)
print(x)