'''
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time
from math import sqrt

class problem9:
    sum = 1000
    
    def brute_force(self):
        for a in range(1, self.sum / 2):
            for b in range(a, self.sum / 2):
                c = self.sum - a - b
                if(a ** 2 + b ** 2 == c ** 2):
                    return a * b * c
        
    def gcd(self, num1, num2):
        if(num2 > num1):
            temp = num1
            num1 = num2
            num2 = temp
            
        while(num1 % num2 != 0):
            temp = num1
            num1 = num2
            num2 = temp % num1
        
        return num2
                       
    '''
    a = d(m^2 - n^2)
    b = 2dmn
    c = d(m^2 + n^2)
    a+b+c=s=1000
    2dm^2+2mnd=s
    m(m+n)=s/2d
    '''  
    def number_theory_approach(self):
        mlimit = int(sqrt(self.sum / 2))  # m < sqrt(sum/2)
        for m in range(2, mlimit + 1):
            if((self.sum / 2) % m == 0):
                if(m % 2 == 0):
                    k = m + 1
                else:
                    k = m + 2
                while(k < 2 * m and k <= self.sum / (2 * m)):
                    if(self.sum / (2 * m) % k == 0 and self.gcd(k, m) == 1):
                        d = self.sum / 2 / (k * m)
                        n = k - m
                        a = d * (m * m - n * n)
                        b = 2 * d * n * m
                        c = d * (m * m + n * n)
                        return a * b * c
                    k += 2
    
if __name__ == "__main__":
    start_time = time.clock()
    p9 = problem9()
    product = p9.number_theory_approach()
    print(product)               
    end_time = time.clock()
    print "Time elapsed: ", end_time - start_time
    
    start_time = time.clock()
    p9 = problem9()
    product = p9.brute_force()
    print(product)               
    end_time = time.clock()
    print "Time elapsed: ", end_time - start_time