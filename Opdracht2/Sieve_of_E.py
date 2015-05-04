import time
import sys
n= int(sys.argv[1])
bestandsnaam = sys.argv[2]

T1 = time.perf_counter()

def primes(n):
    getallen = list(range ( 0, n))
    getallen[1]=0
    for i in range(1,n):
        if getallen[i]!=0:
            for j in range(2*i,n,i):
                getallen[j]=0
    return getallen
    
T2 = time.perf_counter()

document = open ( bestandsnaam , 'w')
for x in primes(n):
    if x!=0:
        document.write(str(x) +'\n')
document.close()
    
number_of_primes= sum( 1 for line in open(bestandsnaam))

print('Found ' + str(number_of_primes) + ' Prime numbers smaller than ' + str(n) + ' in ' + str(T2-T1) + ' sec.')