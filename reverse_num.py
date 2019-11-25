def rev_num(num):
    num1 = str(num)
    num2 = ""
    for i in num1:
        num2 = i + num2
    print(int(num2))

rev_num(123)
