#ths program can also be written by using csv module
data = open('csv-data.txt', 'r')
lines = data.readlines()
data.close()
 
#ignoring first line of data that is heading and removing the whitespaces
line = [line.strip() for line in lines[1:]]

for line in line:
    #slpitting the comma from the data
    place_data = line.split(',')
    name = place_data[0].title()
    place = place_data[1].capitalize()
    x_coordinate = place_data[2]
    y_coordinate = place_data[3]
    elevation = place_data[4]
    displacement  = place_data[5]

    print(f"{place} lies in {name} at cordinate {x_coordinate},{y_coordinate},{elevation} with {displacement}")