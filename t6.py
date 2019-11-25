def fact_of_num(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)


n = int(input("enter the number: "))
fact_of_num(n)
