clustersA = [[], []]
clustersB = [[], [], [], [], []]

for line in open("27_A_17916.txt"):
    x, y = [float(x) for x in line.split()]
    if y < 8:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for line in open("27_B_17916.txt"):
    x, y = [float(x) for x in line.split()]
    if y < 2:
        clustersB[0].append([x, y])
    elif y < 4:
        clustersB[1].append([x, y])
    elif y < 10:
        clustersB[2].append([x, y])
    elif y < 14:
        clustersB[3].append([x, y])
    else:
        clustersB[4].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2- x1)**2 + (y2 - y1)**2)**0.5

def center(cluster):
    m = []
    for p in cluster:
        sm = sum(d(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centerA = [center(cl) for cl in clustersA]
centerB = [center(cl) for cl in clustersB]
pxA = sum(x for x, y in centerA) / 2 * 10000
pyA = sum(y for x, y in centerA) / 2 * 10000
pxB = sum(x for x, y in centerB) / 5 * 10000
pyB = sum(y for x, y in centerB) / 5 * 10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))