class Database:
    content = {'users' : []} #class variable which exist within the object

    @classmethod
    def insert(cls , data):
        """Database.content['users'].append(data)"""
        """since content is class variable we can use cls"""
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder): #finder funct lambda x : x['username'] != 'ayush
        cls.content['users'] = [user for user in cls.content['users'] if not finder(user)]

    @classmethod
    def find(cls, finder):
        return [user for user in cls.content['users'] if finder(user)]

 