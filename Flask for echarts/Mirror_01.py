# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.types import NVARCHAR
# # import pymysql
# import os
#
#
# # def pd2sql():
# #     #engine = create_engine("mysql+mysqlconnector://root:123456@localhost/Weather", echo=False)
# #     engine = create_engine('mysql+pymysql://root:123456@localhost/weather', echo=False)
# #     conn = engine.connect()
#     #     for i in range(1, 10):
#     #         dtypedict = {
#     #             'time_now': NVARCHAR(length=255),
#     #             'temperature': NVARCHAR(length=255),
#     #             'weather': NVARCHAR(length=255),
#     #             'wet': NVARCHAR(length=255),asas
#     #
#     #             'windDirect': NVARCHAR(length=255),
#     #             'windSpeed': NVARCHAR(length=255),
#     #
#     #         }
# #
#
# df = pd.read_excel("F:\Python 工作室学习\WeatherData\\2021-07-111625965333.36322WeatherHourly.xls")
# df.head()
#
# df.index.name = "id"
# df.head()
#
# #
# #         df.to_sql(f'csv_table{i}', engine, if_exists='replace', index=False, dtype=dtypedict)
# #         # 将dataframe 储存为MySQL中的数据表，不储存index列
# #         conn.execute(f"alter table csv_table{i} add constraint  p key primary key (index_code)")
# #         #   设置主键
# #         if i % 2 == 0:
# #             conn.execute(
# #                 f"alter table csv_table{i} add foreign key (index_code) references csv_table{i}(index_code) ")
# #         print(f"Write to Mysql Successfully! ----csv_table{i}")
# #     engine.dispose()
# #
# #
# # if __name__ == '__main__':
# #     pd2sql()
# # 对已存在的表做主键：alter table csv_short1 add constraint p_key primary key (index_code);
#
# # 对已存在的表做外键：alter table csv_short1 add  foreign key (index_code) references csv_short2(index_code);
#
# # 内连接查询：select * from a,b where a.x = b.x
