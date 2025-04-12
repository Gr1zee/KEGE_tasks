clustersA = [[], []]
clustersB = [[], [], []]

for line in open("27/27A_18051.txt"):
    x, y = [float(x) for x in line.split()]
    if y > 6:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for line in open("27/27B_18051.txt"):
    x, y = [float(x) for x in line.split()]
    if x < 9 and y > 0.5:
        clustersB[0].append([x, y])
    elif y < -0.5 * x + 4.75:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])
