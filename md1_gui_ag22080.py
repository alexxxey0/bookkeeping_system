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
        self.win.geometry("1000x600")
        self.win.title("Bookkeeping system")
        self.main_menu()

    def main_menu(self):
        for i in self.win.winfo_children():
            i.destroy()

        self.win.grid_columnconfigure((0, 1), weight=1)
        self.title = tk.Label(self.win, text="BOOKKEEPING SYSTEM", font=TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2, pady=50)

        # Creating the main menu buttons
        self.view_books_btn = tk.Button(self.win, text="View all available books", font=BUTTON_FONT, command=lambda: self.view_books(0), cursor="hand2")
        self.search_isbn_btn = tk.Button(self.win, text="Search by ISBN", font=BUTTON_FONT, cursor="hand2")
        self.search_title_btn = tk.Button(self.win, text="Search by author or title", font=BUTTON_FONT, cursor="hand2")
        self.add_book_btn = tk.Button(self.win, text="Add a new book", font=BUTTON_FONT, command=self.add_book, cursor="hand2")
        self.delete_book_btn = tk.Button(self.win, text="Delete a book", font=BUTTON_FONT, cursor="hand2")

        self.view_books_btn.grid(row=1, column=0, columnspan=2, pady=20)
        self.search_isbn_btn.grid(row=2, column=0, pady=10)
        self.search_title_btn.grid(row=2, column=1, pady=10)
        self.add_book_btn.grid(row=3, column=0, pady=10)
        self.delete_book_btn.grid(row=3, column=1, pady=10)

    def view_books(self, page):
        for i in self.win.winfo_children():
            i.destroy()

        #self.win.grid_columnconfigure((0, 1), weight=1)

        # Table header
        self.go_back = tk.Button(self.win, text="Return to main menu", font=BUTTON_FONT, command=self.main_menu, cursor="hand2")
        self.isbn = tk.Label(self.win, text="ISBN", font=TABLE_HEADER_FONT)
        self.title = tk.Label(self.win, text="Title", font=TABLE_HEADER_FONT)
        self.author = tk.Label(self.win, text="Author", font=TABLE_HEADER_FONT)
        self.quantity = tk.Label(self.win, text="Quantity in stock", font=TABLE_HEADER_FONT)

        self.go_back.grid(row=0, column=0, pady=30)
        self.isbn.grid(row=1, column=0, padx=10)
        self.title.grid(row=1, column=1, padx=10)
        self.author.grid(row=1, column=2, padx=10)
        self.quantity.grid(row=1, column=3, padx=10)


        # Page number and buttons for switching pages
        self.switch_pages = tk.Frame(self.win)
        self.switch_pages.grid(row=0, column=2, columnspan=2)


        first_page = page == 0
        last_page = page == math.ceil(len(books) / 18) - 1

        self.page_number = tk.Label(self.win, text=f"Page {page + 1} of {math.ceil(len(books) / 18)}", font=TABLE_HEADER_FONT)
        self.page_number.grid(row=0, column=1)
        self.previous_page = tk.Button(self.switch_pages, text="<", font=TABLE_HEADER_FONT, command=lambda: self.view_books(page - 1), cursor="hand2" if not first_page else "arrow", state="normal" if not first_page else "disabled")
        self.previous_page.grid(row=0, column=0, padx=10)
        self.next_page = tk.Button(self.switch_pages, text=">", font=TABLE_HEADER_FONT, command=lambda: self.view_books(page + 1), cursor="hand2" if not last_page else "arrow", state="normal" if not last_page else "disabled")
        self.next_page.grid(row=0, column=1, padx=10)

        i = 2
        start, end = page * 18, page * 18 + 18

        # Displaying 18 books per page
        for book in dict(itertools.islice(books.items(), start, end)):
            self.book_isbn = tk.Label(self.win, text=book, font=TABLE_FONT)
            self.book_title = tk.Label(self.win, text=books[book]["title"] if len(books[book]["title"]) < 30 else books[book]["title"][:30] + "...", font=TABLE_FONT)
            self.book_author = tk.Label(self.win, text=books[book]["author"], font=TABLE_FONT)
            self.book_quantity = tk.Label(self.win, text=books[book]["quantity"], font=TABLE_FONT)

            self.book_isbn.grid(row=i, column=0)
            self.book_title.grid(row=i, column=1)
            self.book_author.grid(row=i, column=2)
            self.book_quantity.grid(row=i, column=3)

            i += 1

    def add_book(self):
        for i in self.win.winfo_children():
            i.destroy()

        self.go_back = tk.Button(self.win, text="Return to main menu", font=BUTTON_FONT, command=self.main_menu, cursor="hand2")
        self.go_back.grid(row=0, column=0, pady=30)

        self.form_fields = {}
        self.fields = ("isbn", "title", "author", "price", "quantity")

        for i in range(len(self.fields)):
            label = tk.Label(self.win, text=self.fields[i].capitalize() if self.fields[i] != "isbn" else self.fields[i].upper(), font=BUTTON_FONT)
            label.grid(row=i+1, column=0)
            self.form_fields[self.fields[i]] = tk.Entry(self.win, font=BUTTON_FONT)
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
        
        self.confirm = tk.Button(self.win, text="Confirm", font=BUTTON_FONT, command=confirm)
        self.confirm.grid(row=6, column=0, columnspan=2)

        

TITLE_FONT = ("Arial", 24)
BUTTON_FONT = ("Arial", 20)
TABLE_HEADER_FONT = ("Arial", 20, "bold")
TABLE_FONT = ("Arial", 12)

books = {}
books["0545139708"] = {"title": "Harry Potter and the Deathly Hallows", "author": "J. K. Rowling", "price": 12.99, "quantity": 16}
books["052543576X"] = {"title": "Killing Commendatore", "author": "Haruki Murakami", "price": 18.29, "quantity": 35}

# for i in range(1, 50):
#     books[str(i)] = {"title": "Killing Commendatore", "author": "Haruki Murakami", "price": 18.29, "quantity": 35}

win = tk.Tk()
App(win)
win.mainloop()

