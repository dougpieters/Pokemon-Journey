import pokemon as pkmn
import utility as utl
import time

def delay_print(s):
	utl.d_print(s)

#Journey Intro
delay_print("Hello there!\n")
time.sleep(0.5)
delay_print("Welcome to the world of Pokemon!\n\n")
time.sleep(1)
delay_print("My name is Oak,")
time.sleep(0.5)
delay_print(" people call me the Pokémon Professor!\n")
time.sleep(1)
delay_print("This world is inhabited by creatures called Pokémon.\n")
time.sleep(1)
delay_print("For some people,")
time.sleep(0.5)
delay_print(" Pokémon are pets.")
time.sleep(1)
delay_print(" Other use them for fights.\n")
time.sleep(1)
delay_print("Myself...")
time.sleep(0.5)
delay_print("I study Pokémon as a profession.\n\n")
time.sleep(1)
delay_print("First,")
time.sleep(0.5)
delay_print(" what is your name?\n")
# finished time.sleep work here, need to format from this point on

#Select player name
player_name = str.title(input("Your name: "))
time.sleep(1)
delay_print(f"\nRight! So your name is {player_name}!")
time.sleep(1)
delay_print(f'''

This is my grandson. He's been your rival since you were a baby.
...Erm, what is his name again?
''')

#Select Rival Name
rival_name = str.title(input(""))
time.sleep(1)
delay_print(f"\nThat's right! I remember now! His name is {rival_name}!\n\n")
time.sleep(1)
delay_print(f"{player_name}, ")
time.sleep(1)
delay_print("your very own Pokémon legend is about to unfold!\n")
time.sleep(1)
delay_print(f'''
A world of dreams and adventures with Pokémon awaits!
Let's go!
''')
time.sleep(2)

#Start Journey
delay_print('''
|You wake up in your room, excited to start your adventure.
 Make sure to check your PC to find a potion
 Afterwards, you make your way downstairs to see your mom waiting at the table for you.|
''')
time.sleep(1)
delay_print('''
[Mom]:
 Right.''')
time.sleep(1)
delay_print('''
 All boys leave home someday. It said so on TV.''')
time.sleep(1)
delay_print('''
 Prof.Oak, next door, is looking for you.
 Good luck on your journey, I'll be rooting for you!
''')
time.sleep(1)
delay_print('''
|After your chat with your mom, you head out and head over to the Professor's Lab to get your very own Pokemon!|
''')
time.sleep(1)

#Arrive at Lab
delay_print(f'''
|Once you arrive at the Professor's Lab, you approach the Professor and {rival_name} arguing over something.|
 ''')
time.sleep(1)
delay_print(f'''
[{rival_name}]:
 Gramps! I'm fed up with waiting!
''')
time.sleep(1)
delay_print(f'''
[Oak]:
 {rival_name}? ''')
time.sleep(1)
delay_print("Let me think...")
delay_print(f'''

 Oh, that's right! I told you to come. Just wait.
''')
time.sleep(1)
delay_print(f" Here, {player_name}!")
time.sleep(1)
delay_print(f'''
 There are 3 Pokémon here!...
 Haha! They are inside the Poké Balls.

 When I was young, I was a serious Pokémon trainer!
 In my old age, I have only 3 left, but you can have one!
 Choose!
''')
time.sleep(1)
delay_print(f'''
[{rival_name}]:
 Hey!
 Gramps.... What about me?
''')
time.sleep(1)
delay_print(f'''
[Oak]:
 Be patient! {rival_name}, you can have one too!

 Now, {player_name},
 which Pokémon do you want?
''')
delay_print(
 "|Which Pokemon do you choose; Charmander, Squirtle, or Bulbasaur?|\n")
#Choose Your Starter
while True:
	player_starter = str.title(input(""))
	if player_starter == "Charmander":
		player_starter = pkmn.Charmander
		break
	elif player_starter == "Squirtle":
		player_starter = pkmn.Squirtle
		break
	elif player_starter == "Bulbasaur":
		player_starter = pkmn.Bulbasaur
		break
	else:
		delay_print("Please select your starter: \n")
		continue

delay_print(f'''
[Oak]:
 So! You want the {player_starter.types} Pokemon, {player_starter.name}?
 This Pokemon is really energetic!
 ''')
time.sleep(1)
delay_print(f"{player_name} received a {player_starter.name}!\n")
time.sleep(1)
delay_print(f"Would you like to give your {player_starter.name} a nickname?\n")
rename = str.title(input("\n"))
if rename == "Yes":
	player_starter.name = str.title(input("\n"))
else:
	pass

time.sleep(1)
delay_print(f'''
[{rival_name}]:
 I'll take this one then!
''')
time.sleep(1)
if player_starter == pkmn.Charmander:
	rival_starter = pkmn.Squirtle
elif player_starter == pkmn.Squirtle:
	rival_starter = pkmn.Bulbasaur
elif player_starter == pkmn.Bulbasaur:
	rival_starter = pkmn.Charmander

delay_print(f'''
{rival_name} chose {rival_starter.name}

[{rival_name}]:
 My Pokémon looks a lot stronger.''')
time.sleep(1)
delay_print(f'''
 Wait {player_name}!
 Let's check out our Pokémon!

''')
time.sleep(1)
delay_print(" Come on, I'll take you on!\n")
time.sleep(2)

#Start Battle
delay_print(f"|{rival_name} wants to battle!|\n")
time.sleep(1)

delay_print(f"|{rival_name} sent out {rival_starter.name}!|\n")
time.sleep(1)
delay_print(f"[{player_name}]\n Go {player_starter.name}! I choose you!")

player_starter.fight(rival_starter)
