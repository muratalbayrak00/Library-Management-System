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
      with open("books.txt", "r") as file:
         for line in file:
          infos = line.strip().split(",")
          print(f"Book: {infos[0]}, Author: {infos[1]}")
     
    def add_book(self):
      title =input("Enter the book title: ")
      author = input("Enter the author: ")
      year = input("Enter the release year: ")
      number_of_pages = input("Enter the number of pages: ")
      book = Book(title, author, year, number_of_pages)
      
      with open("books.txt", "a+") as file:
        file.write(book.str())
      print("Book added successfully")

    
    def remove_book(self, book_title):
     
      with open ("books.txt", "r") as file:
        new_lines = []
        info = []
        for line in file:
          info = line.strip().split(",")
          if book_title != info[0]:
            new_lines.append(line)
          else:
            print("The book successfully removed")
        if not book_title in info[0]:
           print(book_title + " couldn't found.")
      with open("books.txt", "w") as file:
        file.writelines(new_lines)
        


lib = Library()

while True:
  print("\n*****MENU*****\n1) List Books\n2) Add Book\n3) Remove Book\nQ) Quit")
  
  choice = input("Enter your choice (1-3): ")
  
  if choice == "1":#list books
    lib.list_books()
  elif choice == "2":#add book
    lib.add_book()
  elif choice == "3":# remove book
    remove_name = input("Enter the book title to remove: ")
    lib.remove_book(remove_name)
  elif choice == ("q" or "Q"):# quit
    break
  else :
    print("Invalid choice! Please choose a number between 1 and 3")
      
      

 




