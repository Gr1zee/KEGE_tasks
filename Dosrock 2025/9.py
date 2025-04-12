data = open("9.txt").read().splitlines()

c = 0
for line in data:
    line = [int(x) for x in line.split()]
    pov3 = [x for x in line if line.count(x) == 3]
    if len(pov3) == 6:
        print("A")
        if max(pov3):
            c += 1
            print(line)
print(c)