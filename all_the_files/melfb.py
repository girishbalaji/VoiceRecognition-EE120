from math import floor, ceil, log1p
def melfb(p, n, fs):
    f0 = 700 / fs
    fn2 = floor(n/2)

    lr = log1p(0.5/f0)/ (p + 1)

    bl = [n * (f0 * (exp(i * lr) - 1)) for i in [0, 1, p, p + 1]]

    b1 = floor(bl[0]) + 1
    b2 = ceil(bl[1])
    b3 = floor(bl[2])
    b4 = min(fn2, ceil(bl[3])) - 1
    
    pf = [log1p(i/n/f0) /lr for i in range(b1,b4 + 1)]
    fp = [floor(i) for i in pf]
    pm = [pf[i] - fp[i] for i in range(len(pf))]

    r = fp[b2 -1:b4] + [fp[i] + 1 for i in range(b3)]
    c = [i+1 for i in range(b2,b4+1)] + [i + 1 for i in range(1,b3+1)]
    v = [2*(1-pm[i-1]) for i in range(b2,b4+1)] + [2*(pm[i]) for i in range(b3)]

    return [r,c,v]
