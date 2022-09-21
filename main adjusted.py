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
first_name_begin = slice(1) #find the position of the first letter from the players first name
first_name_end = player.find(' ') #find the position of the last letter from the players first name
first_name = (player[:first_name_end]) #compile first name
print(first_name) #print result found

#Find the players last name and last name length

last_name_start = player.find(' ') #find start of last name
last_name_space = player[last_name_start: ] #give result of last name
last_name = last_name_space.lstrip() #give result of last name without space
last_name_len = (len(last_name)) #give lenght of last name
first_name_len = (len(first_name)) #give lenght of first name

#give name short and compile chant

name_short = (player[first_name_begin]) + ('. ') + (last_name) #Give the first letter from the first name and the entire last name of the player
chant_name = first_name + '! ' #compile chant_name (first name of player with exclamation mark)
chant = (chant_name.rstrip()*first_name_len) #remove trailing space from chant
good_chant = chant != (chant_name*first_name_len) 