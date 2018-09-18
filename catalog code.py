catalog = []

def book (title, author, genre) :
    book_add = input ("do you want to put this book in the catalog?")
    if book_add == ("yes", "y", "Yes") :
        catalog.append[book]
        return "book has been added to the catalog, call the variable catalog to veiw books that are in the catalog"
    else:
        return;
