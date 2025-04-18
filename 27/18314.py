clustersA = [[], []]
clustersB = [[], [], []]

for l in open("27_A_18314.txt"):
    x, y = [float(x) for x in l.split()]
    if x < 23.5:
        clustersA[0].append([x, y])
    if x >= 23.5:
        clustersA[1].append([x, y])

for l in open("27_B_18314.txt"):
    x, y = [float(x) for x in l.split()]
    if x < 10.0:
        clustersB[0].append([x, y])
    if x > 18.0:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

def dist(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return abs(x2 - x1) + abs(y2 - y1)

def center(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p1, p) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centerA = [center(cl) for cl in clustersA]
centerB = [center(cl) for cl in clustersB]
pxA = sum(x for x, y in centerA) / 2 * 1000
pyA = sum(y for x, y in centerA) / 2 * 1000
pxB = sum(x for x, y in centerB) / 3 * 1000
pyB = sum(y for x, y in centerB) / 3 * 1000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))