def f(s, m):
    if s <= 87: return m%2==0
    if m == 0: return 0
    h = [f(s-2, m-1), f(s//2, m-1)]
    return any(h) if (m-1)%2 ==0 else all(h)

print([x for x in range(88, 200) if (not f(x, 2)) and (f(x, 4) or f(x, 2))])