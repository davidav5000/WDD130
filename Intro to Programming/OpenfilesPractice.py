with open("C:/Users/David/OneDrive/WDD130/Intro to Programming/books.txt") as BOOKS:
    for line in BOOKS:
        book = line.strip()
        print(book)