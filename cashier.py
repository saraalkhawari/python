'''
OUTPUT: 
Item (enter "done" when finished): apples
Price: .2
Quantity: 4
Item (enter "done" when finished): carrot
Price: .1
Quantity: 1
Item (enter "done" when finished): flour
Price: 1.3
Quantity: 2
Item (enter "done" when finished): water bottles
Price: .05
Quantity: 10
Item (enter "done" when finished): done

-------------------
receipt
-------------------
4 apples 0.800KD
1 carrot 0.100KD
2 flour 2.600KD
10 water bottles 0.500KD
-------------------
Total Price: 4.000KD
'''

items=[]

choice  = ''
i = 0 #Counter
total = 0.0

print('\n')

while choice  != 'done':
	choice  = raw_input('Item (enter "done" when finished): ')
	if choice !='done':
		items.append({'Name': choice  })
		items[i]['Price'] = float(raw_input('Price: '))
		items[i]['Quantity'] = raw_input('Quantity: ')
		total += items[i]['Price']*float(items[i]['Quantity'])
	i += 1

i = 0
print('\n-------------------\nreceipt\n-------------------')

for item in items : 
	print(str(items[i]['Quantity']) +'  '+ items[i]['Name'] +'  '+ str(items[i]['Price']*float(items[i]['Quantity'])) + ' KD' ) 
	i += 1
i=0
print('-------------------')
print ('\nTotal Price : {}KD\n\n'.format(total))



























