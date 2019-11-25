from cpu_utilisation import *
with open("C:/Users/Ranjitha/PycharmProject/tt/cpu.txt", "r") as fread:
    content = fread.read().split()
    # print(content)
    dict2 = {}
    for i in content:
        v = i.split(",")
        # print(v[0])
        result = add_key_value(dict2, v[0], v[1])
    print(result)

    