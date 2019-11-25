def is_part(full_string, target):
    return target in full_string


print(is_part("Home Town", "Town"))


some_list = ['abc-123', 'def-345', 'xyz-256']
matching = [s for s in some_list if 'abc' in s]
print(matching)

import re
some_string = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM'
s = re.findall('\S+@+\S+', some_string)
print(s)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8]
print((list(set(list1 + list2))))
