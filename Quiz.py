int_ID = 3220869
name = "Jianlin Wang"
str_1 = "Happy National Day,{name} + {int_ID}!"
print(name.upper(),name.replace(" ","_"),name.startswith("Jianlin"),name.count("a"),len(name.split(' ')[-1]))

str_2 = str_1.format(name=name,int_ID=int_ID)
print(str_2)


t = "Python programming"
result = t.split("o")[-1].strip()#按照o进行分割完毕后取倒数第一个
print(result)

it = ["apple","banana","cherry"]
it[1] = it[0].upper()#把“banana”替换成“apple”元素大写
it.append(it[2][1:])#输出
print(it)


my_dict = {'nums':[1,2,3],'abc':['a','b','c']}
del my_dict['abc'][0]#删除字典中abc键的值中的第一个元素
print(my_dict)

my_dict = {'nums':[1,2,3],'abc':['a','b','c']}
my_dict['float']=[1.0,2.0]#添加一个键值对
print(my_dict)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[0])#输出[1,2,3]
print(nested_list[0][0])#输出1

nested_name = {"Jianlin1":{'name':'alise','age':18},"Jianlin2":{'name':'bob','age':19}}
print(nested_name["Jianlin1"]["name"])#输出alise
print(nested_name["Jianlin2"]["age"])#输出19

#Library = {"Fiction":{'name':'The Great Gatsby','author':'F. Scott Fitzgerald'"The Great Gatsby"},
 #          "Non-fiction":{'fic_1':"Sapiens":"Education"}}
#Company = {"HR":{'name_1':"Alice",'name_2':"Bob"},
#           "Engineering":{"Charlie","David"}}
#print(Library["Fiction"] & Company["HR"])#输出{'The Great Gatsby'}

#字典查找的方法如下
school = {'grade_1':{'g_1':'Math','g_2':'English','g_3':'Science'},
          'grade_2':{'g_1':'Math','g_2':'history'}}
menu = {'Starters':{'S_1':"Soup",'S_2':"Salad"},
        'Main Course':{'M_1':"Steak",'M_2':"Pasta"}}
print(school["grade_1"]['g_1'],menu["Starters"]['S_2'])#输出{'g_1':'Math','g_2':'English'}

#定义函数类型:
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

#定义了函数之后再调用函数
result = subtract(10,5)
print(result)#输出5

r_1 = divide(10,5)
print(r_1)#输出2.0

#有两种赋值方法第一种是直接返回函数值,第二种是赋给第三个数然后返回第三个数
def area_t(base, height):
    return base*height/2
print(area_t(10,5))#输出25.0

name_1 = "Jianlin"
number = len(name_1)
print("Hello"+ name_1 +".Your lucky number is "+ str(number))
 
name_2 = "jessica"
number_2 = len(name_2) * 9
print("Hello" + name_2 + ".Your lucky number is " + str(number_2))

#先定义、后调用
def lucky_number(name):
    number = len(name)
    print("Hello" + name + ".Your lucky number is " + str(number))

lucky_number("Jianlin")#输出HelloJianlin.Your lucky number is 7
lucky_number("jessica")
lucky_number("jane")

#判断 等于 ==,不等于 !=,大于 >,小于 <,大于等于 >=,小于等于 <=

print(10 > 1)
print(1 =="1")
#print(1 < "1")
print("cat"== "dog")# ascii码比头个字符

number = 7#求余操作
if number % 2 == 0 :
    print(f"{number} is even.")#偶数
else:
    print(f"{number} is odd.")#奇数


# ==为比较运算符,而=为赋值运算符

number = 20
if number ==20:
    print("Number is equal to 20")

# 逻辑运算符 and同时为真、 
print(5>1 and 5<10)
print(6*3 >=18 and (9+9 <=36/2))

# or其一为则为真

# not取反,在原先的结果上取反

print(25 > 50 or 1!=2)
print(not 42 == "Answer")
print((100 >50 and 50 <100) or (20 == 20 and not (5<3)))
print(not (8 != 8))
print("apple" < "banana" and "grape"> "pear")

age = 10 
if age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")

age = age =  20

s = 85
if s >= 90:
    print("A")
elif s >= 80:
    print("B")
elif s >= 70:
    print("C")
elif s >= 60:
    print("D")
else:
    print("E")

age  = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 25:
    price = 40
else:
    price = 60

print(f"Your admission cost is ${price}")

my_list = []

if not my_list:
    print("List is empty")
else:
    print("List is not empty")

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is a fruit!")
else:
    print("No, banana is not a fruit!")


numbers = [1,2,3,4,5]
if len(numbers)>3:
    print("List is too long")
else:
    print("NO")


#编写一个判断闰年的代码,先定义再调用
year = 2000
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#about loops
for i in range(5):
    print(i)


x = 1
sum = 1
while x < 10:
    sum = sum * x
    x += 1
print(sum)

#def check_age(age):
#    if age >= 18:
#        status = "Adult"
#        print("Status:",status)

x = 1 
#while x < 10:
#    x -= 1
#    print(x)

