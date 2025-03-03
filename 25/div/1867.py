def div(x):
    res = set()
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return sorted(res)

def rule(x):
    return str(x)[-1] == "8"

c = 0   
for i in range(500000, 1000000):
    d = div(i)
    if len(d) > 0:
        for elem in d:
            if rule(elem) and elem != 8:
                print(i, elem)
                c += 1
                break
        if c == 5:
            break
