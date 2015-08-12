# defining the number of cars to be 100
cars = 100
# setting variable, space_in_a_car to equal 4.0.  The .0 is used to indicate a floating point.
space_in_a_car = 4.0
# setting variable, drivers to be an integer value of 30.
drivers = 30
# defines passengers to be 90 in number.
passengers = 90
# defines unoccupied cars.
cars_not_driven = cars - drivers
# Defines the number of drivers actually driving.
cars_driven = drivers
# Defines the carpool capacity as the number of occupied cars multiplied by the available space in a car.
carpool_capacity = cars_driven * space_in_a_car
# Defines the average # of passengers in a car.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."