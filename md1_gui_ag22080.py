'''
Uzdevums: Izstrādāt grāmatnīcas inventāra pārvaldības sistēmu Python programmēšanas valodā.

Prasības:

    Datu struktūra:

    Inventāra saraksts tiek glabāts kā Python vārdnīca.
    Lai nebūtu dati jāievada katru reizi no jauna, programmā var "iekodēt" sākotnējo grāmatu sarakstu.
    Par katru grāmatu tiek glabāta vismaz šāda informācija: title, author, ISBN, price un quantity in stock.
    Katras grāmatas informācija tiek glabāta atsevišķā vārdnīcā
    Inventāra saraksta vārdnīcas atslēgas ir ISBN kodi un tās vērtības ir vārdnīcas ar informāciju par grāmatu.

    Funkcionalitāte:

    Pievienot grāmatu:
    Lietotājam ir jādod iespēja sarakstam pievienot jaunu grāmatu.
    Pievienojot grāmatu, pārliecinieties, ka tās ISBN numurs ir unikāls. Ja šāds ISBN numurs jau ir sarakstā, attēlot kļūdas ziņojumu.

    Meklēšana pēc ISBN:
    Lietotājiem ir jāļauj meklēt grāmatu pēc tās ISBN numura.
    Ja grāmata tika atrasta, attēlot informāciju par to.
    Ja grāmata netika atrasta, attēlot kļūdas ziņojumu.

    Meklēšana pēc nosaukuma vai autora:
    Ļaut lietotājiem meklēt grāmatu pēc vārda tās nosaukuma vai autora laukā. Rezultātā attēlot sarakstu ar grāmatām, kas atbilst meklēšanas kritērijiem.

    Grāmatu saraksts:
    Attēlot sarakstu ar visām grāmatām, par katru grāmatu parādot šādu informāciju: title, author, ISBN, quantity in stock.

    Dzēst grāmatu:
    Izdzēst no saraksta grāmatu ar doto ISBN numuru.
    Informēt lietotāju, ka grāmata tika veiksmīgi izdzēsta, vai arī, ka ISBN numurs netika atrasts.
'''

import tkinter as tk
from tkinter import messagebox
import itertools
import math
print(f"Using tkinter version: {tk.TkVersion}")

