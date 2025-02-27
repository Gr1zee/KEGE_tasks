N = 10000
data = [int(x) for x in open("26_2652.txt")]


res = [(x, data.count(x)) for x in data]
res.sort(key=lambda x: x[1], reverse=True)
print(res, len(set(data)))

