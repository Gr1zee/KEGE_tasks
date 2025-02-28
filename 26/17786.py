N, V = 1000, 835000
data = [int(x) for x in open("26_17786.txt") if 8000 <= int(x) <= 12000]
data.sort(reverse=True)
print(data)
c = 0
s = 0
for i in range(len(data)):
    if s + data[i] <= V:
        s += data[i]
        l = data[i]
        c += 1

print(c, l)