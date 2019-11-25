def sort_string(strng):
    char = [char for char in strng]
    # print(char)
    for i in range(len(char)):
        for j in range(len(char)-1):
            if char[j] > char[j+1]:
                char[j],char[j+1] = char[j+1],char[j]
    return char
res=sort_string('juarpocl')
print(res)
res = ''.join(res)
print(res)
