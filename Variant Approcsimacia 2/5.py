for N in range(1, 100):
    B = bin(N)[2:]
    B = list(B)
    if B.count("1") % 2 == 0:
        B.append("0")
        B[0] = "1"
        B[1] = "0"
    else:
        B.append("1")
        B[0] = "1"
        B[1] = "1"
    if int("".join(B), 2) > 19:
        print(N, int("".join(B), 2))
        break