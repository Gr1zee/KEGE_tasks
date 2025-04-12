for A in range(100):
    flag = True
    for x in range(1000):
        for y in range(1000):
            f = (5 < y) or (x > 32) or (x + 2*y < A)
            if not f:
                flag = False
                break
    if flag:
        print(A)
        break
        