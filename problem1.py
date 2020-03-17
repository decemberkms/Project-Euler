'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
nums = list(range(0,1000))

list_3 = []
list_5 = []

for i in nums:
    if i % 3 == 0:
        list_3.append(i)
    elif i % 5 == 0:
        list_5.append(i)
print(list_3)
print(list_5)
print(sum(list_3) + sum(list_5))


'''
l = []
for i in range(3,1000):
	if(i%3==0 or i%5==0):
		l.append(i)
'''
