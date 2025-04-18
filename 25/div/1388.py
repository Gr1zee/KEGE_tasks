def div(x):
    res = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return sorted(res)

c = 0
for i in range(150000, 160000):
    s = sum(div(i))
    if s != 0 and s % 13 == 10:
        print(i, s)
        c +=1 
        if c == 7:
            break