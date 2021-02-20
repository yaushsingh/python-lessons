friends=["Ayush","Garima","Mahima","Asish"]
guests= ["ayush","micheal","Charlie","Asish","Prabha"]
friend_lower=set([f.lower() for f in friends])
guest_lower=set([g.lower() for g in guests])
print(friend_lower.intersection(guest_lower))
#another approach
friends_lower=[f.lower() for f in friends]
present_friends= [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)
#dictionary comprehension
new_friends=["susan","sajana","khusi","bishal"]
met_date=[2,23,13,15]
new_dict={
    new_friends[i]:met_date[i]
    for i in range(len(new_friends))
    if met_date[i]>10 
}
print(new_dict)
