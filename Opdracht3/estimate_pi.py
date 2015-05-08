import random
import sys
import math

if len(sys.argv)==4:
    seed = int(sys.argv[3])
    random.seed(seed)

def drop_needle(L):
    x_0 = random.random()   #uniform in [0,1]
    # y_0 = random.random()
    a = random.vonmisesvariate(0,0)     #uniform in [0, 2*pi]
    x_1 = x_0 + L*math.cos(a)
    # y_1 = y_0 + L*math.sin(a)
    if x_1 >= 1:
        return True
    elif x_1 <= 0:
        return True
    else:
        return False

def hits():
    if len(sys.argv)<3:
        print('Use: estimate_pi.py N L')
        return
    
    N = int(sys.argv[1])    
    L = float(sys.argv[2])
    
    if L >1:
        print('AssertionError: L should be smaller than 1')
        return
    
    count = 0    
    for i in range(1,N+1):
        if drop_needle(L)==True:
            count = count +1
    print(str(count) + ' hits in '+ str(N) + ' tries')
    estimate_pi = (2*L*N)/(count)
    print('Pi = '+ str(estimate_pi))
    return

hits()