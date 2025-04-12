for N in range(1000):
    B = bin(N)[2:]
    if B.count("1") % 2 == 0:
        B = B + "0"
        B = list(B)
        B[0] = "1"
        B[1] = "0"
    else:
        B = B + "1"
        B = list(B)
        B[0] = "1"
        B[1] = "1"
    R = int("".join(B), 2)
    if R > 480:
        print(N)
        break