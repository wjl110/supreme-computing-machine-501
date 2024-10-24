import pandas as pd

# 读取CSV文件
file_path = './Sales.csv'  # 请替换为你的文件路径
data = pd.read_csv(file_path)

# 假设CSV文件包含以下列：'Product', 'Sales', 'Date'
# 1. 计算每种产品的总销售额
total_sales_per_product = data.groupby('Product')['Sales'].sum().reset_index()

# 2. 找到最畅销的产品
best_selling_product = total_sales_per_product.loc[total_sales_per_product['Sales'].idxmax()]

# 3. 找到销售额最高的一天
data['Date'] = pd.to_datetime(data['Date'])  # 确保日期列为datetime格式
daily_sales = data.groupby('Date')['Sales'].sum().reset_index()
highest_sales_day = daily_sales.loc[daily_sales['Sales'].idxmax()]

# 输出结果
print("每种产品的总销售额：")
print(total_sales_per_product)
print("\n最畅销的产品：")
print(best_selling_product)
print("\n销售额最高的一天：")
print(highest_sales_day)
