data = open("24_17756.txt").read().split()[0]

s = data.replace("*", "+")
res = s.split("++")

m = 0
for item in res:
    m = max(m, len(item))

print(m+2)
