#先定义再调用函数名称
# 默认油车的相关参数信息
class Car:
  def __init__(self, make, model,year):
    # 初始化汽车对象，设置品牌、型号和年份
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    # 获取汽车的描述性名称
    name = f"{self.make} {self.model} {self.year}"
    return name

  def read_odometer(self):
    # 打印汽车的里程表读数
    print(f"{self.odometer_reading} miles on it")

  def updat_odometer(self, milage):
    # 更新汽车的里程表读数
    self.odometer_reading = milage

  def increment_odometer(self, miles):
    # 增加汽车的里程表读数
    self.odometer_reading += miles
    # self.odometer_reading = self.odometer_reading+ miles
  
  def fill_gas_tank(self):
    # 打印汽车加油信息
    print('This car has some gas.')


class Battery:
  def __init__(self, battery_size = 40):
    # 初始化电池对象，设置电池容量
    self.battery_size = battery_size
  def describe_battery(self):
    # 打印电池容量信息
    print(f'This car has a {self.battery_size}-kWh battery.')

  def get_range(self):
    # 根据电池容量计算汽车续航里程
    if self.battery_size == 40:
      range = 150
    elif self.battery_size == 65:
      range = 200
    print(f'This car can go about {range} miles on a full charge.')

  def upgrade_battery(self):
    # 升级电池容量
    if self.battery_size <65:
        self.battery_size = 65
        print("Battery upgraded to 65- kwh.")
    else:
        print("Battery is already at maximum capacity.")

class ElectricCar(Car):
  def __init__(self, make, model, year):
    # 初始化电动汽车对象，设置品牌、型号和年份
    super().__init__(make, model, year)
    self.battery_size = 40
    self.battery = Battery()

  # def describe_battery(self):
  #   print(f"The car has a {self.battery_size}-kWh battery.")

  def fill_gas_tank(self):
    # 打印电动汽车加油信息
    print("This car does not have a gas tank!")

my_leaf = ElectricCar('nissan','leaf', 2024)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


# 最后一排定义了一个ElectricCar类，继承自Car类，并添加了一个battery属性，用于存储电池容量信息。
# ElectricCar类还重写了fill_gas_tank()方法，使其不再打印加油信息，而是打印电动汽车加油信息。
# 最后，创建了一个ElectricCar对象my_leaf，并调用了battery的describe_battery()和get_range()方法，打印了电池容量和续航里程信息。

# 汽油车用汽油车的电动等级,而不是电动车的等级
my_electriccar = ElectricCar('Tesla', 'Model s', 2024)
print(my_electriccar.get_descriptive_name())
my_electriccar.fill_gas_tank()