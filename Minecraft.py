#!/usr/bin/env python3

import copy	


class Enchantment(object):
	def __init__(self, _name, _max_level, _book_multi, _item_multi):
		self.name = _name
		self.max_level = _max_level
		self.excluded = set()
		self.book_multi = _book_multi
		self.item_multi = _item_multi
		self.id = None

Protection = 0
FireProtection = 1
FeatherFalling = 2
BlastProtection = 3
ProjectileProtection = 4
Thorns = 5
Respiration = 6
DepthStrider = 7
AquaAffinity = 8
Sharpness = 9
Smite = 10
BaneofArthropods = 11
Knockback=12
FireAspect=13
Looting = 14
Efficiency = 15
SilkTouch = 16
Unbreaking = 17
Fortune = 18
Power = 19
Punch =20
Flame=21
Infinity=22
LuckoftheSea=23
Lure=24
FrostWalker=25
Mending=26
Impaling=29
Riptide=30
Loyalty=31
Channeling=32
SweepingEdge =100

Enchantments = {
	Protection: Enchantment("Protection", 5,1,1),
	FireProtection: Enchantment("Fire Protection", 4, 2, 1),
	FeatherFalling: Enchantment("Feather Falling", 4, 2, 1),
	BlastProtection: Enchantment("Blast Protection", 4, 4, 2),
	ProjectileProtection: Enchantment("Projectile Protection", 4, 2, 1),
	Thorns: Enchantment("Thorns", 3, 8, 4),
	Respiration: Enchantment("Respiration", 3, 4, 2),
	DepthStrider: Enchantment("Depth Strider", 3, 4, 2),
	AquaAffinity: Enchantment("Aqua Affinity", 1, 4, 2),
	Sharpness: Enchantment("Sharpness", 5, 1, 1),
	Smite: Enchantment("Smite", 5, 2, 1),
	BaneofArthropods: Enchantment("Bane of Arthropods", 5, 2, 1),
	Knockback: Enchantment("Knockback", 2, 2, 1),
	FireAspect: Enchantment("Fire Aspect", 2, 4, 2),
	Looting: Enchantment("Looting", 3, 2, 1),
	Efficiency: Enchantment("Efficiency", 5, 1, 1),
	SilkTouch: Enchantment("Silk Touch", 1, 8, 4),
	Unbreaking: Enchantment("Unbreaking", 3, 2, 1),
	Fortune: Enchantment("Fortune", 3, 4, 2),
	Power: Enchantment("Power", 5, 1, 1),
	Punch: Enchantment("Punch", 2, 4, 2),
	Flame: Enchantment("Flame", 1, 4, 2),
	Infinity: Enchantment("Infinity", 1, 8, 4),
	LuckoftheSea: Enchantment("Luck of the Sea", 3, 4, 2),
	Lure: Enchantment("Lure", 3, 4, 2),
	FrostWalker: Enchantment("Frost Walker", 2, 4, 2),
	Mending: Enchantment("Mending", 1, 4, 2),
	Impaling: Enchantment("Impaling", 5, 2, 1),
	Riptide: Enchantment("Riptide", 3, 4, 2),
	Loyalty: Enchantment("Loyalty", 3, 1, 1),
	Channeling: Enchantment("Channeling", 1, 8, 4),
	SweepingEdge: Enchantment("Sweeping Edge", 3, 4, 2),
}

Exculsions=[
	set([Fortune, SilkTouch]),
	set([DepthStrider, FrostWalker]),
	set([Sharpness, Smite, BaneofArthropods]),
	set([Infinity, Mending]),
	set([Loyalty, Riptide]),
	set([Channeling, Riptide])
]

class Item (object):
	def __init__(self, _is_book, compatible=set(), _rework=0):
		self.renamed=False
		self.is_book=_is_book
		self.reworked=_rework
		self.compatible = compatible
		self.enchantments={}

	def add_ench(self, ench, level):
		self.enchantments[ench] = level

	def ench_str(self):
		return ",".join([Enchantments[key].name + ":" + str(self.enchantments[key]) for key in self.enchantments])

	def __str__(self):
		return "(" + type(self).__name__ + " {" + self.ench_str() + "} reworked:" + str(self.reworked)+")"

