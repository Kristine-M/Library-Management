
class Book():
    
    
    def __init__(self):
        self.__title = "N/A"
        self.__author = "N/A"
        self.__isbn = "N/A"
        self.__pub_date = "N/A"
        self.__genre = "N/A"
    
    def set_title(self, title):
        
        self.__title = title
    
    def set_author(self, author):
        
        self.__author = author
    
    def set_title(self, title):
        
        self.__title = title
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def set_pub_date(self, date):
        self.__pub_date = date
        
    def set_genre(self, genre):
        self.__genre = genre
        
    def get_title(self):
        
        return self.__title
    
    def get_author(self):
        
        return self.__author
    
    def get_genre(self):
        
        return self.__genre
    
    def get_isbn(self):
        
        return self.__isbn
    
    def get_date(self):
        
        return self.__pub_date
    
    def display(self):
        
        print("Title:", self.title, "\n", "Author:", self.author,  
              "\n", "Genre:", self.genre, "\n")