N, S = 1000, 600
N, S = 6, 500
data = [(int(x), True) for x in open("test.txt")]
data.sort(reverse=True)
c = 0

g = data[0][0]
r = 0
for i in range(1, len(data)):
    print(g, data[i][0])
    if g + data[i][0] < S and data[i][1] == True:
        g += data[i][0]
    else:
        for j in range(i+1, len(data)):
            if g + data[j][0] <= S and data[j][1] == True:
                g += data[j][0]
                data[j] = (data[j][0], False)
        lg = g
        g = data[i][0]
        c += 1
print(c, lg)
