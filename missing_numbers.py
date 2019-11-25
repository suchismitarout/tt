def missing_numbers(l):
    org_list = [x for x in range(l[0],l[-1]+1)]
    l = set(l)
    return (list(l ^ set(org_list)))

print(missing_numbers([2, 4, 6, 7, 8]))