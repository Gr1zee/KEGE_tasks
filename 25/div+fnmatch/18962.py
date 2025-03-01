from fnmatch import fnmatch

d = 0

def div(n):
    r = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            r.append(i)
            r.append(n//i)
    return sorted(r)

for i in range(500_000, 10**6):
    divs = [i for i in div(i) if fnmatch(str(i), "2*3?")]
    if len(divs) > 0:
        print(i, divs[0])
        d += 1
        if d == 5:
            break
