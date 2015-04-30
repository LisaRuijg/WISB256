import time
import sys
n= int(sys.argv[1])
bestandsnaam = sys.argv[2]

T1 = time.perf_counter()

def primes(n):
    getallen = list(range ( 2, n+1 , 1))
    for deler in getallen:
        for x in getallen:
            if x%deler==0 and x!=deler and deler <= int(round(n**0.5)) :   # all delers less or equal than the square root of n don't have to be considered
                getallen.remove(x)
    return getallen
    
T2 = time.perf_counter()

document = open ( bestandsnaam , 'w')
for x in primes(n):
    document.write(str(x) +' \n')
document.close()
    
number_of_primes= len(primes(n))

print('Found ' + str(number_of_primes) + ' Prime numbers smaller than ' + str(n) + ' in ' + str(T2-T1) + ' sec.')