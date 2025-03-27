data = [int(x) for x in open("17_17873.txt")]

mi = min(data)
print(mi)
c = 0
ma = 0

for i in range(len(data)-1):
    if data[i] % 16 == mi or data[i+1] % 16 == mi:
        c += 1
        ma = max(data[i] + data[i+1], ma)
print(c, ma)