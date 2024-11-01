def calculate_bmi(height, weight):
    """计算BMI值"""
    bmi = weight / (height ** 2)
    return bmi

def get_health_advice(bmi):
    """根据BMI值提供健康建议"""
    if bmi < 18.5:
        return "体重过轻，建议增加营养摄入。"
    elif 18.5 <= bmi < 24:
        return "体重正常，继续保持。"
    elif 24 <= bmi < 28:
        return "体重过重，建议进行适量的运动和健康饮食。"
    elif 28 <= bmi < 32:
        return "肥胖，建议寻求专业医生的建议。"
    else:
        return "重度肥胖，建议寻求专业医生的建议。"

def main():
    # 获取用户输入
    height = float(input("请输入您的身高（米）："))
    weight = float(input("请输入您的体重（千克）："))

    # 计算BMI
    bmi = calculate_bmi(height, weight)

    # 输出BMI值
    print(f"您的BMI值是：{bmi:.2f}")

    # 提供健康建议
    advice = get_health_advice(bmi)
    print(advice)

if __name__ == "__main__":
    main()
