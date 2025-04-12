def div(x):
    res = set()
    for i in range(2, int((x**0.5))):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return sorted(res)
c = 0
for i in range(1_125_000, 10_000_000):
    d = div(i)
    f = []
    for elem in d:
        if elem % 10 == 7 and elem != 7:
            f.append(elem)
            break
    if f:
        c += 1
        print(i, f[0], d)
        if c == 5:
            break