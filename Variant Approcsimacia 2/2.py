print("y x z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(x <= y)) or ( z <= w) or (not z)
                if not f:
                    print(y, x, z, w)