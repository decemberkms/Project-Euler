'''
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


tt = []
for i in range(1,101):
    tt.append(i*i)

t_sum = sum(range(1,101))
t_sum_t = t_sum**2
ttt = sum(tt)
a = t_sum_t - ttt
print(a)

# n2=0
# sum2=0
# for i in range(1,101):
#     n2+=i**2
#     sum2+=i
#
# print(sum2**2-n2)
