print("y z x w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= z) <= w) or (not y)
                if f == 0:
                    print(y, z, x, w)