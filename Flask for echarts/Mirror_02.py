import pandas as pd
import warnings
import os
from sqlalchemy import create_engine

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

warnings.filterwarnings("ignore")

engine = create_engine('mysql+pymysql://root:123456@localhost/Weather?charset=utf8')

Names_last_xls = os.listdir("F:\\Python 工作室学习\\WeatherData\\xls")
for fileName in Names_last_xls:
    xls_path = '..//WeatherData//xls//' + fileName
    df = pd.read_excel(xls_path)
    df.to_sql(fileName, engine, index=False, if_exists='append')
