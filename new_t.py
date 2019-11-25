first_list=[2,4,5,7]
n=len(first_list)
value1=(n+1)*(n+2)/2
value2=sum(first_list)
result=value2-value1
print(int(result))


def find_missing_elements(j):
    k = str(j)
    res = [ele for ele in range(max(j)+1) if ele not in j]
    return res
print(find_missing_elements([2,5,7,9]))