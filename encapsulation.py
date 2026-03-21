class Vehicle():

    def __init__(self, transportation,fuel_capacity, fuel_cost, mpg):
        self._transportation = transportation
        self._fuel_capacity = fuel_capacity
        self._fuel_cost = fuel_cost
        self._mpg = mpg

    @property
    def range(self):
        return self._fuel_capacity * self._mpg
    
    @property
    def mile_cost(self):
        return self._fuel_cost / self._mpg
    

car = Vehicle("Car", 13, 3, 40)
bus = Vehicle("Bus", 40, 5, 10)
jet = Vehicle("Plane", 50, 6, 50)
bike = Vehicle("Bike", 10, 4, 40)

vehicles = [car, bus, jet, bike]

def get_mile_cost(vehicles): 
    return vehicles.mile_cost

vehicles.sort(key=get_mile_cost)

print("Name\tRange\tCost per mile")

for v in vehicles:
    print(v._transportation, "\t", v.range, "\t",v.mile_cost)


    
    