from user import User #importing the User class from user module
from databases import Database #importing Database class from databases.py module
from Saveable import Saveable

class Admin(User, Saveable):
    def __init__(self, username, password, access):
        super(Admin,self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin{self.username}, access{self.access}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password' : self.password,
            'access' : self.access
        } 

#from databases import Database gives error #importing Database class from databases.py module
  
# if save function is duplicated in admin.py and other 
#so we create seperate saveable.py for reducing duplicable
    """def save(self):
        Database.insert(self.to_dict())"""

    #self.save() will be searched in Admin
    #then in User
    #then in Saveable, where it will be found

    #self.save() uses self.to_dict
    #self.to_dict() will be searched for in Admin, where it will be found