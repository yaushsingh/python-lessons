from admin import Admin 
from databases import Database 

a = Admin('ayush','1234', 3)
a.save()

print(Database.find(lambda x: x['username'] == 'ayush'))