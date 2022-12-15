import typechart as tc
import pkmnmove as move
import utility as utl
import random
import time

def delay_print(s):
	utl.d_print(s)

S0 = 0.00
S1 = 0.25
S2 = 0.40
S3 = 0.55
S4 = 0.70
S5 = 0.85
S6 = 1.00
S7 = 1.25
S8 = 1.40
S9 = 1.55
S10 = 1.70
S11 = 1.85
S12 = 2.00
buffs = [S0,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12]
debuffs = [S0,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12]


#Create Pokemon Class
class Pokemon:

	def __init__(self, name, type, moves, lvl, maxhp, atk, dfn, spd):
		self.name = str.title(name)
		self.types = str.title(type)
		self.moves = []
		self.lvl = int(lvl)
		self.maxhp = int(maxhp) #This is so that an HP stat can be manipulated during battle, 
		self.hp = self.maxhp 	#while maintaining a max HP stat that can increase on level up
		self.atk = int(atk)
		self.dfn = int(dfn)
		self.spd = int(spd)
		self.xp = int(self.lvl * (self.lvl / 2))  #exp gained for defeating this pokemon in battle
		self.exp = int(self.lvl**3)  #total exp needed for given pokemon level
		self.atkbuff = 6
		self.dfnbuff = 6
		self.spdbuff = 6
		self.attack = self.atk * float(buffs[int(self.atkbuff)]) # Same with HP
		self.defense = self.dfn * float(buffs[int(self.dfnbuff)]) # This breaks up what gets
		self.speed = self.spd * float(buffs[int(self.spdbuff)]) # changed in battle vs. level up
	
	def maxPotion(self):
		self.hp = self.maxhp

	def clearStats(self):
		self.atkbuff = 6
		self.dfnbuff = 6
		self.spdbuff = 6

	def applyBuffs(self):
		self.attack *= buffs[int(self.atkbuff)]
		self.defense *= buffs[int(self.dfnbuff)]
		self.speed *= buffs[int(self.spdbuff)]

	def fight(self, Pokemon2):
		# Allow two pokemon to fight each other
		print(f'''
	 -----Pokemon Battle-----
	''')
		delay_print(f'''
	 {self.name} vs. {Pokemon2.name}
	\n''')
		time.sleep(2)

		#start battle with a speed check
		while (self.hp > 0) and (Pokemon2.hp > 0):
			if self.speed >= Pokemon2.speed:
				#You attack first
				print(f"Go {self.name}!\n")
				for i, x in enumerate(self.moves):
					print(f"{i+1}.", x.name)
				index = (int(input('Pick a move: '))) - 1
				SelectMove1 = self.moves[index]
				delay_print(f"\n{self.name} used {SelectMove1.name}!\n")
				time.sleep(1)
				#damage calc
				if SelectMove1.buff == False:
					if SelectMove1.stat == False:
						if SelectMove1.type == self.types:
								stab = 1.5
						else:
								stab = 1.0
						effectiveness = tc.pkmn_types[SelectMove1.type][Pokemon2.types]
						rnum = random.randint(217,255)
						dmg1 = int((((((((((2*self.lvl)/5)*SelectMove1.pwr*((self.attack*2)/(Pokemon2.defense*1.2)))/50)+2)*stab)*effectiveness)*rnum)/255))
						if effectiveness == 1.5:
							delay_print(f"{Pokemon2.name} was hit! It's super effective!\n")
						elif effectiveness == 1.0:
							delay_print(f"{Pokemon2.name} was hit!\n")
						elif effectiveness == 0.5:
							delay_print(f"{Pokemon2.name} was hit! It's not very effective....\n")
						else:
							delay_print(f"It doesn't effect {Pokemon2.name}!\n")
						Pokemon2.hp -= dmg1
						delay_print(f"{Pokemon2.name} took {dmg1} damage!\n\n")
						if Pokemon2.hp <= 0:
							win = True
							delay_print(f"{Pokemon2.name} has fainted...\n")
							break
					elif SelectMove1.stat == True:
						Pokemon2.atkbuff += SelectMove1.atk
						Pokemon2.dfnbuff += SelectMove1.dfn
						Pokemon2.spdbuff += SelectMove1.spd
						Pokemon2.applyBuffs()
						print(f"{Pokemon2.name}'s stats have changed!")
				elif SelectMove1.buff == True:
					self.atkbuff += SelectMove1.atk
					self.dfnbuff += SelectMove1.dfn
					self.spdbuff += SelectMove1.spd
					self.applyBuffs()
					print(f"{self.name}'s stats have changed!")

			#Opponent attacks next
				print(f"It's {Pokemon2.name} turn!")
				index = (random.randint(0, len(Pokemon2.moves))) - 1
				SelectMove2 = Pokemon2.moves[index]
				delay_print(f"\n{Pokemon2.name} used {SelectMove2.name}!\n")
				time.sleep(1)
				#damage calc
				if SelectMove2.buff == False:
					if SelectMove2.stat == False:
						if SelectMove2.type == Pokemon2.types:
								stab2 = 1.5
						else:
								stab2 = 1.0
						effectiveness = tc.pkmn_types[SelectMove2.type][self.types]
						rnum = random.randint(217,255)
						dmg2 = int((((((((((2*Pokemon2.lvl)/5)*SelectMove2.pwr*((Pokemon2.attack*2)/(self.defense*1.2)))/50)+2)*stab2)*effectiveness)*rnum)/255))
						if effectiveness == 1.5:
							delay_print(f"{self.name} was hit! It's super effective!\n")
						elif effectiveness == 1.0:
							delay_print(f"{self.name} was hit!\n")
						elif effectiveness == 0.5:
							delay_print(f"{self.name} was hit! It's not very effective....\n")
						else:
							delay_print(f"It doesn't effect {self.name}!\n")
						self.hp -= dmg2
						delay_print(f"{self.name} took {dmg2} damage!\n\n")
						if self.hp <= 0:
							win = False
							delay_print(f"{self.name} has fainted...\n")
							break
					elif SelectMove2.stat == True:
						self.atkbuff += SelectMove2.atk
						self.dfnbuff += SelectMove2.dfn
						self.spdbuff += SelectMove2.spd
						self.applyBuffs()
						print(f"{self.name}'s stats have changed!")
				elif SelectMove2.buff == True:
					Pokemon2.atkbuff += SelectMove2.atk
					Pokemon2.dfnbuff += SelectMove2.dfn
					Pokemon2.spdbuff += SelectMove2.spd
					Pokemon2.applyBuffs()
					print(f"{Pokemon2.name}'s stats have changed!")
			elif Pokemon2.speed > self.speed:
				#Opponent attacks first
				print(f"It's {Pokemon2.name} turn!")
				index = (random.randint(0, len(Pokemon2.moves))) - 1
				SelectMove2 = Pokemon2.moves[index]
				delay_print(f"\n{Pokemon2.name} used {SelectMove2.name}!\n")
				time.sleep(1)
				#damage calc
				if SelectMove2.buff == False:
					if SelectMove2.stat == False:
						if SelectMove2.type == Pokemon2.types:
								stab2 = 1.5
						else:
								stab2 = 1.0
						effectiveness = tc.pkmn_types[SelectMove2.type][self.types]
						rnum = random.randint(217,255)
						dmg2 = int((((((((((2*Pokemon2.lvl)/5)*SelectMove2.pwr*((Pokemon2.attack*2)/(self.defense*1.2)))/50)+2)*stab2)*effectiveness)*rnum)/255))
						if effectiveness == 1.5:
							delay_print(f"{self.name} was hit! It's super effective!\n")
						elif effectiveness == 1.0:
							delay_print(f"{self.name} was hit!\n")
						elif effectiveness == 0.5:
							delay_print(f"{self.name} was hit! It's not very effective....\n")
						else:
							delay_print(f"It doesn't effect {self.name}!\n")
						self.hp -= dmg2
						delay_print(f"{self.name} took {dmg2} damage!\n\n")
						if self.hp <= 0:
							win = False
							delay_print(f"{self.name} has fainted...\n")
							break
					elif SelectMove2.stat == True:
						self.atkbuff += SelectMove2.atk
						self.dfnbuff += SelectMove2.dfn
						self.spdbuff += SelectMove2.spd
						self.applyBuffs()
						print(f"{self.name}'s stats have changed!")
				elif SelectMove2.buff == True:
					Pokemon2.atkbuff += SelectMove2.atk
					Pokemon2.dfnbuff += SelectMove2.dfn
					Pokemon2.spdbuff += SelectMove2.spd
					Pokemon2.applyBuffs()
					print(f"{Pokemon2.name}'s stats have changed!")
			#You attack next
				print(f"Go {self.name}!")
				for i, x in enumerate(self.moves):
					print(f"{i+1}.", x.name)
				index = (int(input('Pick a move: '))) - 1
				SelectMove1 = self.moves[index]
				delay_print(f"\n{self.name} used {SelectMove1.name}!\n")
				time.sleep(1)
				#damage calc
				if SelectMove1.buff == False:
					if SelectMove1.stat == False:
						if SelectMove1.type == self.types:
								stab = 1.5
						else:
								stab = 1.0
						effectiveness = tc.pkmn_types[SelectMove1.type][Pokemon2.types]
						rnum = random.randint(217,255)
						dmg1 = int((((((((((2*self.lvl)/5)*SelectMove1.pwr*((self.attack*2)/(Pokemon2.defense*1.2)))/50)+2)*stab)*effectiveness)*rnum)/255))
						if effectiveness == 1.5:
							delay_print(f"{Pokemon2.name} was hit! It's super effective!\n")
						elif effectiveness == 1.0:
							delay_print(f"{Pokemon2.name} was hit!\n")
						elif effectiveness == 0.5:
							delay_print(f"{Pokemon2.name} was hit! It's not very effective....\n")
						else:
							delay_print(f"It doesn't effect {Pokemon2.name}!\n")
						Pokemon2.hp -= dmg1
						delay_print(f"{Pokemon2.name} took {dmg1} damage!\n\n")
						if Pokemon2.hp <= 0:
							win = True
							delay_print(f"{Pokemon2.name} has fainted...\n")
							break
					elif SelectMove1.stat == True:
						Pokemon2.atkbuff += SelectMove1.atk
						Pokemon2.atkbuff += SelectMove1.dfn
						Pokemon2.atkbuff += SelectMove1.spd
						Pokemon2.applyBuffs()
						print(f"{Pokemon2.name}'s stats have changed!")
				elif SelectMove1.buff == True:
					self.atkbuff += SelectMove1.atk
					self.dfnbuff += SelectMove1.dfn
					self.spdbuff += SelectMove1.spd
					self.applyBuffs()
					print(f"{self.name}'s stats have changed!")

		if win == True:
			self.clearStats()
			Pokemon2.clearStats()
			self.exp += Pokemon2.xp;
			delay_print(f"{self.name} gained {Pokemon2.xp} experience!")
			money = Pokemon2.lvl * 50
			delay_print(f"\nOpponent paid you ${money}.\n")
		elif win == False:
			self.clearStats()
			Pokemon2.clearStats()
			money = self.lvl * 50
			delay_print(f"\nYou lost ${money}!")


