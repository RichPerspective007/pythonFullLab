'''
19.	A) Write a Python Program to print the Prime Factors of an Integer

'''
import sys


def is_prime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    
    return True


#taking using input integer.
num = int(input('Enter any positive integer greater than 1 to get its prime factors: '))


if num<=1:
    print('Invalid input. Program execution terminated.\n')
    sys.exit(0)


print(f'Prime factors of {num} are: ')
dup = num
for i in range(2,num//2+1,1):
    if is_prime(i):
        while(num%i == 0):
            num = num // i
            print(i,end=', ')
    if num == 1:
        break

if num == dup:
    print(dup)