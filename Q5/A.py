'''
Write a python program to find all occurrences of “India” in given string ignoring the case

'''

#taking string user input
userInput = input('Enter any string:  ')

#converting userInput to lowerCase
lowerCaseUserInput = userInput.lower()

#flag variable to check if any matching conditions found or not
f=0

#checking occurence of 'India'
for i in range(len(lowerCaseUserInput)):
    if lowerCaseUserInput[i:i+5] == 'india':
        print(userInput[i:i+5])
        f=1

if f:
    pass
else:
    print('\nNo occurences of the string \'India\' in the given string.')