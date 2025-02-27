N = 9937
data = [list(map(int, x.split())) for x in open("test.txt")]

data.sort()
start = 0
end = 0
count = 0
for i in range(len(data)):
    if data[i][0] < end:
        if data[i][1] > end:
            end = data[i][1]
    else:
        start = data[i][0]
        end = data[i][1]
        count += 1
    print(start, end)

print(count)
