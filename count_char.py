count=0
string_given = 'hello world'
for ch in string_given:
    if ch == 'l':
        count=count+1
print("l is present",count,"times")

st=''
string_two='helloo'
for i in string_two:
    if i not in st:
        st = st + i
        count = 1
    else:
        count = count + 1
print(st,count)
def split(word):
   return [ch for ch in word]

print(split('hello'))


