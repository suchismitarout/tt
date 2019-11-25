def intesection(arr1, arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    print(result)


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    intesection(arr1, arr2)

my_list = ["grep", "ee", "geeg", "peep", "red"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
print(result)

from collections import Counter
list1 = ["grep", "mango", "grep", "apple", "mango", "fig", "mango"]
c = Counter(list1)
print(c)






