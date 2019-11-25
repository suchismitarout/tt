list1 = [23, 45, 12, 36]
list2 = "12345"

if isinstance(list1, list):
    print("list1 is a list")
elif isinstance((list2, list)):
    print("list2 is a list")


test_dict = {'gfg': None, 'is': 4, 'for': 2, 'CS': 10}

print(test_dict)
print(str(test_dict))
res = not all(test_dict.values())
print("Does test_dict has None values: ", str(res))

res1 = None in test_dict.values()
print("Does the dict has None values: ", str(res1))