# Protection = Enchantment("Protectaion", 5, 5, 1, 1)

Everytime = set([Unbreaking, Mending])
ArmorBasic = Everytime.union(set([Protection, FireProtection, BlastProtection, ProjectileProtection, Thorns]))
ToolBasic = Everytime.union(set([Efficiency]))
ToolBasicPlus = ToolBasic.union(set([SilkTouch, Fortune]))
WeaponBasic = Everytime.union(set([Sharpness, Smite, BaneofArthropods]))
WeaponBasicPlus = WeaponBasic.union(set([Knockback, FireAspect, Looting]))

class BodyArmor(Item):
	def __init__(self, _rework=0):
		super(BodyArmor, self).__init__(False, ArmorBasic, _rework)

class Pants(Item):
	def __init__(self, _rework=0):
		super(Pants, self).__init__(False, ArmorBasic, _rework)

class Helmet(Item):
	def __init__(self, _rework=0):
		super(Helmet, self).__init__(False, ArmorBasic.union(set([Respiration, AquaAffinity])), _rework)

class Shoes(Item):
	def __init__(self, _rework=0):
		super(Shoes, self).__init__(False, ArmorBasic.union(set([FrostWalker, DepthStrider, FeatherFalling])), _rework)

class Swords(Item):
	def __init__(self, _rework=0):
		super(Swords, self).__init__(False, WeaponBasicPlus, _rework)

class Axe(Item):
	def __init__(self, _rework=0):
		super(Axe, self).__init__(False, ToolBasicPlus.union(WeaponBasic), _rework)

class Pickaxe(Item):
	def __init__(self, _rework=0):
		super(Pickaxe, self).__init__(False, ToolBasicPlus, _rework)

class Shovel(Item):
	def __init__(self, _rework=0):
		super(Shovel, self).__init__(False, ToolBasicPlus, _rework)

class Sheers(Item):
	def __init__(self, _rework=0):
		super(Sheers, self).__init__(False, ToolBasic, _rework)

# class Hoe(Item):
# 	def __init__(self, _rework=0):
# 		super(Hoe, self).__init__(False, set([Protection]), _rework)

# class Eletra(Item):
# 	def __init__(self, _rework=0):
# 		super(Eletra, self).__init__(False, set([Protection]), _rework)

# class FishingPole(Item):
# 	def __init__(self, _rework=0):
# 		super(FishingPole, self).__init__(False, set([Protection]), _rework)

# class Bow(Item):
# 	def __init__(self, _rework=0):
# 		super(Bow, self).__init__(False, set([Protection]), _rework)

class Book(Item):
	def __init__(self, _rework=0):
		super(Book, self).__init__(True, _rework=_rework)

def check_enchantment_equality(i1, i2):
	if not isinstance(i1, Item):
		raise "primary is not an Item"

	if not isinstance(i2, Item):
		raise "secondary is not an Item"

	return i1.enchantments == i2.enchantments

def check_equality(i1, i2, check_reworked=True):
	return check_enchantment_equality(i1, i2) and (not check_reworked or i1.reworked == i2.reworked) and type(i1) == type(i2)

def rework_cost(item):
	if not isinstance(item, Item):
		raise
	if item.reworked == 0:
		return 0
	return (2**(item.reworked)) - 1

def check_compadibility(ench, ench_d):
	ench_set = set([key for key in ench_d])
	for ex in Exculsions:
		if ench in ex and bool((ex - set([ench])) & ench_set):
			return True
	return False

class BadPair(BaseException):
	"""docstring for BadPair"""
	def __init__(self):
		super(BadPair, self).__init__()
		

