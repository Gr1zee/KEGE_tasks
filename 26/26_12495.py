N, R, V = 10000, 1021000, 11111
c = 0
data = [int(x) for x in open("26.txt")]
data.sort()
r = data[0]
for i in range(len(data)-2):
    r += (data[i+1] - data[i])
    if V - r <= 0:
        c += 1
        r = 0
print(c)