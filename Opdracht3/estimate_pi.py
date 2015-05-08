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
        count_2 = 0 
        for i in range(1,N+1):
            if drop_needle(L)==True:
                count_2 = count_2 + 1
        print(str(count_2) + ' hits in '+ str(N) + ' tries')
        P = (count_2)/N
        estimate_pi_2 = (2*(-math.sqrt(L*L-1) + L - math.asin(1/L)))/(P-1)
        print('Pi = '+ str(estimate_pi_2))
        return
   
    else: 
        count = 0    
        for i in range(1,N+1):
            if drop_needle(L)==True:
                count = count +1
        print(str(count) + ' hits in '+ str(N) + ' tries')
        P = (count)/N
        estimate_pi = (2*L)/(P)
        print('Pi = '+ str(estimate_pi))
        return

hits()