#list is in-memory database
#so it once you close app.py
#all data will be erased if file is closed

from utils import databases

User_choice = """
Enter:
- 'a' to add new list
- 'l' to list all the books
- 'r' to mark a read as book
- 'd' to delete a book
- 'q' to quit
Your Choice :  """

def menu():
    user_input = input(User_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else :
            print("Invalid Command enter")

        user_input = input(User_choice)

#now we need four method for adding listing marking deleting a book
def prompt_add_book():
    name = input("Enter the new book name:  ")
    author = input("Enter the new book author :  ")
            
    databases.add_book(name,author)

def prompt_list_book():
    books = databases.get_all_books() #asking books from database
    for book in books:
        read = 'yes' if book['read'] else 'no'
        print(f"{book['name']} by {book['author']}, read : {read}")

def prompt_read_book(): 
    name = input("Enter the name of book you just finished reading : ")

    databases.mark_book_as_read(name) 

def prompt_delete_book():
    name = input("Enter the book you want to delete: ")

    databases.delete_book(name)

#calling our menu function
menu()