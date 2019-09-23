'''
OUTPUT
========================================================================
|-----Age Calculator-----                                               |
|                                                                       |
|                                                                       |
|Enter year of birth: 1995                                              |
|                                                                       |
|Enter month of birth:6                                                 |
|                                                                       |
|Enter day of birth: 3                                                  |
|                                                                       |
|-------------------------                                              |
|                                                                       |
|                                                                       |
|Today : 2019 / 9 / 23                                                  |
|                                                                       |
|You Are Exactly [ 24 ] Years  , [ 3 ]  Months  and   [ 20 ]  Days Old !|
|                                                                       |
|-------------------------                                              |
========================================================================
'''

import datetime
from datetime import date

today = date.today()
TM = today.month
month_days  = [31 , 28 , 31 ,30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]

def check_birthday (y, m , d): 
	if y>today.year or m>12 or d>31:
		print ('\n\n---- Invalid Birthdate ! ----\n\n')

	elif m>today.month and d<today.day:   #Birth Month > Today's Month 
		calculat_age_BM(y,m,d)

	elif m<today.month and d>today.day:   #Birth Day > Today's Day
		calculat_age_BD(y,m,d)

	elif m>today.month and d>today.day:   #Birth Month > Today's Month  && Birth Day > Today's Day 
		calculat_age_BM_BD(y,m,d)

	else:
		calculate_age(y,m,d)

#Calculates Age if Birth Month > Today's Month only
def calculat_age_BM(y,m,d): 

	age_year = (today.year-1) - y

	age_month = (today.month+12) - m

	age_day = today.day - d

	print ("\nYou Are Exactly %s Years  , %s Months  and   %s Days Old !" %(age_year,age_month,age_day))

#Calculates Age if Birth Day > Today's Day
def calculat_age_BD(y,m,d):

	age_year = today.year - y

	age_month = (today.month-1) - m

	if TM==12:
		age_day = (month_days[0]+today.day) - d

	else:
		age_day = (month_days[TM-1]+today.day) - d

	print ("\nYou Are Exactly %s Years  , %s Months  and   %s Days Old !" %(age_year,age_month,age_day))

#Calculates Age if Birth Month > Today's Month  && Birth Day > Today's Day 
def calculat_age_BM_BD(y,m,d):
	
	age_year = (today.year-1) - y

	age_month = (12+today.month-1) - m

	if TM==12:
		age_day = (month_days[0]+today.day) - d

	else:
		age_day = (month_days[TM+1]+today.day) - d

	print ("\nYou Are Exactly %s Years  , %s Months  and   %s Days Old !" %(age_year,age_month,age_day))

def calculate_age(y,m,d):
	
	age_year = today.year - y

	age_month = today.month - m

	age_day = today.day -d

	print ("\nYou Are Exactly [ %s ] Years  , [ %s ]  Months  and   [ %s ]  Days Old !" %(age_year,age_month,age_day))


print('\n-----Age Calculator-----\n')
y = int(input('\nEnter year of birth: '))
m = int(input ('\nEnter month of birth:'))
d = int(input('\nEnter day of birth: '))

print ('\n-------------------------')
print ('\n\nToday : %s / %s / %s' %(today.year,today.month,today.day))

check_birthday(y,m,d)

print ('\n-------------------------')