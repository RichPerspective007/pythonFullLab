#taking user input
userInputList = input('Enter list elements seperate by whitespace: ').split(' ')

move_to_back = []
alreadySeen = []

i = 0

#performing some magic here
while i < len(userInputList):
    if userInputList[i] in alreadySeen:
        move_to_back.append(userInputList.pop(i))
    else:
        alreadySeen.append(userInputList[i])
        i+=1

userInputList+=move_to_back

#displaying output using a print statement
print(userInputList)


'''
python B.py
Enter list elements seperate by whitespace: a a a b b c d d d
['a', 'b', 'c', 'd', 'a', 'a', 'b', 'd', 'd']

'''