def Combine(item, sacrifice):
	if not isinstance(item, Item):
		raise "primary is not an Item"

	if not isinstance(sacrifice, Item):
		raise "secondary is not an Item"

	if not isinstance(sacrifice, Book) and type(item) != type(sacrifice):
		raise BadPair()
		raise "Can't have two different type objects"

	res = copy.deepcopy(item)
	e_cost = 0

	# print(sacrifice)

	for y in sacrifice.enchantments:
		# print("test")
		if check_compadibility(y, res.enchantments):
			# print("pass", Enchantments[y].name)
			pass
		elif y not in res.compatible and not res.is_book:
			# print("?", Enchantments[y].name)
			e_cost = e_cost + 1
		else:
			if y in res.enchantments:
				if sacrifice.enchantments[y] > res.enchantments[y]:
					res.enchantments[y] = sacrifice.enchantments[y]
				elif sacrifice.enchantments[y] == res.enchantments[y]:
					if res.enchantments[y] < Enchantments[y].max_level:
						res.enchantments[y] = res.enchantments[y] + 1
			else:
				res.enchantments[y] = sacrifice.enchantments[y]

			if sacrifice.is_book:
				multi = Enchantments[y].book_multi
			else:
				multi = Enchantments[y].book_multi

			e_cost = res.enchantments[y] * multi + e_cost

	r_cost = rework_cost(item) + rework_cost(sacrifice)

	cost = r_cost + e_cost

	res.reworked = item.reworked+1
	return cost, res


#TESTS

def TestThing():
	b1 = Book(1)
	b1.add_ench(Fortune, 3)
	b1.add_ench(Efficiency, 5)
	b1.add_ench(Unbreaking, 3)
	b1.add_ench(Mending, 1)

	p = Pickaxe()

	c, i = Combine(p, b1)
	print(c, i)


def test_incompatible():
	h = Helmet()

	b1 = Book()
	b1.add_ench(Fortune, 2)

	c, i = Combine(h, b1)
	print(i) # no change


def testEquality_check():
	b1 = Book()
	b1.add_ench(Fortune, 2)
	b2 = Book()
	b2.add_ench(Fortune, 2)
	b3 = Book()
	b3.add_ench(Fortune, 3)

	print(check_enchantment_equality(b1, b2)) #True
	print(check_enchantment_equality(b1, b3)) #False


def testExculsion():

	p = Pickaxe()
	p.add_ench(SilkTouch, 1)
	b = Book()
	b.add_ench(Fortune, 2)

	c, i = Combine(p, b)
	print(i) #Just Silk Touch


def SimpleTest():
	ba = BodyArmor()
	ba.add_ench(Protection, 1)
	b1 = Book()
	b1.add_ench(Protection, 3)

	c, i = Combine(ba, b1)
	print(c, i)
	c, i = Combine(i, b1)
	print(c, i)

	c, b2 = Combine(b1, b1)
	print(c, b2)

	c, i = Combine(i, b2)
	print(c, i)

	c, b3 = Combine(b2, b2)
	print(c, b3)

	# print (i, b1)
	c, bb = Combine(i, b3)
	print(c, bb)

def CheckBadPair():
	try:
		b = BodyArmor()
		p = Pickaxe()
		Combine(b, p)
	except BadPair:
		print("Good")

def test_e_equalities():
	b1 = Book()
	p1 = Pickaxe()

	print(check_enchantment_equality(b1, p1))

	b2 = Book()
	b2.add_ench(Protection, 1)

	print(not check_enchantment_equality(b1, b2))

	p1.add_ench(Protection, 1)

	print(check_enchantment_equality(b2, p1))

	b1.add_ench(Protection, 1)
	b1.add_ench(Unbreaking, 1)

	print(not check_enchantment_equality(b1, b2))

def test_equalities():
	b1 = Book()
	p1 = Pickaxe()
	p2 = Pickaxe()

	b2 = Book()
	b2.add_ench(Protection, 1)

	b3 = Book(1)

	b4 = Book(1)
	b4.add_ench(Protection, 1)

	c, i = Combine(b1, b2)

	#all True
	print(not check_equality(b1, p1))
	print(check_equality(p2, p1))
	print(not check_equality(b2, b1))
	print(not check_equality(b3, b1))
	print(not check_equality(b2, b4))
	print(check_equality(b4, i))
	print(check_equality(b3, b1, False))

