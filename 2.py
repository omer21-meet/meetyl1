
class Animal(object):
	def __init__(self,sound,name,age,fav_color,fav_food):
		self.sound = sound
		self.name = name
		self.age = age
		self.fav_color = fav_color
		self.fav_food = fav_food
	def eat(self,fav_food):
		print("Yummi!" +  "is eating " + self.fav_food)
	def description(self):
		print(self.name + "is" + str(self.age) + "years old and loves the color" + self.fav_color)		
	def make_sound(self):
		print(self.sound + self.sound +  self.sound)

dog = Animal("Hav","Jerry",17,"black","Grass")
dog.eat("fav_food")
dog.description()
dog.make_sound()

class Human(object):
	def __init__(self,name,age,city,gender,fav_breakfest,fav_sports):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.fav_breakfest = fav_breakfest
		self.fav_sports = fav_sports
	def eat_breakfest(self,fav_breakfest):
		print("Yummi!" +  "is eating " + self.fav_breakfest)
	def sports(self):
		print(self.name + " is playing " + self.fav_sports)	

human = Human("Omer",15,"ZurHaddasah","Male","Cornflaks","Soccer")
human.eat_breakfest("fav_breakfest")
human.sports()


