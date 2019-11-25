list1 = [2,11,24,45,13,47]
l=[]
for i in range(len(list1)):
    if list1[i] %2 == 0:
        l.append(str(i))
print(','.join(l))


def profile():
    name = "shrey"
    loc = "blr"
    return name,loc

p,q = profile()
print(q)



