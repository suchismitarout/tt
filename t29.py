my_list = [3, 4, 2, 6, 10, 12]
my_list.append(my_list.pop(my_list.index(2)))
print(my_list)

test_dict = {'Gfg': 11, 'for': 2, 'CS': 11, 'geeks': 8, 'nerd': 2}

res = [key for key in test_dict]
print(res)
print(test_dict.values())

print(min(test_dict.values()))

def Key(x):
    return x%2
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort = sorted(nums, key = Key)
print(sort) 