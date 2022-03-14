def car_info(manufacturer, model, **car_details):
	car_details["Manufacturer_name"]= manufacturer
	car_details["Model_name"]=model
	return car_details
	
# manufacturer= input("Enter the manufacturer name: ")
# model=input("Enter the model name: ")
# car_details={}

# print("Enter 'q' to quit")
# while True:
# 	A_info = input("Enter an additional info: ")
# 	if A_info=="q":
# 		break

# 	car_details[A_info] = input("Enter the detail: ")

# car_infos = car_info(manufacturer, model, **car_details)

# print("\nThe car details include:")
# for info, detail in car_infos.items():
#  print(f"{info} - {detail.title()}")



def choice_profiling():
 responses = {}
 """ This fill up a dictionary with a user's name and his/her choice of mountain 😁"""

# Set a flag to indicate that polling is active.

 polling_active = True

 while polling_active:
 # Prompt for the person's name and response.
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday? ")
 
 # Store the response in the dictionary.
  responses[name] = response
 
 # Find out if anyone elbse is going to take the poll.
  repeat = input("Would you like to let another person respond? (yes/ no) ")
 
  if repeat == 'no':
   polling_active = False
 
# Polling is complete. Show the results.
 print("\n--- Poll Results ---")

 for name, response in responses.items():
  print(f"{name} would like to climb {response}.")
  
# choice_profiling()


def people_profiling(username, first_name, last_name, age, city):
	people = {}
	
	people[username] = {
		"first_name":first_name,
		"last_name":last_name,
		"age":age,
		"city":city,
	}
	for username, user_info in people.items():
		print(username.title())
		
		full_name = f"{user_info['first_name']} {user_info['last_name']}"
		print(f"\n{full_name.title()} is {user_info['age']}yrs old,\nlocated at {user_info['city'].title()}")
		return full_name.title()

# people_profiling()


def build_person(first_name, last_name, age=None):
	
 """Return a dictionary of information about a person."""
 
 person = {'first': first_name, 'last': last_name}
 if age:
  person['age'] = age
 return person


# first_name= input("Enter your first name: ")
# last_name= input("Enter your last name: ")
# age=input("What is your age: ")

# if age:
# 	pass
# else:
# 	pass

# profile = build_person(first_name, last_name, age)

# for datas in profile.values():
# 	if age=="":
# 	 print(f"\nSo your names is {first_name} {last_name}")
# 	else:
# 	 print(f"\nSo your names are {first_name} {last_name}, of age {age}")

# print(profile)

