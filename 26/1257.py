N = 5000
data = [int(x) for x in open("26_1257.txt")]
s = set(data)
c = 0
ma = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if (data[i] + data[j]) % 2 != 0 and (data[i] + data[j]) in s:
            c += 1
            ma = max(ma, data[i] + data[j])
print(c, ma)