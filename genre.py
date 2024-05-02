
class Genre():
    
    def __init__(self):
        self.genre = {}
        pass
    
    def add_genre(self, genre_cat, descrip):
        self.genre[genre_cat] = {}
        self.genre[genre_cat]["Description"] = descrip
        
    def display_detail(self, genre_cat):
        if genre_cat not in self.genre:
            print("This genre has not been added")
        else:
            print(self.genre[genre_cat])
        
    def display(self):
        print(self.genre)