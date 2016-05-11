'''
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Brute force- 142913828922
Time elapsed: 5.276795
Sieve of Eratosthenes- 142913828922
Time elapsed: 0.740057
'''

from math import sqrt
import time
from timeit import itertools


class problem10:
    limit = 2000000
    primeNumbers = [True] * limit
    
    def isPrime(self, n):
        if(n < 2): return False
        if(n == 2): return True
        if(n % 2 == 0): return False
        if(n < 9): return True
        if(n % 3 == 0): return False
        max_ = int(sqrt(n)) + 1
        for i in range(5, max_, 6):
            if(n % i == 0): return False
            if(n % (i + 2) == 0): return False
        return True 
    
    def brute_force(self):
        sum = 0
        for i in range(self.limit):
            if(self.isPrime(i)): sum += i
        return sum
        
    def sieve_of_eratosthenes(self):
        for i in range(2, self.limit):
            if(self.primeNumbers[i] == True):
                for j in range(i * i, self.limit, i):
                    self.primeNumbers[j] = False
        sum = 0
        for (i, val) in enumerate(self.primeNumbers):
            if(val == True):
                sum += i
        return sum - 1
    
if __name__ == "__main__":
    start_time = time.clock()
    p10 = problem10()
    sum = p10.brute_force()
    print "Brute force-", sum 
    end_time = time.clock()
    print "Time elapsed:", end_time - start_time
    start_time = time.clock()
    sum = p10.sieve_of_eratosthenes()
    print "Sieve of Eratosthenes-", sum
    end_time = time.clock()
    print "Time elapsed:", end_time - start_time