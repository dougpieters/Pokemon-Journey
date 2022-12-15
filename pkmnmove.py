class PkmnMove:

	def __init__(self, name, type, stat, buff, pwr, acc, atk, dfn, spd):
		self.name = str.title(name)
		self.type = str.title(type)
		self.stat = bool(stat)
		self.buff = bool(buff)
		self.pwr = int(pwr)
		self.acc = float(acc)
		self.atk = float(atk)
		self.dfn = float(dfn)
		self.spd = float(spd)


Tackle = PkmnMove("Tackle", "Normal", False, False, 40, 100, 0, 0, 0)
Scratch = PkmnMove("Scratch", "Normal", False, False, 40, 100, 0, 0, 0)
TailWhip = PkmnMove("Tail Whip", "Normal", True, False, 0, 100, 0, -1, 0)
Growl = PkmnMove("Growl", "Normal", True, False, 0, 100, -1, 0, 0)
Ember = PkmnMove("Ember", "Fire", False, False, 40, 100, 0, 0, 0)
Bubble = PkmnMove("Bubble", "Water", False, False, 40, 100, 0, 0, 0)
VineWhip = PkmnMove("Vine Whip", "Grass", False, False, 40, 100, 0, 0, 0)
Flamethrower = PkmnMove("Flamethrower", "Fire", False, False, 100, 100, 0, 0, 0)
HydroPump = PkmnMove("Hydro Pump", "Water", False, False, 100, 100, 0, 0, 0)
Solarbeam = PkmnMove("Solarbeam", "Grass", False, False, 100, 100, 0, 0, 0)
SwordsDance = PkmnMove("Swords Dance", "Normal", True, True, 0, 100, 2, 0, 0)

