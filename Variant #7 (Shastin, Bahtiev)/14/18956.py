for A in range(1, 1000000):
    for x in "0123456789ABCDE":
        M = int(f"432{x}3", 15)
        N = int(f"86{x}86", 15)
        if (M + A) % N == 0:
            print(A)
            break

