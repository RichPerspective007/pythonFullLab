
'''
B) Write a program that reads a file line by line. Each line read from the file1 is copied to
another file with line number specified at the beginning of the line.
'''

f1 = open('../python_file_handling.txt','r')

f2 = open('duplicate.txt','a')

line = f1.readline()

i=0
while(line):
    f2.write(f'{i} '+line)
    line = f1.readline()
    i+=1

f1.close()
f2.close()
