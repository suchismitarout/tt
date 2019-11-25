def sec_large(l):
    large = max(l[0],l[1])
    second_large = min(l[0],l[1])
    for i in range(2, len(l)):
        if l[i] > large:
            second_large = large
            large = l[i]
        else:
            if l[i] > second_large:
                second_large = l[i]
    print(second_large)


sec_large([12, 45, 24, 89, 65])