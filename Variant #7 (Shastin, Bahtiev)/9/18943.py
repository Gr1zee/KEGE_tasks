data = open("9.txt")

c = 0
for line in data:
    s = list(map(int, line.split()))
    tr = [x for x in s if s.count(x) == 3]
    dv = [x for x in s if s.count(x) == 2]
    one = [x for x in s if s.count(x) == 1]
    if (len(tr) == 3 and len(dv) == 2 and len(one) == 2) and tr[0] + dv[0] >= sum(one):
        print(tr, dv, one)
        c += 1
print(c)
