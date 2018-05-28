class Database():
    def __init__(self, book_file):
        # Open or create book_file.txt
        try:
            self.book_file = open("book_file.txt", "ab+")
        except:
            self.book_file = open("book_file.txt", "w+")
            self.book_file.write("This is the file that catalogs all of the books in my library. Please don't delete this file.")


    def is_in_file(self, file, cat_entry):     # Check if a cat_entry is in a file. Return a boolean.
        lines = file.read()
        if len(lines) > 1:          # If there is more than one entry in the database file
            for line in lines:
                if line == cat_entry:
                    return True
                else:
                    return False
        else:                       # If there is one entry or less in the database file
            if cat_entry == lines:
                return True
            else:
                return False

    def add_book(self, cat_entry): # cat_entry is in the same format as a Book's cat_entry below.
        # Close book_file and open in read mode
        self.book_file.close()
        self.book_file = open("book_file.txt", "r")
        # Check if the book is already in the library
        if self.is_in_file(self.book_file, cat_entry) == False:
            self.book_file.close()
            self.book_file = open("book_file.txt", "a+")
            self.book_file.write(cat_entry)
            print("Database: The book was added to book_file.txt.")
        else:
            print("Database error in add_book(): This book is already in my library.")
        # Close book_file and open in append+ mode
        self.book_file.close()
        self.book_file = open("book_file.txt", "a+")

    def remove_book(self, cat_entry):
        # Check if the book is already in the library
        #if self.is_in_file(self.book_file, cat_entry) == True:
        # Close book_file and open in read only mode
        self.book_file.close()
        file = open("book_file.txt", "r")
        lines = file.readlines()    # store the information of the file
        file.close()
        # Open file in write only mode
        file = open("book_file.txt", "w")
        for line in lines:
            if line != cat_entry:
                file.write(line)
        # Close the file and open in append+ mode
        file.close()
        file = open("book_file.txt", "a+")
        print("Database: The book was removed from book_file.txt.")


    def find_book(self, search_term):
        # Close file and re-open in read-only mode
        self.book_file.close()
        self.book_file = open("book_file.txt", "r")
        result_count = 0
        lines = self.book_file.readlines()
        for line in lines:
            if search_term in line:
                result_count += 1
                print(result_count, line)
        if result_count == 0:
            print("No items were found in the search.")
        # Close the file and re-open in a+ mode
        self.book_file.close()
        self.book_file = open("book_file.txt", "a+")


class User_Input(Database):
    def __init__(self, Database):
        self.database = Database
    def prompt_int(self, prompt):
        # ... prompt the user for an integer, and return an integer
        number = 0
        try:
            number = int(input(prompt))
            if number < 0:  # If the user enters a negative number...
                number = number - number - number   # ...convert it to a positive number.
            return number
        except:
            print("Input operation cancelled: An integer is required.")


    def prompt_str(self, prompt):
        # ... prompt the user for a string and return a string
        try:
            print(prompt, end="")
            input_string = str(input(""))
            return input_string
        except:
            print("Input operation cancelled: A string is required.")


    def prompt_yn(self):
        # ... prompt the user for a yes or a no and return True or False
        answer = input("Yes or no? (y/n) ")
        if answer == "y":
            return True
        elif answer == "yes":
            return True
        elif answer == "Y":
            return True
        elif answer == "Yes":
            return True
        elif answer == "YES":
            return True
        else:
            return False


    def search(self):
        search_term = self.prompt_str("Enter a term to search: ")
        search = getattr(self.database, "find_book")
        search(search_term)


    def add(self, database):
        '''
	Add a book to the database.
	    '''
        first_name = self.prompt_str("What is the author's first name? ")
        last_name = self.prompt_str("What is the author's last name? ")
        title = self.prompt_str("What is the title? ")
        cat_entry = last_name + " " + first_name + " " + title + "\n"
        self.database.add_book(cat_entry)


    def remove(self, database): # TODO: handle cases where there are multiple books with the same title.
        '''
    Remove a book from the database.
	'''
        remove = self.prompt_str("Enter the title of the book you would like to remove. ")
        # Close book file and open book_file in read mode
        database.book_file.close()
        file = open("book_file.txt", "r")
        lines = file.readlines()
        # Close book file and open in append+ mode
        file.close()
        file = open("book_file.txt", "a+")
        for line in lines:
            if remove in line:
                self.database.remove_book(line)



    def view_library(self, database):   # database is a Database object.
        # Close book_file and open in read mode
        self.database.book_file.close()
        file = open("book_file.txt", "r")
        lines = file.readlines()
        # Close file and open it in append+ mode
        file.close()
        file = open("book_file", "a+")
        books = []  # a list of books in my library
        for line in lines:
            books.append(line)
        books = sorted(books)   # Alphabetize the books list by the authors' last names.
        for item in books:
            print(item)


    def get_user_input(self):
        input_dictionary = {
            "search": 1,
            "add"   : 2,
            "remove": 3,
            "view"  : 4,    # view books
            "help"  : 5,
            "h"     : 6,     # h is also a help command.
            "quit"  : 7,
            "q"     : 8      # q is also a quit command.
        }

        user_input = self.prompt_str("Keep Track> ")

        # Check for valid input
        if user_input not in input_dictionary:
            print("Invalid input. Type \"help\" to see commands.")
        elif input_dictionary[user_input] == 1:
            self.search()
        elif input_dictionary[user_input] == 2:
            self.add(self.database)
        elif input_dictionary[user_input] == 3:
            self.remove(self.database)
        elif input_dictionary[user_input] == 4: # "view" books
            self.view_library(self.database)
        elif input_dictionary[user_input] == 5:
            print("Options: ")
            for item in input_dictionary:
                print("\t",item)
        elif input_dictionary[user_input] == 6:
            print("Options: ")
            for item in input_dictionary:
                print("\t",item)
        elif input_dictionary[user_input] == 7:
            return "QUIT"
        elif input_dictionary[user_input] == 8:
            return "QUIT"
