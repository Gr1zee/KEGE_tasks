data = open("9.txt").read().splitlines()

c = 0
for line in data:
    n = [int(x) for x in line.split()]
    ma = max(n)
    r = [x for x in n if n.count(x) == 2]
    if ma < sum(n) - ma and len(r) == 2:
        print(n, r)
        c += 1
print(c)