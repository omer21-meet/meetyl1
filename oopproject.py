import turtle

mai= turtle.Turtle()

class Post():
	def __init__ (self,name,date,summary):
		self.name= name
		self.date = date
		self.summary = summary

class User():
	def __init__ (self,name,email,password,friend_list=[],posts=[]):
		self.name= name
		self.email = email
		self.password = password
		self.friend_list = []
		self.posts = []
	def add_friend(self):
		email = input("Enter your friend's email")
		self.friend_list.append(email)
		print(self.name + " has added " + email + " as a friend")

	def remove_friend(self):
		email = input("Enter your friend's email")
		self.friend_list.remove(email)
		print(self.name + " has removed " + email)

	def add_post(self):
		text = input("give a name to your post")
		post1 = Post(self.name, "17/11", text )
		# print(post1)
		self.posts.append(post1)
		print(self.name + " has posted " + text)


	def get_userinfo(self):
		print("Name: " + self.name)
		print("Email: " + self.email)
		print("Password: " + self.password)
		print("Friend list: " + str(self.friend_list))
		print("Posts: " + str(self.posts))



def add_friend1():
    user1.add_friend()

def add_post1():
	user1.
    

def remove_friend1():
    snake.direction = 'Right'
    print("You pressed the right key!")
    

def get_userinfo1():
    snake.direction = 'Up'


mai.onkeypress(add_friend, 'q')
mai.onkeypress(add_post, 'w')
mai.onkeypress(remove_friend, 'e')
mai.onkeypress(get_userinfo, 'r')

user1 = User("Mai","mai@gmail.com","Omer")
#q
user1.add_friend()
#w
user1.add_post()
#e
user1.remove_friend()
#r
user1.get_userinfo()

user2 = ("Noa","Noa@gmail.com","123noa123")
user2.add_friend()
user2.add_post()
user2.remove_friend()
user2.get_userinfo()

