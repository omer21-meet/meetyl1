
class User():
	def __init__ (self,name,email,password,friend_list=[],posts=[]):
		self.name= name
		self.email = email
		self.password = password
		self.friend_list = friend_list
		self.posts = posts
	def add_friend(self):
		email = input("Enter your friend's email")
		friend_list.append(email)
		print(self.name + " has added " + email + " as a friend")

	def remove_friend(self):
		email = input("Enter your friend's email")
		friend_list.remove(email)
		print(self.name + " has removed " + email)
	def add_post(self):
		text = input("give a name to your post")
		posts.appned(text)
		print(self.name + " has posted " + text)


user1 = User("Mai","mai@gmail.com","Omer")
user1.add_friend()
user1.add_post()
