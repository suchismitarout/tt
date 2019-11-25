import re

string_input = "The rain in Spain"
x = re.findall(r"\bain", string_input)
print(x)

y = re.findall("\s", string_input)
print(y)
z = re.findall("\S", string_input)
print(z)
p = re.findall("\D", string_input)
print(p)

w = re.sub("\s", "9", string_input,1)
print(w)