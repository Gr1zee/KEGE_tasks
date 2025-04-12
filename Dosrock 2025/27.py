clustersA = [[], []]
clustersB = [[], [], []]

for l in open("27_A_21425.txt"):
    x, y = [float(x) for x in l.split()]
    if y < 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for l in open("27_B_21425.txt"):
    x, y = [float(x) for x in l.split()]
    if x < 0:
        clustersB[0].append([x, y])
    else:
        if y > 0:
            clustersB[1].append([x, y])
        if y < 0:
            clustersB[2].append([x, y])

def d(A, B):
    return ((B[1] - A[1])**2 + (B[0] - A[0])**2)**0.5

def center(cluster):
    m = []
    for p in cluster:
        sm = sum(d(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxA = sum(x for x, y in centersA) / 2 * 10000
pyA = sum(y for x, y in centersA) / 2 * 10000
pxB = sum(x for x, y in centersB) / 3 * 10000
pyB = sum(y for x, y in centersB) / 3 * 10000

print(pxA, pyA)
print(pxB, pyB)