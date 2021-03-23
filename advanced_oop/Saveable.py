from databases import Database

class Saveable:
    def save(self):
        Database.insert(self.to_dict())