def print_numbers(n):
    for i in range(n):
        print(i)
#从0开始循环到99
print_numbers(100)

for n in range (7):
    print(n)

for n in range(1, 6 , 4):
    print(n)#起始值,中止值,步长

for n in range(1, 2, 8):
    print(n)

for n in range(1, 4, 8):
    print(n)

teams = ["Dragons", "Tigers", "Lions", "Wolves"]
for h_t in teams:
    for a_t in teams:
        if h_t != a_t:
            print(h_t, "vs", a_t)

#字符串循环字母输出
g = "Hello"
for c in g:
    print("the  character is :",c)

def factorial(n):
    if n == 1:
        return 1
        for i in range(1,n+1):
            return i * factorial(i-1)
print(factorial(5))

#编写一个for循环计算某数的阶乘





def greet_friends(friends):
    for friend in friends:
        print("Hello", friend)
greet_friends(["Alice", "Bob", "Charlie"])

for i in range(5):
    print(i)



for i in range(3):
    for j in range(2):
        print(i, j)

k = 0
for i in range(101):
    if i % 2 == 0:
        k += i
print(k)

#遍历每个学号数字,并且将各个值相加赋值给k,最后输出k的值

n_1 = 3220869
n_2 ="Jianlin Wang"
n_3 = "jessica"
#计算学号之和
n_str = str(n_1)#转换为字符串
luck = 0

for digit in n_str:
    luck += int(digit)#转化为整数相加
print(luck)

#计算英文名字符数
k = len(n_2)
print(k)
    
#luck_name为luck+k的值
luck_name = luck + k
print(luck_name)
#计算luck_name除以5的余数
print(luck_name % 5)


#创建一个函数,两个字符串名字作为输入,返回一个字典,字典中键是每个字母,值是字母出现次数
from collections import Counter

def count_letters(str1, str2):
    # 将两个字符串合并为一个字符串
    combined_str = str1 + str2
    
    # 使用Counter类计算每个字母出现的次数
    letter_counts = Counter(combined_str)
    
    return dict(letter_counts)

str1 = "Jianlin Wang"
str2 = "jessica"
result = count_letters(str1, str2)
print(result)


#类和事例相当于菜谱和做出来的菜
#类相当于菜谱,实例相当于做出来的菜
#类中定义了属性和方法,实例中可以调用类中的属性和方法


#__init__方法是一个特殊的方法，它会在创建类的实例时自动调用。self参数是一个指向实例本身的引用，你可以使用它来访问和修改实例的属性。
class Dog:
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def sit(self):
        print(f"{self.name} is barking")

    def roll_over(self):
        print(f"{self.name} rolled overd ")

my_dog = Dog("Nubia", 3, "female")
your_dog = Dog("Nokia", 6, "male")
#类中定义了属性和方法,实例中可以调用类中的属性和方法

#下面是对定义的方法进行调用
my_dog.name
my_dog.age
my_dog.gender


print(f"Its name is {my_dog.name} and its age is {my_dog.age} so its gender is {my_dog.gender}")
print(f"Its name is {your_dog.name} and its age is {your_dog.age} so its gender is {your_dog.gender}")

#注意这里一定要给到(),否则不会有输出,因为roll_over()方法中需要给到self参数,默认是传入实例本身
my_dog.roll_over()

#python中的引号单双都可以使用
class Restaurant:
    def __init__(self, restaurant_name, cuision_type,number_served):
        self.restaurant_name = restaurant_name#实例化
        self.cuision_type = cuision_type
    def describe_restaurant(self):#分别定义类中的方法
        print(f"The restaurant name is {self.restaurant_name} and the cuision type is {self.cuision_type}") #格式化固定输出返回值
        print(f"The cuision type is {self.cuision_type}")
    def open_restaurant(self):
        print(f"The restaurant is open")
    def close_restaurant(self):
        print(f"The restaurant is closed")
    def set_number_served(self,number_served):
        print(f'The number of served is {number_served}')
    def increment_number_served(self,extra_number):
        print(f'The number of served is {self.number_served}')
    def increment_number_served(self,extra_number):
        self.number_served += extra_number
    


my_restaurant = Restaurant("Zhoncan Resturant", 'Chinese', '20')#调用定义函数
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.close_restaurant()
my_restaurant.set_number_served()

your_restaurant = Restaurant("KFC", 'English', '30')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
your_restaurant.close_restaurant()
your_restaurant.set_number_served()

#分别定义后调用函数


#先定义类,再调用
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer = 23
    def get_descriptive_name(self):
        print(f"This car is {self.make} {self.model} {self.year}")
        
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")
    
    def update_odometer(self,milage):
        if milage >= self.odometer:
            self.odometer = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,extra_miles):
        self.odometer += extra_miles

#直接在类中调用
my__new_car = Car('Tesla', 'Model S', 2024)
my__new_car.read_odometer()
my__new_car.get_descriptive_name()
my__new_car.update_odometer(200)
my__new_car.increment_odometer(20)

print(my__new_car.get_descriptive_name(),my__new_car.read_odometer())

