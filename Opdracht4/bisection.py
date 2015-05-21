def findRoot(f,a,b,epsilon):
    fa = float(f(a))
    fb = float(f(b))
    m = (a+b)/2
    value_midpoint = f(m)
    if fa*fb>0:
        return str("Geen nulpunten")
    elif fa == 0:
        return a
    elif fb == b:
        return b
    elif abs(b-a) <= epsilon:
        return m
    elif fa * value_midpoint < 0:
        return findRoot(f,a,m,epsilon)    
    else: 
        return findRoot(f,m,b,epsilon)
    return m