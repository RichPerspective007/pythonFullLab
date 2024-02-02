'''

Question: A) Use string slicing to perform the following:
iii. Write a python program to take 2 strings, s1 and s2, create a new string by
appending s2 in the middle of s1.

'''

#taking user input
s1 = input('Please enter the first string: ')
s2 = input('Please enter the second string: ')

#making the new string by slicing the given strings
outputString = s1[:len(s1)//2] + s2 + s1[len(s1)//2:]

print('The required string is:',outputString, sep=' ')

'''
Example output 1: python three.py

Please enter the first string: python
Please enter the second string: assignment
The required string is: pytassignmenthon

Example output 2: python three.py

Please enter the first string: practical
Please enter the second string: exams
The required string is: pracexamstical

'''