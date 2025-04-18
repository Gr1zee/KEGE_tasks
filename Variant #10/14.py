def d(x):
    res = []
    while x != 0:
        res = [x % 3] + res
        x //= 3
    return res

for a in range(0, 100000):
    n = (3**10 + 3**7 + 3**3 + 2 + a)
    tr = d(n)
    col = [tr.count(x) for x in tr]
    if len(set(col)) == 1:
        print(a, tr,col)
        break