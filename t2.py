def missing_num(num_list):
    original_lst = [x for x in range(num_list[0], num_list[-1]+1)]
    num_list = set(num_list)
    return list(num_list ^ set(original_lst))
print(missing_num([1,2,3,5,7]))
