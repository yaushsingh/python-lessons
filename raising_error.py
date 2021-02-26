""" raising an error helps developer to know the error
    its good to crash program during development phase 
    but for user interface its good to catch error ratherthan showing the stack errors"""
class User:
    def __init__(self, name, engagement): 
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'< User {self.name}>'

def get_user_score(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
        return user.score
    except KeyError:
        print('Incorrect values provided to our calcualtion function.')
        raise
    #while using raise we need to give type of error if we use raise outside except block

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    get_user_score(user)
    if user.score > 500:
        print(f' Notification sent to {user}.')


my_user1 = User('asish', {'clicks': 84, 'hits': 50})
send_engagement_notification(my_user1)
print(get_user_score(my_user1))

my_user = User('Ayush' , {'click' : 61 , 'hits' : 100})
get_user_score(my_user)
