#Keenan Githu
#W6D2 Lab 5
#2-20-2025

"""
PROGRAM PROMPT:


VARIABLE DICTIONARY:

NOTES:
None
"""

import csv



library_number = []
book_title = []
book_author = []
book_genre = []
page_count = []
status = []

with open('text_files/book_list.csv') as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        library_number.append(record[0].lower())
        book_title.append(record[1].lower())
        book_author.append(record[2].lower())
        book_genre.append(record[3].lower())
        page_count.append(record[4].lower())
        status.append(record[5].lower())



library_menu = True

while library_menu == True:
    print("\n---------Personal Library Menu---------\n")
    print("1. Show All Titles")
    print("2. Search By Title")
    print("3. Search By Author")
    print("4. Search By Genre")
    print("5. Search By Library Number")
    print("6. Show All Available")
    print("7. Show All On Loan")
    print("8. EXIT")

    options = input("Enter a number (1-8): ")

    match options:
        case "1":
            print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
            for i in range(len(book_title)):
                print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
        
        case "2":
            count = 0

            title_search = input("Enter the title of a book: ").lower()
            if title_search in book_title:
                i = book_title.index(title_search)
                print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
                print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
            else:
                print("Book not found. Searching by keywords...")
                for i in range(len(book_title)):
                    if title_search in book_title[i]:
                        if count == 0:
                            print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
                        count += 1
                        print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
                if count == 0:
                    print("No items found associated with keyword.\n")
        
        case "3":
            count = 0

            author_search = input("Enter the name of the author: ").lower()
            for i in range(len(book_author)):
                if book_author[i] == author_search:
                    if count == 0:
                        print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
                    count += 1
                    print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
            if author_search not in book_author:
                print("Author not found. Searching by keywords...")
                for i in range(len(book_author)):
                    if author_search in book_author[i]:
                        if count == 0:
                            print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
                        count += 1
                        print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
                if count == 0:
                    print("No items found associated with keyword.\n")

        case "4":
            count = 0

            genre_search = input("Enter a genre to search by: ").lower()

            for i in range(len(book_genre)):
                if book_genre[i] == genre_search:
                    if count == 0:
                        print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
                    count += 1
                    print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
            if count == 0:
                print("No items found associated with keyword. \n")
        
        case "5":
            count = 0

            number_search = input("Enter the book's library number: ")
            if number_search in library_number:
                i = library_number.index(number_search)
                print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
                print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())
            else:
                print("Book not found.")
        
        case "6":
            print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
            for i in range(len(status)):
                if status[i] == "available":
                    print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())

        case "7":
            print(f"{"NAME":35} {"NUM":5} {"AUTHOR":16} {"GENRE":20} {"PAGES":7} {"STATUS":10}")
            for i in range(len(status)):
                if status[i] == "on loan":
                    print(f"{book_title[i]:35} {library_number[i]:5} {book_author[i]:16} {book_genre[i]:21} {page_count[i]:6} {status[i]:10}".upper())

        case "8":
            library_menu = False
            continue


        case _:
            print("Invalid Input \n \n")
            continue

    