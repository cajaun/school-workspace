from question1 import books,get_Isbn,get_Qty, get_Title,  bookshop, makebook, add_book


def booksToReorder(reorder, bookshop):
    
  allBooks = books(bookshop)  
  booksForReorder = [(get_Isbn(book), get_Title(book)) for book in allBooks if get_Qty(book) <= reorder]

  return booksForReorder


b1 = makebook("9780262510875","Struc. & Interp of Comp. Prog.",["Abelson H.","Sussman G.","Sussman J."],12, 7340.00,"CS text", 1996)

b2 = makebook("0216874068000","Algebra & No. Sys",["Hunter J."],30, 1040.00,"Math text", 1985)

b3 = makebook("9780521644082","Haskell School of Expr.",["Hudak P."],1,3455.00,"CS text", 2000)

uwiBookshop = bookshop()

add_book(b1,uwiBookshop)

add_book(b2,uwiBookshop)

add_book(b3,uwiBookshop)

print(booksToReorder(15, uwiBookshop))
