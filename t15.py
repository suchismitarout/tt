import json

x = {"name":"abc", "age":27, "address":"blr"}

y = json.dumps(x)

print(y)

print(json.dumps({"name": "John", "age": 30}))

print(json.dumps(["apple", "bananas"]))
print(json.dumps(True))
print(json.dumps(("apple", "bananas")))
