import time

T1 = time.perf_counter()

def primes(n):
    getallen = list(range ( 2, n+1 , 1))
    for deler in getallen:
        for x in getallen:
            if x%deler==0 and x!=deler:
                getallen.remove(x)
    print(getallen)
    T2 = time.perf_counter()
    number_of_primes= len(getallen)
    print('Found ' + str(number_of_primes) + ' Prime numbers smaller than ' + str(n) + ' in ' + str(T2-T1) + ' sec.')
    
primes(10000)




# print('Time required '+ str(T2-T1) +' sec.')