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
