from flask import Flask, render_template
import pandas as pd
import os

# 获取数据
Names_last_csv=os.listdir(r"F:\Python 工作室学习\WeatherData\csv")
# print(Name_last_csv)
Name_last_csv_01='\\'+Names_last_csv[-1]
Name_last_csv_02=r'F:\Python 工作室学习\WeatherData\csv'+Name_last_csv_01

data = pd.read_csv(Name_last_csv_02)
# 获取数据的列
columns = data.columns
# 提取数据
time_now = data['time_now'].tolist()
temperature_ = data['temperature'].tolist()
temperature = []
weather = data['weather'].tolist()
wet_ = data['wet'].tolist()
wet = []
for i in range(len(wet_)):
    wet_str = wet_[i]
    wet .append( wet_str.strip('%') )
for i in range(len(temperature_)):
    temperature_str = temperature_[i]
    temperature .append( temperature_str.strip('°') )
# print(temperature)
# print(wet)
windDirection = data['windDirection'].tolist()
windSpeed = data['windSpeed'].tolist()

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
