'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import timeit

def primeTest(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(primeTest(20))

t = 10
prime_list = []
for i in range(2,t):
    if primeTest(i):
        if t % i == 0:
            prime_list.append(i)
    else:
        pass


print(prime_list)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        print('first ',i,n)
        if n % i:
            print('second ', i,n)
            i += 1
        else:
            print('third ',i,n)
            n /= i
            print('forth ',i,n)
            factors.append(i)
    if n > 1:
        print('fifth ', i,n)
        factors.append(n)
    return factors

print (prime_factors(600851475143))
