S, N = 100000, 1000
data = list(map(int, open("26_813.txt").read().splitlines()))
data.sort(reverse=True)
s = 0
c = 0
l = 0
for i in range(len(data)):
    if s % 2 == 0:
        s += data[i]
        l = data[i]
    else:
        s += data[len(data)-i]
        l = data[len(data)-i]
    c += 1
    if s > S:
        break
print(c, l)