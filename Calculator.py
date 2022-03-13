class Calculator:
	def __init__(self, list_numbers=None):
		self.number_list=list_numbers
		self.answer=None
		
	def addition(self, first, second, third=None):
		if third:
			try:
				self.answer= int(first) + int(second) + int(third)
			except ValueError:
				pass
		else:
			try:
				self.answer= int(first) + int(second)
			except ValueError:
				pass
			
	def substraction(self, first, second, third=None):
		if third:
			try:
				self.answer= int(first) - int(second) - int(third)
			except ValueError:
				pass
		else:
			try:
				self.answer= int(first) - int(second)
			except ValueError:
				pass
			
	def division(self, first, second, third=None):
		if third:
			try:
				self.answer= int(first) / int(second) / int(third)
			except ValueError:
				pass
		else:
			try:
				self.answer= int(first) / int(second)
			except ValueError:
				pass
			
	def multiplication(self, first, second, third=None):
		if third:
			try:
				self.answer= int(first) * int(second) * int(third)
			except ValueError:
				pass
		else:
			try:
				self.answer= int(first) * int(second)
			except ValueError:
				pass
			
	def square(self, number):
		try:
			self.answer=int(number) * int(number)
		except ValueError:
			pass
			
	def exponential(self, first, second):
		try:
			self.answer=int(first)** int(second)
		except ValueError:
			pass
			
		
		
cal=Calculator()
cal.addition(2,3,4)
print(cal.answer)

cal.substraction(7,6)
print(cal.answer)

cal.division(9,2,2)
print(cal.answer)

cal.multiplication(2,2,4)
print(cal.answer)

cal.square(6)
print(cal.answer)

cal.exponential(2,3)
print(cal.answer)

# r)

# cal.multiplication(2,2,4)
# print(cal.answer)

# cal.square(6)
# print(cal.answer)

# cal.exponential(2,3)
# print(cal.answer)

# r)







cal.multiplication(2,2,4)
print(cal.answer)

cal.square(6)
print(cal.answer)

cal.exponential(2,3)
print(cal.answer)

# r)

# cal.multiplication(2,2,4)
# print(cal.answer)

# cal.square(6)
# print(cal.answer)

# cal.exponential(2,3)
# print(cal.answer)

# r)

