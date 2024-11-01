import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def my_function():
    import pandas as pd
    # 使用 pandas 的 read_csv 方法

start_date = "2023-01-01"
end_date = "2023-12-31"

apple_data = yf.download("AAPL", start=start_date, end=end_date)

# 获取开盘价数据
open_prices = apple_data['Open']

# 获取收盘价数据
close_prices = apple_data['Close']
# 获取最高价数据
high_prices = apple_data['High']

# 获取最低价数据
low_prices = apple_data['Low']

# 打印数据
print("Open Prices:\n", open_prices)
print("Close Prices:\n", close_prices)
print("High Prices:\n", high_prices)
print("Low Prices:\n", low_prices)
# 计算20日移动平均线
moving_average = close_prices.rolling(window=20).mean()

# 打印日收盘价和20日移动平均线
print("日收盘价：")
print(close_prices)
print("\n20日移动平均线：")
print(moving_average)

#第二部分
#使用matplotlib创建这些图表的示例代码：


# 假设我们有一个包含股票价格的DataFrame
data = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
                     'Price': [100, 110, 105, 115]})

# 将日期转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])

# 绘制股票价格走势图
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Price'], marker='o')
plt.title('Stock Price Trend')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()

#第三部分
#图表价格和移动平均线在同一图表上：
import matplotlib.pyplot as plt
import pandas as pd

# 假设我们有一个包含股票价格的DataFrame
data = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
                     'Price': [100, 110, 105, 115]})

# 将日期转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])

# 计算移动平均线
data['MA'] = data['Price'].rolling(window=2).mean()

# 绘制股票价格走势图和移动平均线
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Price'], marker='o', label='Price')
plt.plot(data['Date'], data['MA'], marker='o', label='Moving Average')
plt.title('Stock Price and Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

#第四部分
#用不同的颜色区分价格的涨跌：
import matplotlib.pyplot as plt
import pandas as pd

# 假设我们有一个包含股票价格的DataFrame
data = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
                     'Price': [100, 110, 105, 115]})

# 将日期转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])

# 计算价格的涨跌
data['Change'] = data['Price'].pct_change()

# 绘制股票价格走势图，用不同的颜色区分价格的涨跌
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Price'], marker='o', label='Price')
plt.fill_between(data['Date'], data['Price'], where=data['Change'] > 0, color='green', alpha=0.3)
plt.fill_between(data['Date'], data['Price'], where=data['Change'] < 0, color='red', alpha=0.3)
plt.title('Stock Price with Up/Down Color Distinction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
