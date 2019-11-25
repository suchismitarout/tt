x = [{'A':[{'name':{'m':[1,2,3]}}]}, {'surname':{'2':[4,2,3]}}]
print(x[1]['surname']['2'])

m = 'aabbbcdan'
count = 0
max = 0
l = []
for i in set(m):
    p = m.count(i)
    print(i+str(p),end='')

a = "GiniiGinnnaaaaProtiiiijayyyyyyyyyyyyyyyi"

count = 0
maxcount = 0
lastCharacter = ""
longestcharacter = ""

for ch in a:
    if(ch == lastCharacter):
        count += 1
        if(count > maxcount):
            maxcount = count
            longestcharacter = ch

    else:
        count = 1
        lastCharacter = ch

print(longestcharacter)
print(maxcount)








