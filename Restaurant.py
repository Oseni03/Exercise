class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
		
	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} is {self.cuisine_type} restaurant")
		
	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is Now Open!!")
		
	def set_number_served(self, number_served):
		self.number_served=number_served
		
	def increment_number_served(self, served):
		self.number_served+=served


class IceCreamStand(Restaurant):
	
	def __init__(self, restaurant_name, cuisine_type):
		
		super().__init__(restaurant_name, cuisine_type)
		
		self.flavors=["strawberry", "cream", "chocolate", "vanilla"]
	
	def display_flavors(self):
		print("\nThese are the list of flavors available")
		for items in self.flavors:
			print(f"-{items}")
			
	def update_flavors(self, flavor):
		self.flavors.append(flavor)
		
	def reset_flavors(self):
		self.flavors=[]
	
		
name=input("Enter your restaurant name: ")
cuisine_type=input("Enter your restaurant cuisine type: ")

restaurant=Restaurant(name, cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)

restaurant.set_number_served(27)

print(restaurant.number_served)


ice_cream=IceCreamStand(name, cuisine_type)
ice_cream.display_flavors()

print("\nEnter 'quit' to exit")
while True:
	flavor=input("Enter a new flavor: ")
	if flavor=="quit":
		break
	else:
		ice_cream.update_flavors(flavor)
		
ice_cream.display_flavors()

ice_cream.reset_flavors()
ice_cream.display_flavors()



# est.open_restaurant()