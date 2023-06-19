from car import Car

low = Car('Toyota Camry', 25000)
medium = Car('Honda Accord', 35000)
high = Car('Tesla Model 3', 50000)

try:
    car_budget = float(input('What is your car budget? '))
except ValueError:
    exit('Please enter a number')

for car in [high, medium, low]:
    car.buy(car_budget)