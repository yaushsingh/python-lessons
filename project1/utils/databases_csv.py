"""concered with storing and retrieving books from a csv file
    Format of csv file
    name,author,read\n
    """ 
books_file = 'databases-csv.txt'

def add_book(name, author):
    with open(books_file,'a') as f: # a for opening file in append mode
        f.write(f'{name},{author},0\n')

def get_all_books():
    with open(books_file,'r') as file:
        lines = [lines.strip().split(',') for lines in file.readlines()]

    books= [
        {'name' : line[0] , 'author' : line[1], 'read':line[2]} #changing list into dictionary
        for line in lines #dictionary comprehension
    ]
    return books

def mark_book_as_read (name): #calling all books then modify and saving it again
    books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books) #_save denotes its a private function and used within this file only

def _save_all_books(books): 
    with open(books_file,'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
  
     
    
    
    #considered bad practice to modify a list while you iterate over it
    """
     for book in books:
        if book['name'] = name
            books.remove(book[])"""