import re

card = "1133-4815-6745-4361"
p = re.compile(r'(?:\d{4}-){3}\d{4}|\d{16}')
e = re.match(p, card)
if e:
    print("it is valid")
else:
    print("it is not valid")

list1 = [12,34,13,23,54]
max = max(list1[0],list1[1])
second_max = min(list1[0], list1[1])
for i in range(2, len(list1)):
    if list1[i] > max:
        second_max = max
        max = list1[i]
    else:
        if list1[i] > second_max:
            second_max = list1[i]
print(max)
print(second_max)
