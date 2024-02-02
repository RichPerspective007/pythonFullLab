'''
12.	A) Write a python program to find the Twins primes between a range( Twin primes are pairs of prime numbers that have just one number between them: 5 and 7, 11 and 13,and 29 and 31)

'''

import sys

def is_prime(num):
    #implement logic for checking prime number
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    
    return True

#taking user-input for lower and upper limits of the range
print('This program will find palindromic prime numbers in a given range consisting of a lower limit and an upper limit, both positive integers.')
lower_limit = int(input('Please enter lower limit of the range: '))
upper_limit = int(input('Please enter upper limit of the range: '))

if lower_limit>=upper_limit or lower_limit<0 or upper_limit<0:
    print('Invalid inputs. Please try again.')
    sys.exit(0)

if lower_limit==0:
    lower_limit=2

print(f'The twin prime numbers between {lower_limit} and {upper_limit} are: ')
f=0
for i in range(lower_limit,upper_limit-1,1):
    if is_prime(i) and is_prime(i+2):
        print(i,' and ',i+2)
        f=1

if f:
    pass
else:
    print('NONE. There are no such numbers satisfying the required conditions in the given range.')