'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import time
#Time at the start of exection
start_time = time.time()

def pythagorean_triplet():
 for a in range(1,999):
  for b in range(1,999):
   c = 1000-a-b
   if (a**2+b**2) == c**2:
    print(a,b,c)
    return a*b*c

print(pythagorean_triplet())

#time at the end of execution
end_time = time.time()

#Printing the total_time
print(end_time - start_time)
