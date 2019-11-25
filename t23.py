some_string = 'FUNNY'
unique = []
for char in some_string:
    if char not in unique:
        unique.append(char)
print(len(unique))

a = [1, 2, 3, 4]
for i in a:
    print(i, end=" ")


def test_sum():
    assert sum([1, 2, 3]) == 6, "should be 6"


def test_sum1():
    assert sum((2, 2, 2)) == 6, "should be 6"


if __name__ == '__main__':
    test_sum()
    test_sum1()
    print("everything passed")




