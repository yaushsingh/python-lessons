books = []

def add_book(name, author):
    books.append({'name':name , 'author': author, 'read': False})

def get_all_books():
    return books

def mark_book_as_read (name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books 
    """for python to know that books used as variable and in this
        list compreshension is same as declared globally"""
    books = [book for book in books if book['name'] != name]
    
    
    
    #considered bad practice to modify a list while you iterate over it
    """
     for book in books:
        if book['name'] = name
            books.remove(book[])"""
