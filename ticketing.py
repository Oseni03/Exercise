def ticketing():
	print("Enter 'quit' to exit")
	while True:
		age =input("What is your age: ")
		if age =="quit":
			break
		age=int(age)
		
		if age<3:
			print("The cost of your ticket is free")
		elif age<=12:
			print("The cost of your ticket is $10")
		elif age>12:
			print("The cost of your ticket is $15")

ticketing()