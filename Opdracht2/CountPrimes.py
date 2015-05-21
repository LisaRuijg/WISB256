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

#pi2_n = 

print("Largest Prime = "+str(N))
print("pi(N) = "+str(pi_n))
print("N/log(N) = "+ str(A))
print("ratio = "+ str(prime_number_theorem))
#print("pi_2(N) = "+str(pi2_n))
