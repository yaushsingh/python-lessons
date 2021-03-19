""" if you named your file datetime.py for testing
then you wrote import datetime inside it, because that's the module you want to try out
What happens when you run the file, is that:

Python first looks into your local directory for a module called datetime
Since Python only finds your original file, 
it makes an empty module file called datetime.pyc, 
because it expects you to build upon it"""
from datetime import datetime,timezone, timedelta
#importing datetime class from datetime module

print(datetime.now()) #naive datetime as it doesnot include timezone
print(datetime.now(timezone.utc))
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days = 1.5)
print(today)
print(tomorrow)
print(today.strftime('%d-%m-%Y %H:%M:%S')) #strftime formats the time value
try:
    user_date = input(" Enter the date in YYYY-mm-dd: ")
    user_date = datetime.strptime(user_date, '%Y-%m-%d')  #strptime = string phrase time
except ValueError :
    exit ('please enter date in mentioned format')


print(user_date)