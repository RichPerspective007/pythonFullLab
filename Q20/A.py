#taking user-input binary string
binString = input('Enter a binary string. We will check and tell if it is binary number or not: ')
binString = binString.strip()

if binString.count('0')+binString.count('1')+binString.count('.') == len(binString):
    print("Given string IS a binary number.")
else:
    print("Given string IS NOT a binary number.")