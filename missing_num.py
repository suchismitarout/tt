def find_missing_num():
    list_of_num = [1, 3, 4, 5, 6, 7]
    length_list = len(list_of_num)
    total = (length_list+1)*(length_list+2)/2
    sum_of_num = sum(list_of_num)
    missing_num = total - sum_of_num
    print(missing_num)

find_missing_num()