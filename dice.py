import random

class dice:

	def __sanityCheck(self, int=null, string=null, bool=null):
		__temp
		if int != null:
			try:
				__temp = int(int)
			except exception e:
				print( int + "is not an integer.")
			else:
				return __temp
		elif string != null:
			return string
		elif bool != null:
			try:
				__temp = bool(bool)
			except exception e:
				print( bool + "is not an integer.")
			else:
				return __temp

	def __init__(self, sides):
		self.__sanityCheck(int=sides)

	def setSides(self, sides):
		self.__sanityCheck(int=sides)

	def roll(self):
		return random.randint(1, self._sides)