def div(x):
    res = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return sorted(res)


for i in range(81234, 134169+1):
    if len(div(i)) == 3:
        print(div(i)[0], div(i)[1], div(i)[2])