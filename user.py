class User:
    
    def __init__(self):    
        self.users = {}
    
    def add_user(self, name, ID):
        if name in self.users:
            print("This user already exists")
        else:
            self.users[name] = {}
            self.users[name]["Library ID"] = ID
            self.users[name]["Borrowed Titles"] = []
        
    def borrowed_titles(self, name, title):
        if title not in self.users[name]["Borrowed Titles"]:
            self.users[name]["Borrowed Titles"].append(title)
    
    def display__detail(self, name):
        if name not in self.users:
            print("No info on this user")
        else:
            print(self.users[name])
        
    def display(self):
        print(self.users)
        