class App:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1000x650")
        self.win.title("Bookkeeping system")
        self.main_menu()


    def main_menu(self):
        for i in self.win.winfo_children():
            i.destroy()

        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(anchor="center")

        self.title = tk.Label(self.main_frame, text="BOOKKEEPING SYSTEM", font=TITLE_FONT)
        self.title.grid(row=0, column=0, pady=50)

        # Creating the main menu buttons
        self.view_books_btn = tk.Button(self.main_frame, text="View all available books", font=BUTTON_FONT, command=lambda: self.view_books(0), cursor="hand2")
        self.search_isbn_btn = tk.Button(self.main_frame, text="Search by ISBN", font=BUTTON_FONT, cursor="hand2")
        self.search_title_btn = tk.Button(self.main_frame, text="Search by author or title", font=BUTTON_FONT, cursor="hand2")
        self.add_book_btn = tk.Button(self.main_frame, text="Add a new book", font=BUTTON_FONT, command=self.add_book, cursor="hand2")
        self.delete_book_btn = tk.Button(self.main_frame, text="Delete a book", font=BUTTON_FONT, command=self.delete_book, cursor="hand2")

        self.view_books_btn.grid(row=1, column=0, pady=20)
        self.search_isbn_btn.grid(row=2, column=0, pady=10)
        self.search_title_btn.grid(row=3, column=0, pady=10)
        self.add_book_btn.grid(row=4, column=0, pady=10)
        self.delete_book_btn.grid(row=5, column=0, pady=10)


    def view_books(self, page):
        for i in self.win.winfo_children():
            i.destroy()

        self.top_row = tk.Frame(self.win)
        self.top_row.pack(anchor="center", pady=30)
        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(anchor="center", pady=20)


        # Table header
        self.isbn = tk.Label(self.main_frame, text="ISBN", font=TABLE_HEADER_FONT)
        self.title = tk.Label(self.main_frame, text="Title", font=TABLE_HEADER_FONT)
        self.author = tk.Label(self.main_frame, text="Author", font=TABLE_HEADER_FONT)
        self.quantity = tk.Label(self.main_frame, text="Quantity in stock", font=TABLE_HEADER_FONT)

        self.isbn.grid(row=1, column=0, padx=10)
        self.title.grid(row=1, column=1, padx=10)
        self.author.grid(row=1, column=2, padx=10)
        self.quantity.grid(row=1, column=3, padx=10)


        # Page number and buttons for switching pages
        self.go_back = tk.Button(self.top_row, text="Return to main menu", font=BUTTON_FONT, command=self.main_menu, cursor="hand2")
        self.go_back.grid(row=0, column=0, padx=10)
        self.page_number = tk.Label(self.top_row, text=f"Page {page + 1} of {math.ceil(len(books) / 18)}", font=TABLE_HEADER_FONT)
        self.page_number.grid(row=0, column=1, padx=10)
        self.switch_pages = tk.Frame(self.top_row)
        self.switch_pages.grid(row=0, column=2, padx=10)


        first_page = page == 0
        last_page = page == math.ceil(len(books) / 18) - 1

        self.previous_page = tk.Button(self.switch_pages, text="<", font=TABLE_HEADER_FONT, command=lambda: self.view_books(page - 1), cursor="hand2" if not first_page else "arrow", state="normal" if not first_page else "disabled")
        self.previous_page.grid(row=0, column=0, padx=10)
        self.next_page = tk.Button(self.switch_pages, text=">", font=TABLE_HEADER_FONT, command=lambda: self.view_books(page + 1), cursor="hand2" if not last_page else "arrow", state="normal" if not last_page else "disabled")
        self.next_page.grid(row=0, column=1, padx=10)

        i = 2
        start, end = page * 18, page * 18 + 18 # Displaying 18 books per page

        for book in dict(itertools.islice(books.items(), start, end)):
            self.book_isbn = tk.Label(self.main_frame, text=book, font=TABLE_FONT)
            self.book_title = tk.Label(self.main_frame, text=books[book]["title"] if len(books[book]["title"]) < 30 else books[book]["title"][:27] + "...", font=TABLE_FONT)
            self.book_author = tk.Label(self.main_frame, text=books[book]["author"], font=TABLE_FONT)
            self.book_quantity = tk.Label(self.main_frame, text=books[book]["quantity"], font=TABLE_FONT)

            self.book_isbn.grid(row=i, column=0)
            self.book_title.grid(row=i, column=1, padx=10)
            self.book_author.grid(row=i, column=2, padx=10)
            self.book_quantity.grid(row=i, column=3)

            i += 1


    def add_book(self):
        for i in self.win.winfo_children():
            i.destroy()

        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(anchor="center", pady=20)

        self.go_back = tk.Button(self.main_frame, text="Return to main menu", font=BUTTON_FONT, command=self.main_menu, cursor="hand2")
        self.go_back.grid(row=0, column=0, columnspan=2, pady=30)

        self.form_fields = {}
        self.fields = ("isbn", "title", "author", "price", "quantity")

        for i in range(len(self.fields)):
            label = tk.Label(self.main_frame, text=self.fields[i].capitalize() if self.fields[i] != "isbn" else self.fields[i].upper(), font=BUTTON_FONT)
            label.grid(row=i+1, column=0)
            self.form_fields[self.fields[i]] = tk.Entry(self.main_frame, font=BUTTON_FONT)
            self.form_fields[self.fields[i]].grid(row=i+1, column=1)

        def confirm():
            # Validate the form
            for field in self.form_fields:
                if self.form_fields[field].get() == "":
                    messagebox.showerror("Error", "Please fill out all fields!")
                    return

            if self.form_fields["isbn"].get() in books:
                messagebox.showerror("Error", "A book with this ISBN already exists!")
                return
            
            try:
                float(self.form_fields["price"].get())
            except ValueError:
                messagebox.showerror("Error", "The price should be a number!")
                return
            else:  
                if float(self.form_fields["price"].get()) < 0:
                    messagebox.showerror("Error", "The price cannot be negative!")
                    return

            try:
                int(self.form_fields["quantity"].get())
            except ValueError:
                messagebox.showerror("Error", "The quantity must be an integer!")
                return
            else:     
                if int(self.form_fields["quantity"].get()) < 0:
                    messagebox.showerror("Error", "The quantity cannot be negative!")
                    return
                
            books[self.form_fields["isbn"].get()] = {"title": self.form_fields["title"].get(), "author": self.form_fields["author"].get(), "price": self.form_fields["price"].get(), "quantity": self.form_fields["quantity"].get()}
            messagebox.showinfo("Success", "Book added successfully!")
            self.add_book()
        
        self.confirm = tk.Button(self.main_frame, text="Confirm", font=BUTTON_FONT, command=confirm)
        self.confirm.grid(row=6, column=0, columnspan=2, pady=20)


    def delete_book(self):
        for i in self.win.winfo_children():
            i.destroy()

        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(anchor="center", pady=20)

        self.go_back = tk.Button(self.main_frame, text="Return to main menu", font=BUTTON_FONT, command=self.main_menu, cursor="hand2")
        self.go_back.grid(row=0, column=0, columnspan=2, pady=30)

        self.isbn = tk.Label(self.main_frame, text="ISBN", font=BUTTON_FONT)
        self.isbn.grid(row=1, column=0, padx=10)
        self.isbn_input = tk.Entry(self.main_frame, font=BUTTON_FONT)
        self.isbn_input.grid(row=1, column=1, padx=10)

        def confirm():
            if self.isbn_input.get() == "":
                messagebox.showerror("Error!", "Please enter an ISBN number")
                return
            
            if self.isbn_input.get() not in books:
                messagebox.showerror("Error!", "Book not found")
                return
            
            del books[self.isbn_input.get()]
            messagebox.showinfo("Success", "Book deleted successfully!")
            self.delete_book()

        self.confirm = tk.Button(self.main_frame, text="Confirm", font=BUTTON_FONT, command=confirm)
        self.confirm.grid(row=2, column=0, columnspan=2, pady=20)

        
        

