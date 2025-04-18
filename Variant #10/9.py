data = open("9.txt").read().splitlines()

c = 0
for l in open("9.txt"):
    a = [int(x) for x in l.split()]
    u1 = all([99 <= x <= 10 for x in a])
    u2 = all([x % 5 != 0 for x in a])
    if u1 + u2 == 1:
        c += 1
        print(a, u1, u2)
print(c)