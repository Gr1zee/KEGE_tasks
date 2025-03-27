def div(x):
    res = []
    while x > 0:
        res = [str(x%3)] + res
        x //= 3
    return res[::-1]

for x in range(1, 2031):
    f = 3**100 - x
    r = "".join(div(f))
    if r.count("0") == 1:
        print(x)