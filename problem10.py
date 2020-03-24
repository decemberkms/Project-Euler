'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def primeTest(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(primeTest(20))

n = 20000
t = 0
for i in range(2,n):
    if primeTest(i):
        t += i

print(t)
