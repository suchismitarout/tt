string1 = "MOUNTAIN"
count = 0
string2 = ""
for i in string1:
    if i in string2:
        count = count + 1
    else:
        string2 = string2 + i
print(string2)


st = "steel12iron43"
data = ""
for i in st:
    if i.isdigit():
        data = data + i
print(data)
