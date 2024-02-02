'''

B) Print the following pattern using Python program 
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1

0
1 0
2 1 0
3 2 1 0


'''

#taking user input for number of lines
n = int(input('Enter number of lines of the pattern. It must be an integer: '))

print('\nRequired pattern is:\n')
for i in range(n):
    for j in range(i,-1,-1):
        print(2**j,end=' ')
    print()