def _print_bottom_up(answer):
	cost, items = answer
	item1, item2 = items
	cost1 = 0
	cost2 = 0

	if not isinstance(item1, Item):
		cost1, item1 = _print_bottom_up(item1)
	
	if not isinstance(item2, Item):
		cost2, item2 = _print_bottom_up(item2)

	print("For", cost, "Levels Combine", item1, "and", item2)
	c, i = Combine(item1, item2)
	return c + cost1 + cost2, i

def print_answer(answer):
	c, item = _print_bottom_up(answer)
	print("For",c,"recieve", item)
	print()
	pass

def pair_up(iList, goal):
	[print_answer(ans) for ans in _pair_up(iList, goal, 0)]

def Test_calculate_value():
	x = Book()
	ans1 = (3, (x,x))
	ans2 = (2, (x,x))
	ans3 = (1, ((2, (x,x)),x))
	ans4 = (1, (x, (1,(x,x))))
	ans5 = (1, (x, (1,((1,(x,x)),x))))
	ans6 = (1, ((1,(x,x)), (1,(x,x))))
	ans7 = (1, ((1,((1,(x,x)),(1,(x,(1,(x,x)))))), (1,((1,(x,(1,((1,(x,x)),x)))),x))))

	print(calculate_value(ans1) == 3)
	print(calculate_value(ans2) == 2)
	print(calculate_value(ans3) == 3)
	print(calculate_value(ans4) == 2)
	print(calculate_value(ans5) == 3)
	print(calculate_value(ans6) == 3)
	print(calculate_value(ans7) == 9)

def calculate_value(answer):
	cost, i = answer
	item1, item2 = i

	if isinstance(item1, Item) and isinstance(item2, Item):
		return cost
	else:
		c1 = 0
		if not isinstance(item1, Item):
			c1 = calculate_value(item1)

		c2 = 0
		if not isinstance(item2, Item):
			c2 = calculate_value(item2)

		return cost + c1 + c2

def Test_Lowest_answers():
	x = Book()
	ans1 = (3, (x,x))
	ans2 = (2, (x,x))
	ans3 = (1, ((2, (x,x)),x))
	ans4 = (1, (x, (1,(x,x))))
	ans5 = (1, (x, (1,((1,(x,x)),x))))
	ans6 = (1, ((1,(x,x)), (1,(x,x))))

	print(lowest_anwers_only([], None, ans1) == [ans1])
	print(lowest_anwers_only([ans1], 3, ans1) == [ans1,ans1])
	print(lowest_anwers_only([ans1], 3, ans2) == [ans2])
	print(lowest_anwers_only([ans1], 3, ans3) == [ans1,ans3])
	print(lowest_anwers_only([ans4], 2, ans1) == [ans4])
	print(lowest_anwers_only([ans1,ans3,ans5], 3, ans4) == [ans4])
	print(lowest_anwers_only([ans1,ans3], 3, ans5) == [ans1,ans3,ans5])
	print(lowest_anwers_only([ans1], 3, ans6) == [ans6])


def lowest_anwers_only(answer_list, local_lowest, new_answer):

	value = calculate_value(new_answer)
	#if emplty trivially add the item
	if not answer_list:
		local_lowest = value
		return local_lowest, [new_answer]

	#We can assume all answers have the same value
	#that value is the lowest value
	if value < local_lowest:
		local_lowest = value
		return local_lowest, [new_answer]
	elif value > local_lowest:
		return local_lowest, answer_list
	elif value == local_lowest:
		answer_list.append(new_answer)
		return local_lowest, answer_list

	raise "Shouldn't reach here"

def Test_replace_item_simple():

	b1 = Book()
	b1.add_ench(Unbreaking,1)

	b2 = Book()
	b2.add_ench(Unbreaking,1)

	cost, b3 = Combine(b1, b2)

	p = Pickaxe()

	ans = replace_item((10, (p, b3)), (1, (b1, b2)), b3)

	print(ans == (10, (p, (1, (b1, b2)))))

