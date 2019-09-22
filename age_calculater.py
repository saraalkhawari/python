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

	if m>today.month :
		print ('\nYou are %s Years old \n\n' % ((today.year-1)-y))
	else: 
		print ('\nYou are %s Years old \n\n' % (today.year-y))

y = int(input('\n\nEnter year of birth: '))
m = int(input ('\nEnter month of birth:'))
d = int(input('\nEnter day of birth: '))

check_birthday(y,m,d)

'''TO CALCULATE THE EXACT AGE BY YEARS , MONTH , AND DAYS !! BUT THE CALCULATIONS ARE WRONG :)======>
import datetime
from datetime import date

today = date.today()


#month_days  = [31 , 28 , 31 ,30 , 31 , 30 , 31 , 31 , 30 , 31 , 30]

def check_birthday (y, m , d): 
	if y>today.year:
		print ('\n\n---- Invalid Birthdate ! ----\n\n')
	else:
		calculate_age(y,m,d)

def calculate_age (y,m,d):
	print ('\n\nToday :' + str(date.today()))

	if m>today.month & d<today.day:
		print('\nYou are %s years  %s months %s Days old !\n\n'%(((today.year-1)-y),((12+today.month)-m),(today.day-d)))
	elif m<today.month & d>today.day:
		print('\nYou are %s years  %s months %s Days old !\n\n'%((today.year-y),((today.month-1)-m),((month_days[today.day]+today.day)-d)))
	elif m>today.month & d>today.day:
		print('\nYou are %s years  %s months %s Days old !\n\n'%(((today.year-1)-y),((12+today.month-1)-m),((month_days[today.day]+today.day)-d)))
	else:
		print('\nYou are %s years  %s months %s Days old !\n\n' % ((today.year-y),(today.month - m),(today.day-d)))

y = int(input('\n\nEnter year of birth: '))
m = int(input ('\nEnter month of birth:'))
d = int(input('\nEnter day of birth: '))

check_birthday(y,m,d)

'''



















