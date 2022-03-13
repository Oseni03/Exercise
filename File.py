class File:
	def __init__(self, file_name):
		self.file_name=file_name
		self.contents=""
		self.contents_strip=""
		
	def read_file(self):
		try:
			with open(self.file_name) as file_object:
				self.contents=file_object.read()
		except FileNotFoundError:
			print(f"Sorry, the file {self.file_name} does not exist.")
			
	def word_search(self, search_digits):
		if search_digits in self.contents:
			print(f"{search_digits} is found!")
		else:
			print(f"{search_digits} not found")
			
	def millions_digits(self):
		with open(self.file_name) as f:
			file= f.readlines()
		for line in file:
			if len(line)>50000:
				print(f"{line[:30]}...")
			elif len(line)>1000000:
				print(f"{line[:50]}...")
			else:
				print(line)
				
				
class Replace():
	def __init__(self, file_name):
		self.replace_filename=file_name
		self.r_contents=""
		
	def read_r_file(self):
		try:
			with open(self.replace_filename) as f:
				self.r_contents=f.read()
		except FileNotFoundError:
			print(f"Sorry, the file {self.replace_filename} does not exist.")
		
		
	def replace_word(self, to_replace="Python", replace_with="C"):
		self.r_contents=self.r_contents.replace(to_replace, replace_with)
		
		
class Text(File):
	def __init__(self, file_name):
		super().__init__(file_name)
		self.replace=Replace(self.file_name)
		
	def words_count(self):
		words = self.contents.split()
		num_words = len(words)
		print(f"The file {self.file_name} has about {num_words} words.")
		




filename= "pi-digits.txt"
filename_2="learning_python.txt"


text=Text(filename_2)
# text.millions_digits()
text.read_file()
print(text.contents)

text.word_search("Python")
text.words_count()

text.replace.read_r_file()
print(text.replace.replace_word())
print(text.replace.r_contents)



# rst million digits of pi!")
# else:
#  print("Your birthday does not appear in the first million digits of pi.")


# text=Text(filename_2)
# # text.millions_digits()
# text.read_file()
# print(text.contents)

# text.word_search("Python")
# text.words_count()

# text.replace.read_r_file()
# print(text.replace.replace_word())
# print(text.replace.r_contents)


# digits of pi.")


# ip())ip())

# ip())tents)


 #digits of pi.")


# ip())ip())

# ip())
# ip())ip())

# ip())()))p())# print(text.replace.r_contents)


# digits of pi.")


# ip())ip())

# ip())tents)


 #digits of pi.")


# ip())ip())

# ip())
# ip())ip())

# ip())()))p())