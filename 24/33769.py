s = open("24(4).txt").readline()

m = [""]*len(s)

for i in range(1, len(s)-1):
    if s[i-1] == s[i]:
        m[i+1] = s[i+1]

d = [x for x in m if x != ""]
r = {}
for i in range(len(d)):
    if d[i] in r:
        r[d[i]] += 1
    else:
        r[d[i]] = 0
print(sorted(r))