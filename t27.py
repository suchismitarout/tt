rem = lambda num: num % 2
print(rem(10))


def test_lambda(num):
    return lambda x: x * num


n = test_lambda(10)
print(n(5))
