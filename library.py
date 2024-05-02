class Library():
    
    def __init__(self):
        self.library = {}
        
        pass
    
    def add_book(self, book):
            
        self.library[book.get_title()] = {}
        self.library[book.get_title()]["Author"] = book.get_author()
        self.library[book.get_title()]["ISBN"] = book.get_isbn()
        self.library[book.get_title()]["Publication Date"] = book.get_date()
        self.library[book.get_title()]["Genre"] = book.get_author()
        self.library[book.get_title()]["Status"] = "Available"
        
    def borrow_book(self, title):
        if title not in self.library:
            print("This book is not available in our library")
            return False
        elif self.library[title]["Status"] == "Borrowed":
            print("This book is already being borrowed")
            return False
        else:
            self.library[title]["Status"] = "Borrowed"
            return True
        
    
    def return_book(self, title):
        self.library[title]["Status"] = "Available"
        
    def find_book(self, title):
            
        if title in self.library:
            print("Found", title, "\n", self.library[title])
        
        else:
            print("This book is not available in our library")
            
    def display(self):
        print(self.library)
        
        


    
        