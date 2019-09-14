'''
OUTPUT : 
============================
| Enter year of birth: 2000 |
| Enter month of birth: 6   |
| Enter day of birth: 6     |
| You are 18 years old.     |
============================
'''
import datetime
from datetime import date

today = date.today()

def check_birthday (y, m , d): 
	if y>today.year:
		print ('\n\n---- Invalid Birthdate ! ----\n\n')
	else:
		calculate_age(y,m,d)

def calculate_age (y,m,d):
	print ('\n\nToday :' + str(date.today()))
	print('\nYou are ' + str(today.year - y) +' years old !\n\n')

y = input('\n\nEnter year of birth: ')
m = input ('\nEnter month of birth:')
d = input('\nEnter day of birth: ')

check_birthday(y,m,d)


















