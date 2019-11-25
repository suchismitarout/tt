text = "Hi my name is John Doe John Doe is my name"
nw_lst = text.split(" ")
new_lst = []
for i in range(len(nw_lst)):
    if i not in new_lst:
        new_lst.append(nw_lst[i])
print(set(new_lst))


