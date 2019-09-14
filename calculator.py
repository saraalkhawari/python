'''
OUTPUT..

Enter the first number: 4.0
Enter the second number: 6.0
Choose the operation (+, -, /, *): /
The answer is 0.666666666667

 '''

num1 = input ('\n\nEnter the first number:  ')

num2 = input ('\nEnter the second number : ')

oprtn = raw_input ('\nChoose the operation (+,-,/,*):  ')


if oprtn == '+':
	print ('\nThe answer is '+ str(num1+num2) + '\n')
elif oprtn == '-':
	print ('\nThe answer is '+ str(num1-num2) + '\n')
elif oprtn == '/':
	print ('\nThe answer is '+ str(float(num1/num2)) + '\n')
elif oprtn == '*':
	print ('\nThe answer is '+ str(num1*num2) + '\n')
else:
	print ('\n----- Opertation Invalid ! -----\n')