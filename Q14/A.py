'''

14.	A) Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Input : green-red-yellow-black-white Output : black-green-red-white-yellow


'''

words = input('Please enter a hyphen-separated sequence of words: ').split('-')
for i in range(len(words)):
    for j in range(i+1,len(words),1):
        curr_word = words[i]
        comp = words[j]
        if curr_word>comp:
            words[j]=curr_word
            words[i]=comp

for i in range(len(words)):
    if i==len(words)-1:
        print(words[i])
    else:
        print(f'{words[i]}-',end='')
