import re
string1 = "Nutanix is nutanix and NUTANIX NutaniX"
p = re.split("\s", string1)
print(p)
for i in set(p):
    m = p.count("i")
    print(i+str(m),end='')