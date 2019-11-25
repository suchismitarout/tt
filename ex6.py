dict1 = {"name": "abc", "loc": "blr"}
for key, value in dict1.items():
    new = dict([(value,key)])
    print(new)

new_dict = dict([(value,key) for key, value in dict1.items()])
print(new_dict)


x = 10
y = 20
x,y = y,x
print(x,y)