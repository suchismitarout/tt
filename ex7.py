def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            print("this is not a prime number")
            break
    else:
        print("it is a prime number")

prime_number(5)
