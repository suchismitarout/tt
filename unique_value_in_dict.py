test_dict = [{"abc": 1}, {"efg": 1}, {"klm": 2}, {"xyz": 3}, {"tfc": 3}]

res = list(set(val1 for val in test_dict for val1 in val.values()))
print(str(res))




# string1 = "2 dogs are standing behind 1 guy"
# res =i for i in string1.split() if i.isdigit()

l1 = [2, 4, 7]
l2 = [9]
l1.extend(l2)
print(l1)

l1.extend('3')
print(l1)