#Create Starters
Charmander = Pokemon("Charmander", "Fire", [], 5, 14, 10, 9, 12)
Charmander.moves = [move.Scratch, move.Growl]
Squirtle = Pokemon("Squirtle", "Water", [], 5, 14, 10, 12, 9)
Squirtle.moves = [move.Tackle, move.TailWhip]
Bulbasaur = Pokemon("Bulbasaur", "Grass", [], 5, 15, 10, 10, 10)
Bulbasaur.moves = [move.Tackle, move.Growl]

# Stage 2 Evo
Charmeleon = Pokemon("Charmeleon", "Fire", [], 50, 164, 115, 109, 131)
Charmeleon.moves = [move.Scratch, move.Growl, move.Ember]
Wartortle = Pokemon("Wartortle", "Water", [], 50, 165, 114, 131, 109)
Wartortle.moves = [move.Tackle, move.TailWhip, move.Bubble]
Ivysaur = Pokemon("Ivysaur", "Grass", [], 50, 166, 113, 114, 111)
Ivysaur.moves = [move.Tackle, move.Growl, move.VineWhip]

# Stage 3 Evo
Charizard = Pokemon("Charizard", "Fire", [], 100, 359, 266, 254, 298)
Charizard.moves = [move.Scratch, move.Growl, move.Ember, move.Flamethrower]
Blastoise = Pokemon("Blastoise", "Water", [], 100, 361, 264, 298, 254)
Blastoise.moves = [move.Tackle, move.TailWhip, move.Bubble, move.HydroPump]
Venasaur = Pokemon("Venasaur", "Grass", [], 100, 363, 262, 264, 258)
Venasaur.moves = [move.Tackle, move.Growl, move.VineWhip, move.Solarbeam]

starterPokemon = [Charmander, Squirtle, Bulbasaur]
