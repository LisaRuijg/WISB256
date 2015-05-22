import sys
import math

bestand = sys.argv[1]

C_2 = 0.6601618

prime_list = list(open(bestand))
pi_n = len(prime_list)
for i in range(pi_n):
    prime_list[i] = int(prime_list[i])

N = prime_list[-1]

A = N/math.log(N)

prime_number_theorem = pi_n/A

def pi2_n():
    count = 0
    for p in prime_list:
        if p+2 in prime_list:
                count = count + 1
    return count    

C = pi2_n()

D = (2*C_2*N)/math.log(N)**2
E = C/D

print("Largest Prime    = "+ str(N))
print("------------------------------------")
print("pi(N)            = "+ str(pi_n))
print("N/log(N)         = "+ str(A))
print("ratio            = "+ str(prime_number_theorem))
print("------------------------------------")
print("pi_2(N)          = "+ str(C))
print("2CN/log(N)^2     = "+ str(D))
print("ratio            = "+ str(E))