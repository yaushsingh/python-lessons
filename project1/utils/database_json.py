"""concered with storing and retrieving books from a JSON file
    Format of JSON file
    [
        {'name': name, 'author': author, 'read': true}
    ]
    """ 
import json
books_file = 'books.json'

#creating books.json if it doesnot exists
def create_the_table():
    with open (books_file,'w') as f :
        json.dump([],f) #json file cannot be empty so we initialize by .dump(,)
        


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name , 'author': author, 'read': False})
    #it is list so we can do .append()
    _save_all_books(books)

def get_all_books():
    with open(books_file,'r') as file:
        return json.load(file)

def mark_book_as_read (name): #calling all books then modify and saving it again
    books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books) #_save denotes its a private function and used within this file only

def _save_all_books(books): 
    with open(books_file,'w') as file:
        json.dump(books,file)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
  
     
    
    
    #considered bad practice to modify a list while you iterate over it
    """
     for book in books:
        if book['name'] = name
            books.remove(book[])"""