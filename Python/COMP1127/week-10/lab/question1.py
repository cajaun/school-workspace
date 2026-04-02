def bookshop():
    """constructor- creates a new bookshop"""
    return ("bookshop",[])

def books(bookshop):
    """accessor - returns all books of a bookshop"""
    return bookshop[1]
  
def makebook(isbn,title,authors,qtystck,saleprice,genre,year):
    """constructor - creates a book"""
    return [isbn,title,authors,qtystck,saleprice,genre,year]

def add_book(book,bookshop):
    """mutator - adds a book to the bookshop"""
    return bookshop[1].append(book)

# Complete the following accessor functions below.
#
# The function is expected to return the data requested such as STRING, INTEGER or FLOAT.
# The function accepts a BOOK_ADT book as parameter.
#

def get_Isbn(book):
    return book[0]

def get_Title(book):
    return book[1]

def get_Authors(book):
    return book[2]

def get_Qty(book):
    return book[3]

def get_Saleprice(book):
    return book[4]

def get_Genre(book):
    return book[5]

def get_Year(book):
    return book[6]
  


b1 = makebook("9780262510875","Struc. & Interp of Comp. Prog.",["Abelson H.","Sussman G.","Sussman J."],12, 7340.00,"CS text", 1996)

b2 = makebook("0216874068000","Algebra & No. Sys",["Hunter J."],30, 1040.00,"Math text", 1985)

b3 = makebook("9780521644082","Haskell School of Expr.",["Hudak P."],1,3455.00,"CS text", 2000)

uwiBookshop = bookshop()

add_book(b1,uwiBookshop)

add_book(b2,uwiBookshop)

add_book(b3,uwiBookshop)

