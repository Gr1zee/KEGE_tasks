data = [int(x) for x in open("Variant #7 (Shastin, Bahtiev)/17/17_18957.txt")]
print(data)

ma = max(data)//2
mr = 0
c = 0

for i in range(len(data)-2):
    tr = (data[i], data[i+1], data[i+2])
    s_tr = list(map(str, tr))
    if ((not "0" in s_tr[0]) and (not "0" in s_tr[1])) or ((not "0" in s_tr[1]) and (not "0" in s_tr[2])) or ((not "0" in s_tr[0]) and (not "0" in s_tr[2])) or ((not "0" in s_tr[0]) and (not "0" in s_tr[1]) and (not "0" in s_tr[2])):
        if sum(tr) < ma:
            c += 1
            mr = max(mr, sum(tr))

print(c, mr)



