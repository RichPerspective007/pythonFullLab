#A) Write a program to take a year as input and check If it is a leap year or not.

'''
Seriously?? Yeh bhi nhi aata? Chalo koi baat nahi dekh lo aur pass ho jao
'''

#taking user input:
while (1):
    try:
        year = int(input('Please enter any year to check whether it is a leap year or not: '))
        break
    except:
        print('Given input is not a valid year. Please try again.\n\n')
        continue


#testing year value against leap year conditions:

if not year%4:
    if not year%100:
        if not year%400:
            print(f'{year} is a centurion leap year.')
        else:
            print(f'{year} is not a leap year.')
    else:
        print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')



'''
Sample Output 1: 

Please enter any year to check whether it is a leap year or not: 20PY
Given input is not a valid year. Please try again.


Please enter any year to check whether it is a leap year or not: 2016
2016 is a leap year.


Sample Output 2:

Please enter any year to check whether it is a leap year or not: 2000
2000 is a centurion leap year.


Sample Output 3:

Please enter any year to check whether it is a leap year or not: 1900
1900 is not a leap year.


Sample Output 4:

Please enter any year to check whether it is a leap year or not: 2019
2019 is not a leap year.

'''