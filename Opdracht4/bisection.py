def findRoot(f,a,b,epsilon):
    m = (a+b)/2
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    elif f(m) == 0:
        return m
    elif abs(b-a) <= epsilon:
        return m
    elif f(a) * f(m) < 0:
        return findRoot(f,a,m,epsilon)    
    elif f(m) * f(b) < 0: 
        return findRoot(f,m,b,epsilon)
    
def findAllRoots(f,a,b,epsilon):
    roots=[]
    n = 100000
    l = (b-a)/n
    for i in range(n):
        if f(a+i*l)*f(a+(i+1)*l)<0:
            x = findRoot(f, a+i*l, a+(i+1)*l, epsilon)
            roots.append(x)
    return list(set(roots))    