TITLE_FONT = ("Arial", 24)
BUTTON_FONT = ("Arial", 20)
TABLE_HEADER_FONT = ("Arial", 20, "bold")
TABLE_FONT = ("Arial", 12)

books = {
    "978006112008401": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 10.99, "quantity": 25},
    "978014240733202": {"title": "The Outsiders", "author": "S.E. Hinton", "price": 8.99, "quantity": 30},
    "978073933491703": {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "price": 12.99, "quantity": 20},
    "978006085052404": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 9.99, "quantity": 15},
    "978031601584405": {"title": "The Hunger Games", "author": "Suzanne Collins", "price": 11.99, "quantity": 22},
    "978037453355706": {"title": "The Road", "author": "Cormac McCarthy", "price": 14.99, "quantity": 18},
    "978006222781807": {"title": "Divergent", "author": "Veronica Roth", "price": 10.49, "quantity": 28},
    "978140003271608": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 8.49, "quantity": 10},
    "978054792822709": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 11.99, "quantity": 25},
    "978044631078910": {"title": "1984", "author": "George Orwell", "price": 9.49, "quantity": 16},
    "978145167331911": {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "price": 12.99, "quantity": 12},
    "978030788743612": {"title": "The Help", "author": "Kathryn Stockett", "price": 10.99, "quantity": 20},
    "978006662076713": {"title": "The Da Vinci Code", "author": "Dan Brown", "price": 11.49, "quantity": 17},
    "978006250217614": {"title": "The Alchemist", "author": "Paulo Coelho", "price": 8.99, "quantity": 23},
    "978014198079415": {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 7.99, "quantity": 14},
    "978140007917716": {"title": "The Kite Runner", "author": "Khaled Hosseini", "price": 10.99, "quantity": 21},
    "978006447277217": {"title": "The Giver", "author": "Lois Lowry", "price": 7.49, "quantity": 32},
    "978038534994418": {"title": "The Goldfinch", "author": "Donna Tartt", "price": 13.49, "quantity": 19},
    "978014311643519": {"title": "Eat, Pray, Love", "author": "Elizabeth Gilbert", "price": 9.99, "quantity": 27},
    "978014044929020": {"title": "Moby-Dick", "author": "Herman Melville", "price": 10.49, "quantity": 18},
    "978145167331021": {"title": "War and Peace", "author": "Leo Tolstoy", "price": 15.99, "quantity": 30},
    "978031601584222": {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "price": 11.49, "quantity": 15},
    "978044631078223": {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "price": 14.99, "quantity": 20},
    "978006222781224": {"title": "Brave New World", "author": "Aldous Huxley", "price": 9.99, "quantity": 18},
    "978037453355225": {"title": "The Odyssey", "author": "Homer", "price": 10.99, "quantity": 25},
    "978006112008226": {"title": "The Divine Comedy", "author": "Dante Alighieri", "price": 12.99, "quantity": 22},
    "978140003271227": {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "price": 11.99, "quantity": 28},
    "978054792822228": {"title": "The Road Not Taken", "author": "Robert Frost", "price": 7.99, "quantity": 14},
    "978006662076229": {"title": "The Metamorphosis", "author": "Franz Kafka", "price": 8.49, "quantity": 21},
    "978006250217230": {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "price": 10.49, "quantity": 19},
    "978014198079231": {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "price": 9.99, "quantity": 20},
    "978030788743232": {"title": "The Iliad", "author": "Homer", "price": 11.49, "quantity": 15},
    "978006447277233": {"title": "The Odyssey", "author": "Homer", "price": 9.49, "quantity": 23},
    "978038534994234": {"title": "A Tale of Two Cities", "author": "Charles Dickens", "price": 12.99, "quantity": 27},
    "978014311643235": {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "price": 10.99, "quantity": 22},
    "978014044929236": {"title": "Les Misérables", "author": "Victor Hugo", "price": 13.49, "quantity": 16},
    "978145167331237": {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "price": 8.49, "quantity": 30},
    "978031601584338": {"title": "The Martian", "author": "Andy Weir", "price": 10.99, "quantity": 18},
    "978044631078339": {"title": "Frankenstein", "author": "Mary Shelley", "price": 11.99, "quantity": 25},
    "978006222781340": {"title": "Dracula", "author": "Bram Stoker", "price": 9.99, "quantity": 14},
    "978037453355341": {"title": "The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle", "price": 12.99, "quantity": 20}
}


win = tk.Tk()
App(win)
win.mainloop()