def Test_replace_item_deep():

	b1 = Book()
	b1.add_ench(Unbreaking,1)

	b2 = Book()
	b2.add_ench(Unbreaking,1)

	cost, b3 = Combine(b1, b2)

	p = Pickaxe()

	ans = replace_item((3, (p, (2, (b1, b3)))), (1, (b1, b2)), b3)

	print(ans == (3, (p, (2, (b1, (1, (b1, b2)))))))

def replace_item(a, combo, item):
	ans_cost, last_comb = a
	item1,item2 = last_comb
	new_answer = None
	if item1 == item:
		return (ans_cost, (combo, item2))
	elif item2 == item:
		return (ans_cost, (item1, combo))
	else:
		#check in the lower levels
		if not isinstance(item1, Item):
			a1 = replace_item(item1, combo, item)
			if a1:
				return (ans_cost, (a1, item2))

		if new_answer is None and not isinstance(item2, Item):
			a2 = replace_item(item2, combo, item)
			if a2:
				return (ans_cost, (item1, a2))

	return None

def _pair_up(iList, goal, current_cost):
	answers = []
	# global lowest_value
	local_lowest = None

	for mergee in iList:
		possible_mergers = list(iList)
		possible_mergers.remove(mergee)
		for merger in possible_mergers:
			try:
				item_cost, new_item = Combine(mergee, merger)
				#maximum amount of levels you can echant with is 39
				if item_cost >= 40:
					pass
				#if calulated value is higher then the lowest current value
				#stop there
				elif local_lowest is not None and item_cost + current_cost > local_lowest:
					pass
				#if it doesn't meaninfully change the first item
				#don't bother
				elif check_equality(new_item, mergee, False):
					pass
				#if it doesn't change the second one why bother at all
				elif check_equality(new_item, merger):
					pass
				#check if item is the goal state
				elif check_equality(new_item, goal, False):
					#need to add for possible futures
					local_lowest, answers = lowest_anwers_only(answers, local_lowest, (item_cost, (mergee, merger)))

				else:
					next_list = list(possible_mergers)
					next_list.remove(merger)
					next_list.append(new_item)

					ans = _pair_up(next_list, goal, item_cost + current_cost)

					for a in ans:
						local_lowest, answers = lowest_anwers_only(answers, local_lowest, replace_item(a, (item_cost, (mergee, merger)), new_item))

			#This is a improper pairing of items
			except BadPair:
				pass

	return answers

def TryPairingS():
	b1 = Book()
	b1.add_ench(Fortune, 3)
	b2 = Book()
	b2.add_ench(Efficiency, 5)

	p = Pickaxe()

	goal = Pickaxe()
	goal.add_ench(Fortune, 3)
	goal.add_ench(Efficiency, 5)

	pair_up([b1, b2, p], goal)

def TryPairingD():
	b1 = Book()
	b1.add_ench(Fortune, 3)
	b3 = Book()
	b3.add_ench(Fortune, 3)
	b2 = Book()
	b2.add_ench(Efficiency, 5)

	p = Pickaxe()

	goal = Pickaxe()
	goal.add_ench(Fortune, 3)
	goal.add_ench(Efficiency, 5)

	pair_up([b1, b2, b3, p], goal)

def TryPairingL():
	b1 = Book()
	b1.add_ench(Fortune, 3)
	b2 = Book()
	b2.add_ench(Efficiency, 5)
	b3 = Book()
	b3.add_ench(Unbreaking, 3)
	b4 = Book()
	b4.add_ench(Mending, 1)

	p = Pickaxe()

	goal = Pickaxe()
	goal.add_ench(Fortune, 3)
	goal.add_ench(Efficiency, 5)
	goal.add_ench(Unbreaking, 3)
	goal.add_ench(Mending, 1)

	pair_up([b1, b2, b3, b4, p], goal)

if __name__ == "__main__":
	TryPairingL()
