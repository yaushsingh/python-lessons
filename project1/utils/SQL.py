import sqlite3

"""concered with storing and retrieving books from a database
    
    """ 
books_file = 'books.json'

 
def create_the_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    #format of creating a table in database
    #we need to say what type of data a column will store
    # column that identifies a table is primary key
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text , read interger) ')
    connection.commit()
    connection.close()
        


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    #below command makes vunerable by string injection attak by 0);DROP book TABLE;0)
    #cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)') so use
    cursor.execute('INSERT INTO books VALUES(?,?,0)', (name,author))
    connection.commit()
    connection.close()
     

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0],'author': row[1], 'read' :row[2]} for row in cursor.fetchall()]
    #cursor.fetch gives us list of value as [(name,author,read),(name,author,read)]

    #nothing is written in disc so .commmit is not necessary
    connection.close()
    return books

def mark_book_as_read (name): #calling all books then modify and saving it again
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read =1 WHERE name = ?',(name,))

    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name = ?' (name,))
    connection.commit()
    connection.close()

  
     
    
    
