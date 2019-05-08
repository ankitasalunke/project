import pandas as pd
import numpy as np
from datetime import timedelta, date, datetime
from enum import Enum
from calculate import *
from defined import *

def tubing_leak(df3):
    problemTrend=[]
    for x in range(8):
        colss=df3.iloc[:,x]
        problemTrend.append(calculate(colss))

    if problemTrend == tubing_leak:
        print(problemTrend)
        print(tubing_leak)
        return True
    else:
        return False


df = pd.read_csv('sample.csv', index_col='DateTime')
df.index = pd.to_datetime(df.index)

first_date=df.first_valid_index()
last_date=df.last_valid_index()

fs=pd.Timestamp(first_date)
ls=pd.Timestamp(last_date)

first_date = fs.to_pydatetime(first_date)
last_date = ls.to_pydatetime(last_date)

start_date = first_date + pd.Timedelta('02:00:00')

df2=df.loc[start_date:last_date]

for row in df2.itertuples():
    day1 = row.Index - pd.Timedelta('02:00:00')
    df3=df.loc[day1:row.Index]
    df.loc[row.Index, 'class'] = tubing_leak(df3)

print(df)
