import random

class Dice:

	def __sanityCheck(self, integer=None, string=None, bool=None):
		__temp = None
		if integer != None:
			try:
				__temp = int(integer)
			except:
				print( integer + " is not an integer.")
			else:
				return __temp
		elif string != None:
			return string
		elif bool != None:
			try:
				__temp = bool(bool)
			except:
				print( bool + " is not an integer.")
			else:
				return __temp

	def __init__(self, sides):
		self._sides = self.__sanityCheck(integer=sides)

	def setSides(self, sides):
		self._sides = self.__sanityCheck(integer=sides)

	def roll(self):
		if self._sides == 2:
			__temp = random.randint(1, self._sides)
			if __temp == 1:
				return 'Heads'
			else:
				return 'Tails'
		else:
			return random.randint(1, self._sides)