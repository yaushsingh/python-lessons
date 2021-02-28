#ask user for list of things 
#for each room, we'll tell user whether things are in room
#for each things in room we'll save things to things .txt

#split is used to split the string given by user
things = input("Enter ther list of things.Please write comma with no spaces: ").split(',')

furniture = open('furniture.txt' , 'r')
things_in_room = [line.strip() for line in furniture.readlines()]
"""function readlines reads line and gives list of [line1,line2,..] with
whitespace i.e. \n in  each list element
so we need to remove these for set inter section 
as {'chair\n'}.intersection({'chair'}) will give null set"""
"""for removing \n we perform list comprehension i.e. strip() method as seen in line 9"""

furniture.close()

things_set = set(things)
things_in_room_set = set(things_in_room)

furniture_in_room_set = things_set.intersection(things_in_room_set)
furnitures_in_room_file = open('furnitures-in-room.txt', 'w')

for things in furniture_in_room_set:
    print(f'{things} is in room.')
    furnitures_in_room_file.write(f'{things}\n')

furnitures_in_room_file.close()