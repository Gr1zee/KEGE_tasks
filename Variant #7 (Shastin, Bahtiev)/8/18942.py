from itertools import product

c = 0
for item in product("ДИОНСЙ", repeat=6):
    s = "".join(item)
    s2 = s.replace("ИИ", "**").replace("ДД", "**").replace("СС", "**").replace("ОО", "**").replace("ЙЙ", "**").replace("НН", "**")
    if ((s.count("Д") != 0 and s.count("И") == 0) or (s.count("Д") == 0 and s.count("И") != 0)) and (s2.count("**") < 1):
        print(s, s2)
        c += 1
print(c)
