def find_gcd(a, b):
    while(b > 0):
        a %= b
        if(a == 0): return b
        b %= a
    return a

lcm = 1
for i in range(2, 10):
    lcm = lcm * int(i / find_gcd(lcm, i))

print(lcm)
