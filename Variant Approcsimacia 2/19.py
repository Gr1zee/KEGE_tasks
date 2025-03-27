def f(s1, s2, m):
    if s1 + s2 >= 81: return m%2==0
    if m == 0: return 0
    h = [f(s1+1, s2, m-1), f(s1*2, s2, m-1), f(s1, s2+1, m-1), f(s1, s2*2, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print([x for x in range(1, 74) if (not f(7, x, 2)) and f(7, x, 4)])