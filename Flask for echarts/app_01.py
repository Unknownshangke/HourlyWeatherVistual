from flask import Flask, render_template
import pandas as pd
import os
from sqlalchemy import create_engine

#连接 MySQL
Names_last_xls = os.listdir(r"F:\Python 工作室学习\WeatherData\xls")
# print(Name_last_csv)

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/weather')
sql_query = "select * from `" + Names_last_xls[-1] + "`"

# print(sql_query)

data_frame = pd.read_sql_query(sql_query, engine)

# print(data_frame)

# 获取数据的列
columns = data_frame.columns
# 提取数据
time_now = data_frame['time_now'].tolist()
temperature_ = data_frame['temperature'].tolist()
temperature = []
weather = data_frame['weather'].tolist()
wet_ = data_frame['wet'].tolist()
wet = []
for i in range(len(wet_)):
    wet_str = wet_[i]
    wet.append(wet_str.strip('%'))
for i in range(len(temperature_)):
    temperature_str = temperature_[i]
    temperature.append(temperature_str.strip('°'))
# print(temperature)
# print(wet)
windDirection = data_frame['windDirection'].tolist()
windSpeed = data_frame['windSpeed'].tolist()

# 创建flask实例
app = Flask(__name__)


# 创建视图
@app.route("/")
def echarts_01():
    # 数据传输到前端
    return render_template("Echarts_01.html", time_now=time_now, temperature=temperature, wet=wet,
                           weather=weather, windDirection=windDirection, windSpeed=windSpeed)


#
# 运行程序
if __name__ == '__main__':
    app.run(debug=True)
