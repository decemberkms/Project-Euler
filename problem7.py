'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def primeTest(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(primeTest(20))

t = 2
n = 0
while n != 10001:
    if primeTest(t) == True:
        print('###prime', t)
        t += 1
        print('count', n)
        n += 1
    else:
        print('count', n)
        n
        t += 1


print('prime', t -1 , 'count', n)
104724
104730
