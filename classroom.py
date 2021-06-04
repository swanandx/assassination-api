from json import load
from random import choice

class Assasination:
	def __init__(self):
		with open("quotes.json","r") as read_me:
			self.quotes = load(read_me)

	def get_random_quote(self):
		charecter, quote = choice(list(self.quotes.items()))
		result = {charecter : choice(quote)}
		return result
	def get_5_quotes(self):
		result = {}
		for _ in range(5):
			charecter, quote = choice(list(self.quotes.items()))
			res = {charecter : choice(quote)}
			result.update(res)	
		return result
	def list_characters(self):
		result = {"characters" : list(self.quotes.keys())}
		return result
	def get_quote_by_name(self,name):
		try:
			result = {name : choice(self.quotes[name])}
			return result
		except KeyError:
			result = {name : "Character not found."}
			return result

if __name__ == '__main__':
	a = Assasination()
	print(a.get_random_quote())
	print(a.get_5_quotes())
	print(a.list_characters())
	print(a.get_quote_by_name('koro-sensei'))
	print(a.get_quote_by_name('swanand'))



