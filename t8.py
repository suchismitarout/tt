def reverse_string(s):
    nw_st = " "
    length = len(s) - 1
    for i in s:
        nw_st = nw_st + s[length]
        length = length - 1
    print(nw_st)


m = input()
reverse_string(m)
