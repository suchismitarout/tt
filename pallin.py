def pallindrome_num(num):
    num2 = ""
    for i in str(num):
        num2 = i + num2
    if int(num2) == int(num):
        print("it is a pallindrome number")
    else:
        print("it is not a pallindrome number")

n = 150
pallindrome_num(n)
