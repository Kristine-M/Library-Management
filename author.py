class Author:
    
    def __init__(self):
        self.authors = {}
    
    def add_author(self, author_to_add, bio):
        
        if author_to_add in self.authors:
            print("Author already added")
        else:
            self.authors[author_to_add] = bio
    
    def display_detail(self, name):
        
        if name not in self.authors:
            print("This author is not in the added in the library database yet")
        else:
            print(self.authors[name])
        
    def display(self):
        print(self.authors)
        
    