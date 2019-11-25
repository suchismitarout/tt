string1 = "1hello24"

result = ''.join(filter(lambda i:i.isdigit(), string1))
print(result)


import re

test_string = "7world23"

res = re.sub("\D", "", test_string)
print(str(res))

test_string1 = "123ghhj354bhhj89"
res1 = re.findall("\d+", test_string1)
rs = map(int, res1)
result1 = max(rs)
print(result1)