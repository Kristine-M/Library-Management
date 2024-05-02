
import library
import book
import user
import author
import user
import menu
import genre
import error_handle

lib_user = user.User()
lib_authors = author.Author()
menu.print_main_menu()
user_input = error_handle.main_menu_valid_input()
my_lib = library.Library()

    
while (user_input != 5):
    if user_input == 1:
        menu.print_book_op()
        inner_input = error_handle.main_menu_valid_input()
    # self.__title = "N/A"
    # self.__author = "N/A"
    # self.__isbn = "N/A"
    # self.__pub_date = "N/A"
    # self.__genre = "N/A"
        if inner_input == 1:
            new_book = book.Book()
            title = input("Title of the book you want to add: ")
            authr = input("Author of the book you want to add: ")
            isbn = input("ISBN of the book you want to add: ")
            pub_date = input("Publication date of the book you want to add: ")
            genre = input("Genre of the book you want to add: ")
            
            new_book.set_title(title)
            new_book.set_author(authr)
            new_book.set_isbn(isbn)
            new_book.set_pub_date(pub_date)
            new_book.set_genre(genre)

            my_lib.add_book(new_book)
            my_lib.display()
        
        elif inner_input == 2:
            name = input("What is your name? ")
            id = input("What is your library ID? ")
            title = input("Title of the book you want to borrow: ")
            can_borrow = my_lib.borrow_book(title)
            if can_borrow:
                lib_user.add_user(name, id)
                lib_user.borrowed_titles(name, title)    
            lib_user.display()
        
        elif inner_input == 3:
            title = input("Title of the book you want to return: ")
            my_lib.return_book(title)
            
        elif inner_input == 4:
            title = input("Title of the book you want to find: ")
            my_lib.find_book(title)
        
        elif inner_input == 5:
            print("Here is the library collection")
            my_lib.display()
            
    elif user_input == 2:
        menu.print_user_op()
        inner_input = error_handle.valid_input()
        
        if inner_input == 1:
            name = input("What is the name of the user you want to add? ")
            id = input("What is the library ID? ")
            lib_user.add_user(name, id)
            
        elif inner_input == 2:
            name = input("What is the name of the user you want to view? ")
            lib_user.display__detail(name)
            
        elif inner_input == 3:
            print("Here are all the library users")
            lib_user.display()
            
    elif user_input == 3:
        menu.print_author_op()
        inner_input = error_handle.valid_input()
        
        if inner_input == 1:
            name = input("What is the name of the author you want to add? ")
            bio = input("Give a brief description of the author? ")
            lib_authors.add_author(name, bio)
            
        elif inner_input == 2:
            name = input("What is the name of the author you want to view? ")
            lib_authors.display_detail(name)
            
        elif inner_input == 3:
            print("Here are all the library authors")
            lib_authors.display()
            
    elif user_input == 4:
        menu.print_genre_op()
        inner_input = error_handle.valid_input()
        genre_list = genre.Genre()
        
        if inner_input == 1:
            name = input("What is the genre you want to add? ")
            descrip = input("Give a brief description of the genre? ")
            genre_list.add_genre(name, descrip)
            
        elif inner_input == 2:
            name = input("What is the genre you want to view? ")
            genre_list.display_detail(name)
            
        elif inner_input == 3:
            print("Here are all the library genres")
            genre_list.display()
            

    menu.print_main_menu()           
    user_input = error_handle.main_menu_valid_input()
    
print("Thank you for visiting the library!")