from question1 import books, get_Isbn, get_Saleprice, bookshop, makebook, add_book


def check_price(isbn, bookshop):
    
    allBooks = books(bookshop)
    prices = [get_Saleprice(book) for book in allBooks if get_Isbn(book) == isbn]
    return prices[0] if prices else "Book not found"

b1 = makebook("9780262510875","Struc. & Interp of Comp. Prog.",["Abelson H.","Sussman G.","Sussman J."],12, 7340.00,"CS text", 1996)

b2 = makebook("0216874068000","Algebra & No. Sys",["Hunter J."],30, 1040.00,"Math text", 1985)

b3 = makebook("9780521644082","Haskell School of Expr.",["Hudak P."],1,3455.00,"CS text", 2000)

uwiBookshop = bookshop()

add_book(b1,uwiBookshop)

add_book(b2,uwiBookshop)

add_book(b3,uwiBookshop)

print(check_price("9780262510875", uwiBookshop))
print(check_price("978026251085", uwiBookshop))