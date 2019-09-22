''' 

OUTPUT:
======================================================== 
|Welcome to HR Pro 2019
|
|    1. Show Employees
|    2. Show Managers
|    3. Add An Employee
|    4. Add A Manager
|    5. Exit
|What would you like to do? 
|3
|-----------------
|Name: shosho
|Age: 24
|Salary: 666
|Employement year: 2018
|Employee added succesfully !
|-----------------
|
|    1. Show Employees
|    2. Show Managers
|    3. Add An Employee
|    4. Add A Manager
|    5. Exit
|
|What would you like to do? 
|1
|-----------------
|Name: shosho, Age: 24, Salary: 666, Working Years: 1
|-----------------
|
|    1. Show Employees
|    2. Show Managers
|    3. Add An Employee
|    4. Add A Manager
|    5. Exit
|
|What would you like to do? 
|4
|-----------------
|Name: sammy
|Age: 52
|Salary: 4600
|Employement Year: 1900
|Bonus Percentage: .3
|Manager added succesfully
|-----------------
|    1. Show Employees
|    2. Show Managers
|    3. Add An Employee
|    4. Add A Manager
|    5. Exit
|
|What would you like to do? 
|2
|-----------------
|Name: sammy, Age: 52, Salary: 4600, Working Years: 119, Bonus: 1380.000000
|-----------------
|
|Options:
|    1. Show Employees
|    2. Show Managers
|    3. Add An Employee
|    4. Add A Manager
|    5. Exit
|
|What would you like to do?
| 5
|
|<==Exiting==>
=========================================================
'''


import datetime
from datetime import date

today  = date.today()

class Employee: 
	
	def __init__(self , name , age , salary , employment_date):
		self.name =name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
	def get_working_years(self):
		working_years = today.year-int(self.employment_date)
		return working_years

class Manager: 

	def __init__(self ,name , age , salary , employment_date , bonus_percentage):	
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
		self.bonus_percentage = bonus_percentage
	def get_working_years(self):
		working_years =  today.year - int(self.employment_date)
		return working_years
	def get_bonus(self):
		bounus = float(self.salary)*float(self.bonus_percentage)
		return bounus



Employees=[]
Managers=[]

option = 0

print ('\nWelcome to HR Pro 2019')



while option != 5 :

	option = int(input ('\n\t1. Show Employees\n\t2. Show Managers\n\t3. Add An Employee\n\t4. Add A Manager\n\t5. Exit\nWhat would you like to do? \n'))

	if option == 1: 
		for n in Employees:
			print('-----------------')
			print ('Name: {} Age: {} Salary: {} Working Years: {}'.format(n.name,n.age,n.salary,(n.get_working_years())))
			print('-----------------')

	elif option == 2: 
		for n in Managers:
			print('-----------------')
			print ('Name: {} Age: {} Salary: {} Working Years: {} Bonus: {}'.format(n.name,n.age,n.salary,n.get_working_years(),n.get_bonus()))
			print('-----------------')

	elif option == 3: 
		print('-----------------')
		
		name= input('Name: ')
		age= input('Age: ')
		salary = input('Salary: ')
		employment_date= input('Employement year: ') 
		e=Employee(name , age , salary , employment_date)
		Employees.append(e)
		print ('\nEmployee added succesfully!')
		print('-----------------')

	elif option == 4: 
		print('-----------------')
		
		name= input('Name: ')
		age= input('Age: ')
		salary= input('Salary: ')
		employment_date= input('Employement year: ') 
		bonus_percentage=float(input('Bonus Percentage: '))
		m=Manager(name , age , salary , employment_date , bonus_percentage)
		Managers.append(m)
		print ('Manager is added succesfully!')
		print('-----------------')
	else :
		print('\n\n<==Exiting==>\n\n')
		option = 5









