def div(x):
    res = set()
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return sorted(res)

c = 0
for i in range(250200, 1000000000):
    d = div(i)
    if len(d) > 0:
        if (d[0] + d[-1]) % 123 == 17:
            c += 1
            print(i, d[0] + d[-1])
            if c == 5:
                break
