class PkmnMove:

	def __init__(self, name, type, pwr, acc, atk, dfn, spd):
		self.name = str.title(name)
		self.type = str.title(type)
		self.pwr = int(pwr)
		self.acc = float(acc)
		self.atk = float(atk)
		self.dfn = float(dfn)
		self.spd = float(spd)


Tackle = PkmnMove("Tackle", "Normal", 40, 100, 0, 0, 0)
Scratch = PkmnMove("Scratch", "Normal", 40, 100, 0, 0, 0)
TailWhip = PkmnMove("Tail Whip", "Normal", 0, 100, 0, -0.2, 0)
Growl = PkmnMove("Growl", "Normal", 0, 100, -0.2, 0, 0)
Ember = PkmnMove("Ember", "Fire", 40, 100, 0, 0, 0)
Bubble = PkmnMove("Bubble", "Water", 40, 100, 0, 0, 0)
VineWhip = PkmnMove("Vine Whip", "Grass", 40, 100, 0, 0, 0)
Flamethrower = PkmnMove("Flamethrower", "Fire", 100, 100, 0, 0, 0)
HydroPump = PkmnMove("Hydro Pump", "Water", 100, 100, 0, 0, 0)
Solarbeam = PkmnMove("Solarbeam", "Grass", 100, 100, 0, 0, 0)