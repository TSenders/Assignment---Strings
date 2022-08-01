# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
"""Report of the UEFA Euro 1988 final between
the Soviet Union and The Neterlands, played at the
Olympiastadion in Munich """

#Goalscorers

scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

#Score minutes

goal_0 = 32
goal_1 = 54

scorers = (f'{scorer_0}'' 'f'{goal_0}'', 'f'{scorer_1}'' 'f'{goal_1}')
print(scorers)

report = (f'{scorer_0} ''scored in the 'f'{goal_0}nd minute' '\n'
f'{scorer_1} ''scored in the 'f'{goal_1}th minute')
print(report)

#Find the players first name

player = ('Frank Rijkaard')
first_name = player.find('F') #Find the position of the first letter from the players first name
print(first_name)
first_name = player.find('k') #Find the position of the last letter from the players first name
print(first_name)
first_name = slice(0,5) #Take all letters from the first till the last position found
print(player[first_name]) #Print result found
first_name = ('Frank')

#Find the players last name and last name length

last_name_len = player.find('R', 5,) #Find the position of the first letter from the players last name
print(last_name_len)
last_name_len = player.find('d') #Find the postion of the last letter from the players last name
print(last_name_len)
last_name_len = slice(6,14) #Take all letters form the first till the last postion found
print(player[last_name_len]) #Print result found
last_name_len = 'Rijkaard'
print(len(last_name_len)) #Print the length of the last name
last_name_len = 8
name_short = (player[0]) + ('. ') + (player[6:14]) #Give the first letter from the first name and the entire last name of the player
print(name_short)
player1 = ('Frank!')
chant = (f'{player1} 'f'{player1} 'f'{player1} 'f'{player1} 'f'{player1}') 
print(chant)
good_chant = (chant != ('Frank!' * 5))
print(good_chant)