
max_chap = 0
max_book = ""
with open("C:/Users/David/OneDrive/WDD130/Intro to Programming/books_and_chapters.txt") as FILE:
    for line in FILE:
        parts = line.split(":")
        book = (parts[0].strip())
        chapter = int(parts[1])
        cannon = (parts[2].strip())
        print(f"Scripture: {book} Chapters: {chapter} Cannon: {cannon}")
        if chapter > max_chap:
            max_chap = chapter
            max_book = book
print(f"\nThe book with the most chapters is {max_book} with {max_chap} chapters.")