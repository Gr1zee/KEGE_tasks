print("z x w y")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (((y <= (not x)) and y) == w) and z
                if f:
                    print(z, x, w, y)
# x y z w
# 0 0 1 0
# 1 0 1 0
# 1 1 1 0