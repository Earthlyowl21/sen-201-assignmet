# library.py

class Book:
	def _init_(self, isbn, title, author, quantity):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.quantity = quantity

class Member:
	def _init_(self, id, name, email):
		self.id = id
		self.name = name
		self.email = email

class Borrowing:
	def _init_(self, id, isbn, member_id, borrow_date, return_date=None):
		self.id = id
		self.isbn = isbn
		self.member_id = member_id
		self.borrow_date = borrow_date
		self.return_date = return_date

class Library:
	def _init_(self):
		self.books = []
		self.members = []
		self.borrowings = []

	def add_book(self, book):
		self.books.append(book)

	def borrow_book(self, isbn, member_id):
		# logic to borrow book
		pass

# main.py
from library import Book, Member, Borrowing, Library

lib = Library()
book1 = Book("12345", "Python Basics", "John Doe", 5)
lib.add_book(book1)
[10:24 pm, 21/01/2026] Sukuna21: # library.py (same as above)

# main.py
from library import Book, Member, Borrowing, Library

def main():
	lib = Library()
	while True:
		print("1. Add book")
		print("2. Borrow book")
		choice = input("Choose: ")
		if choice == "1":
			isbn = input("ISBN: ")
			title = input("Title: ")
			author = input("Author: ")
			quantity = int(input("Quantity: "))
			book = Book(isbn, title, author, quantity)
			lib.add_book(book)
		# add more logic

if _name_ == "_main_":
	main()