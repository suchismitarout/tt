def find_digit(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    print(count)

find_digit(458796)