print('\n\nMad libs where libs get mad.')
print('\nStart below:')

time = input('\nEnter a number from 1 to 12: ')
items = raw_input('Enter a noun (plural): ')
name = raw_input('Enter a name: ')
scream = raw_input('Enter any sentence: ')
action = raw_input('Enter a verb: ')

print ('\n\tIt was ' + str(time) + ' o\'clock when I heard a knock at the door.') 
print ('\tI opened the door and there was a box full of ' + items + ' with a note saying \"From Mr.' + name.title() + '.\"')
print ('\tJust as I closed the door I heard a scream \"' + scream.upper() + '.\"')
print ('\tI froze in place and all I could do was ' + action + '.\n\n')