for A in range(1, 1000):
    f = True
    for x in range(10000):
        func = (x&A == 0) <= ((x &77 == 0) and (x&44 == 0))
        if not func:
            f = False
    if f:
        print(A)
        break