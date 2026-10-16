name = input("Please enter your name: ")
print(f"Welcome, {name}.")

books = []
count = int(input("How many books do you want to add? "))
for i in range(count):
    book = input("Enter a Book: ")
    books.append(book)
    
for i in books:
    print("Book Title: ", i)