'''
CRITERIA : 
- Age between 20 and 36
- 2 or more years of experience
- Should be a Worker 

OUTPUT:

Welcome to the special recruitment program, 
please answer the following questions:

What's your name?  Sara Ali

How old are you?  21

How many years of experience do you have?  2

	Skills:

		1. Determinded
		2. Worker
		3. Intence
		4. Good Worker
		5. Hard Worker
		6. Terrific

Choose a skill from above by entering its number: 1

Choose another skill from above by entering its number: 2

You have been accepted, Sara Ali
'''


skills_list  = ['Determinded','Worker','Intence','Good Worker','Hard Worker','Terrific']

cv ={}

print('\nWelcome to the special recruitment program, \nplease answer the following questions:')

cv['name'] = raw_input('\nWhat\'s your name?  ')

cv['age'] = input('\nHow old are you?  ')

cv['experience'] = input('\nHow many years of experience do you have?  ')

cv['skills'] = []

print('\n\tSkills:\n')

for i,n in enumerate(skills_list):
	print('\t\t{}. {}'.format(i+1,n))

cv['skills'].append(skills_list[input('\nChoose a skill from above by entering its number: ')-1])

cv['skills'].append(skills_list[input('\nChoose another skill from above by entering its number: ')-1])

if (int(cv['age']) > 20) & (int(cv['age']) < 36) & (int(cv['experience']) >= 2) & ('Worker' in cv['skills']) :
	print ('\nYou have been accepted, {}\n'.format(cv['name']))
else:
	print ('\n!! {}, You Do not fit our criteria!!\n'.format(cv['name']))


print('\n')