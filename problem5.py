'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''



def division(k):
    t = list(range(1,21))
    for i in t:
        if k % i == 0:
            pass
        else:
            return False
    return k
        # elif k % i != 0:
        #     break


k = 200000000
while k < 250000000:
    evenly_divi = division(k)

    if evenly_divi != False:
        break

    else:
        print(k)

    k += 1

# def dividable(num):    # return 1 if a number can be divided by number 1~20. otherwise return 0
#     rslt = 0
#     for i in range(1,21):
#         k = num%i
#         rslt = rslt + k
#     if rslt == 0:
#         return 1
#     else:
#         return 0
#
# j= 19
# while 1:
#     j = j+1
#     if dividable(j) == 1:
#         print(j)
#         break
