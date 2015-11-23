def isPalin(number_str):
    return number_str[::-1] == number_str

maxim = 0
for i in range(999, 100, -1):
    # print(i)
    for j in range(999, 100, -1):
        prod = i * j
        if(maxim < prod and isPalin(str(prod))):
            maxim = prod
            
print(maxim)
