def add_key_value(dict1, key, value):
    if value in dict1:
        dict1[value].append(key)
    else:
        dict1[value] = [key]

    return dict1


# d = {24: ["c1"], 34: ["c2"], 25: ["c3"], 24: ["c4"]}
# print(add_key_value(d, "c1", 24))

# dict1 = {24:["c1"], 25:["c2"], 26:["c3"], 35:["c4"]}
# def add_k_v(dict1,key,value):
#     if value in dict1:
#         dict1[value].append(key)
#     else:
#         dict1[value] = [key]
#     return dict1
#
# print(add_k_v(dict1,"c5",24))




