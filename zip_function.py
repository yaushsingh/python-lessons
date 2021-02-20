#zip function
friends=["ayush", "shiva","jayant","Tirtha"]
time_since_met=[2,14,23,30]
long_timer=dict(zip(friends,time_since_met))
print(long_timer)
rev=list(zip(time_since_met,friends,list(range(1,5))))
print(rev)