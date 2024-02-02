'''
11.	A) Write a python program to find out the palindromic prime numbers between a range

'''
import sys

def is_prime(num):
    #implement logic for checking prime number
    return True

def is_palidrome(string):
    #implement logic for checking palindrome number
    return True

#taking user-input for lower and upper limits of the range
print('This program will find palindromic prime numbers in a given range consisting of a lower limit and an upper limit, both positive integers.')
lower_limit = int(input('Please enter lower limit of the range: '))
upper_limit = int(input('Please enter upper limit of the range: '))

if lower_limit>=upper_limit or lower_limit<0 or upper_limit<0:
    print('Invalid inputs. Please try again.')
    sys.exit(0)

print(f'The palidromic prime numbers between {lower_limit} and {upper_limit} are: ')
f=0
for i in range(lower_limit,upper_limit+1,1):
    if is_prime(i) and is_palidrome(str(i)):
        print(i)
        f=1

if f:
    pass
else:
    print('NONE. There are no such numbers satisfying the required conditions in the given range.')

