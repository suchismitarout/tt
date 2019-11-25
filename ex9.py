s = "murder redrum"
m = s[-6:]
n = s[:-7]

p = ""
for i in m:
    p = i + p

if p == n:
    print("it is pallindrom string")

