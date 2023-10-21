books = {}
books["0545139708"] = {"title": "Harry Potter and the Deathly Hallows", "author": "J. K. Rowling", "price": 12.99, "quantity": 16}
books["052543576X"] = {"title": "Killing Commendatore", "author": "Haruki Murakami", "price": 18.29, "quantity": 35}


def add_book(isbn, title, author, price, quantity):
    if isbn in books:
        print("Error! A book with this ISBN already exists!")
    else:
        books[isbn] = {"title": title, "author": author, "price": price, "quantity": quantity}

def search_isbn(isbn):
    if isbn in books:
        print(books[isbn])
    else:
        print("Error! Book not found!")

def search_title_author(str):
    for book in books:
        if str in books[book]["title"] or str in books[book]["author"]:
            print(books[book])
            return
    print("No books match the search string!")

def list_books():
    count = 1
    if books == {}:
        print("Error! The booklist is empty!")
    else:
        for book in books:
            print(f"Book {count}")
            print(f"Title: {books[book]['title']}")
            print(f"Author: {books[book]['author']}")
            print(f"ISBN: {book}")
            print(f"Quantity: {books[book]['quantity']}")
            count += 1


def delete_book(isbn):
    if isbn not in books:
        print("Error! A book with this ISBN doesn't exist!")
    else:
        del books[isbn]
        print("Book deleted successfully!")

add_book("12345678", "cool book", "Alexey Gorlovich", 99.99, 3)

print("Testing search by ISBN:")
search_isbn("12345678") # cool book
search_isbn("12345") # error
print()

print("Testing search by title/author:")
search_title_author("Potter") # book found
search_title_author("Murakami") # book found
search_title_author("King") # no matches
print()

print("Testing listing all the books:")
print("A list of all available books:")
list_books()
print()

delete_book("12345678")
delete_book("0545139708")
delete_book("052543576X")
list_books() # testing with an empty booklist, should give an error




