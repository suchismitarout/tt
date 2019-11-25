def kangaroo_pro(x1, v1, x2, v2):
    if (v1 > v2) and ((x2-x1) % (v1 - v2) == 0):
        print("YES")
    else:
        print("NO")

kangaroo_pro(0, 3, 5, 2)



