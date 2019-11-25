def balanced_string(parent_string):
    c=0
    for i in range(len(parent_string)):
        if (parent_string[i]=='('):
            print(parent_string[i],end='')
            c+=1
        elif (parent_string[i]==')') and c!=0:
            print(parent_string[i],end='')
            c-=1
        elif (parent_string[i]!=')'):
            print(parent_string[i],end='')
    if c!=0:
        for i in range(c):
            print(")",end='')

str="gau)ra)v(ku(mar(rajput))"
balanced_string(str)
