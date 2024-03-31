class Prime:

    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    
    def findPrime(n):
        sieve = [True] * n

        m = int(n ** 0.5)
        for i in range(2,m+1):
            if sieve[i] == True:
                for j in range(i+i,n,i):
                    sieve[j] = False
        return [i for i in range(2,n) if sieve[i] == True]