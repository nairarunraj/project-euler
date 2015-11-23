from math import sqrt
def isPrime(n):
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

prime_count = 0
n = 2
while(prime_count < 10001):
    if(isPrime(n)):
        prime_count = prime_count + 1
    n = n + 1
    
print(n - 1)
