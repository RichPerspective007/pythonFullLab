'''
Question: A) Use string slicing to perform the following:
i. Take a string of length greater than 2, return a string except 1 st and last
characters.
'''
import sys
#taking input string from user
inputString = input('Please enter a string of length greater than 2: ')

#checking for string length constraints
if len(inputString)<=2:
    print("String length less than or equal to 2. Please enter a longer string.\n")
    sys.exit(0)

#performing string slicing to get the required output
print('Required output after string slicing is:', inputString[1:len(inputString)-1], sep=' ')

'''
Example output:

python one.py
Please enter a string of length greater than 2: assignment
Required output after string slicing is: ssignmen

'''