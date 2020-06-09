# remove and reverse a given string
strValue = input('enter string:')
print(strValue.replace(strValue[0:3],"")[::-1])

#addition of two numbers
num1 = input('enter first number for additon:')
num2 = input('enter second number for additon:')

try:
 fNum = int(num1)
 sNum = int(num2)
 print('sum is :' + str(fNum + sNum))
except ValueError:
 print('Please enter an integer')

#string replacements
inputString = input('enter a sentense:')
print(inputString.replace('python','pythons'))
