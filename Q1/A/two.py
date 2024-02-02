'''

Question: A) Use string slicing to perform the following:
ii. Take 2 strings, s1, and s2 return a new string made of the first, middle and last
char of each input string.

'''

#taking user input
s1 = input('Please enter the first string: ')
s2 = input('Please enter the second string: ')

#making the new string by slicing the given strings
outputString = s1[0]+s1[len(s1)//2]+s1[len(s1)-1]+s2[0]+s2[len(s2)//2]+s2[len(s2)-1]

print('The required string is:',outputString, sep=' ')

'''

Example output 1: python two.py

Please enter the first string: python
Please enter the second string: assignment
The required string is: phnant

Example output 2: python two.py

Please enter the first string: practise
Please enter the second string: repository
The required string is: pteriy


'''