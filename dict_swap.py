dict1 = {"name": "abc", "age": 25, "loc": "blr"}
d = dict([(values,keys) for keys,values in dict1.items()])
print(d)