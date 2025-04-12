def f(x, n_t1, n_t2, n_f):
    if x > 57:
        return 0
    elif x == 57 and n_t1 and n_t2 and (not n_f):
        return 1
    elif x == 13:
        n_t1 = True
    elif x == 15:
        n_t2 = True
    elif x == 35:
        n_f = True
    return f(x+1, n_t1, n_t2, n_f) + f(x+2, n_t1, n_t2, n_f) + f(x*2, n_t1, n_t2, n_f)

print(f(7, False, False, False))