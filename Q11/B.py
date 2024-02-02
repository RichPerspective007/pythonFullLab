'''

B) Write programs using nested loops to produce the following patterns:
A
A B
A B C
A B C D
A B C D E
A B C D E F


'''

#taking user-input for number of lines in the pattern
n = int(input('Please enter number of lines in the pattern.'))
print('\nRequired pattern is: \n')

for i in range(65,65+n):
    for j in range(65,i+1,1):
        print(chr(j),end=' ')
    print()