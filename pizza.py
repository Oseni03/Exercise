def make_pizza(name, *toppings):

 """Summarize the pizza we are about to make."""

 print(f"\nMaking a pizza for {name} with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")
 
name = input("What is your name: ")
toppings =[]
while True:
	tops = input("Enter a topping: ")
	if tops == "q":
		break
	toppings.append(tops)

make_pizza(name, *toppings)