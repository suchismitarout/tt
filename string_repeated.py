def repeating_string(s, n):
    if len(s) == 1:
        return n
    else:
        return sum(1 for i in range(n) if s[i % len(s)] == 'a')

s = 'aba'
n = 10
result = repeating_string(s, n)
print(result)