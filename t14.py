import re

txt = "Hey its a beautiful day"
x = re.search("^hey.*day$", txt)
if x:
    print("it is there")
else:
    print("it is not there")


y = re.findall("hello", txt)

print(y)

z = re.search("\s", txt)
print(z.start())

m = re.search("^H", txt)
print(m.start())

p = "umbrella"
t = iter(p)
print(next(t))

