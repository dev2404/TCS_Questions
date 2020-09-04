class cars:
	def __init__(self,speed,units):
		self.speed = speed
		self.units = units

	def car(self):
		print("Car with the maximum speed of", self.speed + self.units.strip())


ca = cars("151", "km/pr")
print(ca.car())		