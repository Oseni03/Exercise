import json

class User:
	def __init__(self):
		self.user_name= ""
		self.first_name=""
		self.last_name=""
		self.age=""
		self.city=""
		self.middle_name=""
		self.full_name=""

		self.login_attempt=0
		
	def sign_up(self):
		username = input("Enter your username: ")
		first=input("Enter your first name: ")
		last=input("Enter your last name: ")
		middle=input("Enter your middle name: ")
		age= input("Enter your age: ")
		city=input("Enter your city: ")
		
		self.user_name=username
		self.first_name=first
		self.last_name=last
		self.age=age
		self.city=city
		if middle:
			self.middle_name=middle
			self.full_name=f"{self.first_name} {self.middle_name} {self.last_name}"
		else:
			self.full_name=f"{self.first_name} {self.last_name}"
			
		# self.save_users_info()
			
	def retrieve_data(self):
		
		"""Get stored username if available."""
		filename = 'users_info.json'
		try:
			with open(filename) as f:
				infos = json.load(f)
		except FileNotFoundError:
			return None
		else:
			for username, details in infos.items():
				return username
				
				for info in details.values():
					return info
					
	def describe_user(self):
		if self.full_name:
			print(f"{self.full_name.title()} info include:")
			print(f"Age: {self.age} \nCity: {self.city.title()}")
		else:
			pass
			
	def greet_user(self):
		try:
			file="users_info.json"
			with open(file, "r") as book:
				users_info=json.load(book)
			for name in users_info.keys():
				print(f"Welcome back {name.title()}")
		except FileNotFoundError:
			self.sign_up()

	def increment_login_attempt(self):
		self.login_attempt+=1
		
	def reset_login_attempts(self):
		self.login_attempt=0
		
	def save_users_info(self):
		file="users_info.txt"
		infos ={}
		infos[self.user_name.title()]={
			"full-name":self.full_name.title(),
			"first-name":self.first_name.title(),
			"last-name":self.last_name.title(),
			"age":self.age,
			"city":self.city,
		}
		# with open(file, "w") as book:
		# 	json.dump(infos, book)
		for name, details in infos.items():
			with open(file, "a") as book:
				book.write(f"{name.title()}:{details}")
			
class Privileges:
	def __init__(self):
		self.privileges=[
			"Can post",
			"Can delete post",
			"Can edit post",
			"Can ban user",
			]
			
	def show_privileges(self):
		print("An admin:")
		for privilege in self.privileges:
			print(f"- {privilege}")
			
			
class Admin(User):
	def __init__(self):
		
		super().__init__()
		self.privileges=Privileges()
		
	def delete_user(self, name):
		try:
			file="users_info.json"
			with open(file, "r") as book:
				users_info=json.load(book)
			if users_info:
				for username, details in users_info.items():
					if username==name:
						users_info.keys().remove(name)
					print(f"{name.title()} profile deleted")
		except FileNotFoundError:
			print("User does not exist!")
		
		
		
my_self=User()
my_self.sign_up()
my_self.greet_user()
my_self.describe_user()
my_self.save_users_info()

# my_self.increment_login_attempt()
# my_self.increment_login_attempt()
# my_self.increment_login_attempt()

# print(my_self.login_attempt)

# admin=Admin()

# # admin.privileges.show_privileges()
# admin.save_users_info()
# admin.retrieve_data()

# admin.delete_user("Oseni")


# # ide")


# # ast_name=last,
# # # 	age=age,
# # 	city=city,
# # 	middle_name=middle
# # )

# # admin.privileges.show_privileges()
# # admin.save_users_info()
# # admin.retrieve_data()

# # # es()


# # # .describe_user()
# # # my_self.greet_user()
# # # # if marital_status:
# # # # 	my_self.update_marital_status(marital_status)
	
# # # my_self.marital_status()
# # # # )

# # # # 	my_self.marital_status()
# # # # tus()
# # # s()
# # # )

# # lf.marital_status()
# # # # tus()
# # # s()
# # # )

# # )
# # # )


# # # my_self.greet_user()
# # # # if marital_status:
# # # # 	my_self.update_marital_status(marital_status)
	
# # # my_self.marital_status()
# # # # )

# # # # 	my_self.marital_status()
# # # # tus()
# # # s()
# # # )

# # lf.marital_status()
# # # # tus()
# # # s()
# # # )

# # )
# # # )

# )
# # # )

# # )

# )
# # # )

