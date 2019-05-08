import numpy as np
import pandas as pd
from sklearn import linear_model

def trendline(data, order=1):
    coeffs = np.polyfit(data.index.values, list(data), order)
    print(data.index.values)
    slope = coeffs[-2]
    return float(slope)

#Sample Dataframe
revenue = [0.85, 0.99, 1.01, 1.12, 1.25, 1.36, 1.28, 1.44]
year = [1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
df = pd.DataFrame({'year': year, 'revenue': revenue})


slope = trendline(df['revenue'])
print(slope)

    reg.fit(df.datetime.values.reshape(-1, 1), df['current'].values)



