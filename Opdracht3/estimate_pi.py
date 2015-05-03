import random
import sys
import math

N = 2
L = 0.5
#N = int(sys.argv[1])    
#L = int(sys.argv[2])

x_0 = random.random()
y_0 = random.random()
a = random.vonmisesvariate(0,0)

x_1 = x_0 + L*math.cos(a)
y_1 = y_0 + L*math.sin(a)

def drop_needle(L):
    for i in range(int(N)):
        N==i


h = 3
print(' hits '+' in '+' tries.')
estimate_pi = (2*L*N)/(h)
print('Pi = '+ str(estimate_pi))