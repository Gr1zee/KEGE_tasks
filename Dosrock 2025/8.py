from itertools import product

c = 0
for item in product("ДГИАШЭ", repeat=5):
    s = "".join(item)
    if s[0] not in "ИАЭ" and s[-1] not in "ДГШ":
        c += 1
        print(s)
print(c)