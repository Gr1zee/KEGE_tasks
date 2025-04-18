from itertools import product

c2 = 0
c1 = 0
l = 1
f = False
for item in product("АЕИКМСЧ", repeat=5):
    s = "".join(item)
    print(l, s)
    if s == "МАСИК":
        c1 = l
    if s == "ЧЕЧИК":
        c2 = l
        break
    l += 1
print(c2 - c1 - 1)