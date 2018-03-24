#the number of cars,space_in_a_car,drivers,passengers
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#the number of cars which not driven
cars_not_driven = cars - drivers
#the number of cars which driven
cars_driven = drivers
#The number of seats in the car which driven 
carpool_capacity = cars_driven * space_in_a_car
#The number of passengers carried in each car
average_passengers_per_car = carpool_capacity/cars_driven


#print the number of cars,drivers
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
# print the number of cars which not driven
print "There will be", cars_not_driven, "empty cars today."
#print The number of seats in the car which driven 
print "We can transports", carpool_capacity, "pepple today,"
#print the number of passengers
print "We have", passengers, "to carpool today."
#print The number of passengers carried in each car
print "We need to put about", average_passengers_per_car, "in each car."