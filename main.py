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
    book_name = input("Enter a Book: ")
    priority = input("Enter the book's priority: ")
    book = {
        "name": book_name,
        "priority": priority
    }
    books.append(book)

show_books(book)

save_books(book)