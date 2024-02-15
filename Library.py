from Book import Book

class Library:
    def __init__(self):
        try:
            with open('books.txt', 'r') as file:
                pass
        except FileNotFoundError:
            with open('books.txt', 'w') as file:
                pass
    # add destructor 

    
    def list_books(self):
      with open('books.txt', 'r') as file:
         for line in file:
            print(line.strip())
      
     
    def add_book(self):
      pass
    def remove_book(self):
      pass
    
library = Library()


while True:
  print("*****MENU*****\n1) List Books\n2) Add Book\n3) Remove Book\n4) Quit")
  choice = int(input("Enter your choice (1-4): "))
  if choice == 1:#list books
    pass
  elif choice == 2:#add book
    title =input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the release year: ")
    number_of_pages = input("Enter the number of pages: ")
    book = Book(title, author, year, number_of_pages)
    
    with open("books.txt", "a+") as file:
      file.write(book.str())
    print("Book added successfully\n")
  elif choice == 3:# remove book
    pass
  elif choice == 4:# quit
    break
  else :
    print("Invalid choice! Please choose a number between 1 and 4")
  







library.list_books()
#library.write_to_file("Harry Potter")


