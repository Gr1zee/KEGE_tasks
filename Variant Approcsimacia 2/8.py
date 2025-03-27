from itertools import product
c = 0
for item in product("012345678", repeat=5):
    s = "".join(item)
    s2 = s.replace("1", "*").replace("3", "*").replace("5", "*").replace("7", "*")
    if s[0] != "0" and s.count("0") == 1 and (not "*0" in s2) and (not "0*" in s2):
        print(s)
        c += 1
print(c)