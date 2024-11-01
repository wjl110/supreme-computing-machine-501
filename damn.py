import random

def main():
    # 生成1到100之间的随机数
    secret_number = random.randint(1, 100)
    
    print("欢迎来到数字猜字谜游戏！")
    print("我已经想好了一个1到100之间的数字。")
    
    # 循环直到用户猜对
    while True:
        # 获取用户输入
        guess = int(input("请猜一个数字："))
        
        # 比较用户猜测和秘密数字
        if guess < secret_number:
            print("猜低了！")
        elif guess > secret_number:
            print("猜高了！")
        else:
            print("恭喜你，猜对了！")
            break

if __name__ == "__main__":
    main()
