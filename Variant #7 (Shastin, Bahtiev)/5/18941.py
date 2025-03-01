for N in range(1000, 10000):
    s = list(map(int, str(N)))
    r = []
    r.append(s[0]*s[1])
    r.append(s[0]*s[2])
    r.append(s[0]*s[3])
    r.sort()
    if "".join(map(str, r[1:])) == "5472":
        print(N)
