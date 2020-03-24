'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

three_digit_n = list(range(900,1000))

number_list = []
for i in range(100, 1000):
    for j in range(100,1000):
        number_list.append(str(i*j))

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)

    if s == rev:
        return True
    return False

list_p = []
for i in number_list[::-1]:
    if isPalindrome(i):
        list_p.append(int(i))

print(max(list_p))
