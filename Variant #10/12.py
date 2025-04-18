c = 0
s = "4"*222
while "4444" in s or "222" in s:
    if "4444" in s:
        s = s.replace("4444", "2", 1)
        c += 1
    else:
        s = s.replace("222", "44", 1)
        c += 1
print(c)