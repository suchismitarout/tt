import re
txt = "192.168.10.41"
txtmatch = re.match(r"^((\d){1,3}.){3}(\d){1,3}$",txt)
if txtmatch:
    print(txtmatch.group())
else:
    print("not valid")


string1 = "mountain"
string2 = ""
for i in string1:
    string2 = i + string2
print(string2)





