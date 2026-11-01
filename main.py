from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Please enter your name: ")
print(f"Welcome, {name}.")

admin_mode = input("Do you want to enter admin mode (yes/no)? ")
if admin_mode == "yes":
    admin_password = input("Enter admin password: ")
    
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated.")
    else:
        print("Wrong Password")

books = load_books()
count = int(input("How many books do you want to add? "))
for i in range(count):
    book = input("Enter a Book: ")
    books.append(book)

show_books(books)

save_books(books)