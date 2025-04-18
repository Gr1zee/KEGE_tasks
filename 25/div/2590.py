def div(x):
    res = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return sorted(res)

for i in range(6080068, 6080176):
    if len(div(i)) == 0:
        print(i)