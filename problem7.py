'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# def primeTest(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
#
# print(primeTest(20))
#
# t = 2
# n = 0
# while n != 10001:
#     if primeTest(t) == True:
#         print('###prime', t)
#         t += 1
#         print('count', n)
#         n += 1
#     else:
#         print('count', n)
#         t += 1
#
#
# print('prime', t -1 , 'count', n)

import time

def erato(n):
    prime_n = []
    prime_bool = [True for i in range(n+1)]
    p = 2
    while p*p <=n:
        if(prime_bool[p]==True):
            for i in range(p*p,n+1,p):
                prime_bool[i]=False
        p += 1
    for p in range(2,n):
       if prime_bool[p]:
           prime_n.append(p)

    return(prime_n)

tic = time.time()
p = erato(1000000)
# print(p)
# print(len(p))
print(p[10000])
print("Time taken = {}ms".format(1000*(time.time()-tic)))
