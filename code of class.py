class Car:
  def __init__(self, make, model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    name = f"{self.make} {self.model} {self.year}"
    return name

  def read_odometer(self):
    print(f"{self.odometer_reading} miles on it")

  def updat_odometer(self, milage):
    self.odometer_reading = milage

  def increment_odometer(self, miles):
    self.odometer_reading += miles
    # self.odometer_reading = self.odometer_reading+ miles
  
  def fill_gas_tank(self):
    print('This car has some gas.')


class Battery:
  def __init__(self, battery_size = 40):
    self.battery_size = battery_size
  def describe_battery(self):
    print(f'This car has a {self.battery_size}-kWh battery.')

  def get_range(self):
    if self.battery_size == 40:
      range = 150
    elif self.battery_size == 65:
      range = 200
    print(f'This car can go about {range} miles on a full charge.')

  def upgrade_battery(self):
    if self.battery_size <65:
        self.battery_size = 65
        print("Battery upgraded to 65- kwh.")
    else:
        print("Battery is already at maximum capacity.")

class ElectricCar(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = 40
    self.battery = Battery()

  

  # def describe_battery(self):
  #   print(f"The car has a {self.battery_size}-kWh battery.")

  def fill_gas_tank(self):
    print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan','leaf', 2024)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_electriccar = ElectricCar('Tesla', 'Model s', 2024)
print(my_electriccar.get_descriptive_name())
