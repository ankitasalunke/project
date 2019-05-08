#You can use datetime.toordinal to map each date to an integer and sklearn.linear_model to fit a linear regression model on your data to obtain the slope like:
import datetime as dt
import pandas as pd
import numpy as np
from datetime import timedelta, date, datetime
from enum import Enum
from num import *
from sklearn import linear_model

def calculate(cols):
    df=cols.to_frame()

    df['datetime'] = df.index

    df.datetime = pd.to_datetime(df.datetime)

    df["datetime"]= df.datetime.values.astype(np.int64) // 10 ** 9
    
    reg = linear_model.LinearRegression()

    reg.fit(df.datetime.values.reshape(-1, 1), df.iloc[:,0].values)
    if reg.coef_[0]>0:
        return trend.incereasing
    elif reg.coef_[0]<0:
        return trend.decreasing
    elif reg.coef_[0]==0:
        return trend.constant


