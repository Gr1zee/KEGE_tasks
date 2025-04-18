def f(x):
    res = []
    while x != 0:
        res = [x%3] + res
        x = x // 3
    return res

for N in range(10, 1000):
    Tr = f(N)
    if N % 3 == 0:
        Tr.insert(0, Tr[-2])
        Tr.insert(1, Tr[-1])
    else:
        Tr =  f(sum(Tr)) + Tr
    R = int("".join([str(x) for x in Tr]), 3)
    if R > 418 and R % 2 != 0:
        print(R)