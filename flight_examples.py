#KTM -> NPJ -> BJR
from typing import List

class segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments:List[segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return "--->".join(stops)
    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter  #decorator of property
    def departure_point(self, val): #can use same thing or something else
        #self.segments[0].departure = val
        dest = self.segments[0].destination
        self.segments[0] = segment(departure = val, destination = dest) 



flight = Flight([segment("KTM","BJR")])
print(flight.departure_point) #calling the property from a class
#flight.segments[0].departure = "NPJ"
print(flight)
flight.departure_point = "NPJ"
print(flight)