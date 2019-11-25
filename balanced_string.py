def single_string(s):
    n = len(s)
    st = []
    for i in range(n):
        if s[i] == '(':
            st.append(s[i])
        else:
            if len(st) == 0:
                return False
            else:
                st.pop()
    return True

if __name__ == '__main__':
    v= single_string("(()")
    if v:
        print("balanced")
    else:
        print("not balanced")





