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

scorers = 'Ruud Gullit ' + str(goal_0), 'Marco van Basten ' + str(goal_1)
print(scorers)

report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'
print(report)

#Find the players first name

player = 'Frank Rijkaard'
first_name_begin = player.find('F') #Find the position of the first letter from the players first name
first_name_end = player.find(' ') #Find the position of the last letter from the players first name
first_name = (player[:first_name_end]) 
print(first_name) #Print result found

#Find the players last name and last name length

last_name_begin = player.find('R', 5,) #Find the position of the first letter from the players last name
print(player[last_name_begin:]) #Print result found
last_name_len = player[last_name_begin:]
print(len(last_name_len)) #Print the length of the last name
name_short = (player[first_name_begin]) + ('. ') + (player[last_name_begin:]) #Give the first letter from the first name and the entire last name of the player
print(name_short)
chant_name = first_name + '! ' 
chant = (chant_name.rstrip()*5)
print(chant)
good_chant = chant != (chant_name*5)
print(good_chant)