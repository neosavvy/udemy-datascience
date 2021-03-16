#!/usr/bin/env python
# coding: utf-8

# # Financial Data - Advanced Analysis Techniques

# ## Importing Financial Data from Excel

# In[ ]:


import pandas as pd


# In[ ]:


pd.read_excel("SP500.xls").info()


# In[ ]:


pd.read_excel("SP500.xls", parse_dates= ["Date"], index_col = "Date")


# In[ ]:


pd.read_excel("SP500.xls", parse_dates= ["Date"], index_col = "Date", usecols = "A, C:E")


# In[ ]:


pd.read_excel("SP500.xls", sheet_name= "Sales")


# In[ ]:


SP500 = pd.read_excel("SP500.xls", parse_dates= ["Date"], index_col = "Date", usecols= "A:E")


# In[ ]:


SP500.head()


# In[ ]:


SP500.tail()


# In[ ]:


SP500.info()


# In[ ]:


SP500.to_csv("SP500.csv")


# In[ ]:


SP500.to_excel("SP500_red.xls")


# In[ ]:





# ## Simple Moving Averages (SMA) with rolling()

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt 
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates = ["Date"], index_col = "Date")


# In[ ]:


SP500.head()


# In[ ]:


SP500.tail()


# In[ ]:


SP500.info()


# In[ ]:


SP500 = SP500.Close.to_frame()


# In[ ]:


SP500.head()


# In[ ]:


SP500.plot(figsize = (12,8), fontsize= 15)
plt.legend(loc = "upper left", fontsize = 15)
plt.show()


# In[ ]:


SP500 = SP500.loc["2008-12-31":"2018-12-31"].copy()


# In[ ]:


SP500.rolling(window = 10)


# In[ ]:


type(SP500.rolling(window = 10))


# In[ ]:


SP500.head(15)


# In[ ]:


SP500.rolling(window = 10).mean()


# In[ ]:


SP500.rolling(window = 10).mean()


# In[ ]:


SP500.rolling(window = 10, min_periods=5).mean()


# In[ ]:





# ## Momentum Trading Strategies with SMAs

# In[ ]:


SP500.head()


# In[ ]:


SP500.tail()


# In[ ]:


SP500["SMA50"] = SP500.rolling(window = 50, min_periods=50).mean()


# In[ ]:


SP500


# In[ ]:


SP500.plot(figsize = (12, 8), fontsize = 15)
plt.legend(loc = "upper left", fontsize = 15)
plt.show()


# In[ ]:


SP500["SMA200"] = SP500.Close.rolling(window = 200).mean()


# In[ ]:


SP500.tail()


# In[ ]:


SP500.info()


# In[ ]:


SP500.plot(figsize = (15,10), fontsize= 15)
plt.legend(fontsize = 15)
plt.show()


# In[ ]:


SP500.iloc[:,-2:].plot(figsize = (15,10), fontsize= 15)
plt.legend(fontsize = 15)
plt.show()


# In[ ]:





# ## Performance Reporting with rolling()

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col = "Date", 
                    usecols= ["Date", "Close"])


# In[ ]:


SP500.head()


# In[ ]:


SP500.resample("M", kind = "period").last()


# In[ ]:


month_ret = SP500.resample("M", kind = "period").last().pct_change().dropna()


# In[ ]:


month_ret


# In[ ]:


month_ret.rolling(36).mean()*12


# In[ ]:


month_ret["Return"] = month_ret.rolling(36).mean()*12


# In[ ]:


month_ret.Close.rolling(36).std()*np.sqrt(12)


# In[ ]:


month_ret["Risk"] = month_ret.Close.rolling(36).std()*np.sqrt(12)


# In[ ]:


month_ret.dropna(inplace= True)


# In[ ]:


month_ret.head()


# In[ ]:


month_ret.tail()


# In[ ]:


month_ret.iloc[:,-2:].plot(figsize = (15,10), fontsize= 15)
plt.legend(fontsize = 15)
plt.show()


# In[ ]:


month_ret.iloc[:,-2:].corr()


# In[ ]:


month_ret.iloc[:,-2:].plot(kind = "scatter", x = "Risk", y = "Return", figsize = (15,10), fontsize= 15, s = 40)
plt.show()


# In[ ]:





# ## Performance and Investment Periods / Time Diversification

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col = "Date",
                    usecols = ["Date", "Close"])


# In[ ]:


SP500.head()


# In[ ]:


SP500.info()


# In[ ]:


SP500.plot(figsize = (15,10), fontsize= 15)
plt.legend(fontsize = 15)
plt.show()


# In[ ]:


month_ret = SP500.resample("M", kind = "period").last().pct_change().dropna()


# In[ ]:


month_ret.tail()


# In[ ]:


month_ret.columns = ["m_returns"]


# In[ ]:


month_ret.rolling(3 * 12).mean()*12


# In[ ]:


for years in [1, 3, 5, 10, 20]:
    month_ret["{}Y".format(years)] = month_ret.m_returns.rolling(years*12).mean()*12


# In[ ]:


month_ret.tail()


# In[ ]:


month_ret.iloc[:,-5:].plot(figsize = (15,40), subplots =True, fontsize= 15, sharey = True)
plt.legend(fontsize = 20)
plt.show()


# In[ ]:





# ## Simple Returns vs. Log Returns

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


df = pd.DataFrame(index = [2016, 2017, 2018], data = [100, 50, 95], columns = ["Price"])


# In[ ]:


df


# In[ ]:


simple_returns = df.pct_change().dropna()
simple_returns


# In[ ]:


simple_returns.mean()


# In[ ]:


100 * 1.2 * 1.2


# In[ ]:


df


# In[ ]:


np.log(df / df.shift(1))


# In[ ]:


log_returns = np.log(df / df.shift(1)).dropna()


# In[ ]:


log_returns


# In[ ]:


log_returns.mean()


# In[ ]:


100 * np.exp(2 * log_returns.mean())


# In[ ]:





# ## The S&P 500 Return Triangle

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date", 
                    usecols = ["Date", "Close"])


# In[ ]:


SP500.head()


# In[ ]:


SP500 = SP500.loc["1988-12-30":"2018-12-31"].copy()


# In[ ]:


SP500.head()


# In[ ]:


annual = SP500.resample("A", kind = "period").last()
annual


# In[ ]:


annual["Return"] = np.log(annual.Close / annual.Close.shift())


# In[ ]:



annual.dropna(inplace = True)


# In[ ]:


annual


# In[ ]:


years = annual.index.size
years


# In[ ]:


windows = [year for year in range(30, 0, -1)]
windows


# In[ ]:


for year in windows:
    annual["{}Y".format(year)] = annual.Return.rolling(year).mean()


# In[ ]:


annual


# In[ ]:


triangle = annual.drop(columns = ["Close", "Return"])


# In[ ]:


triangle


# In[ ]:


plt.figure(figsize=(50,40))
sns.set(font_scale=1.8)
sns.heatmap(triangle, annot = True, fmt = ".1%", cmap = "RdYlGn", 
            vmin = -0.10, vmax = 0.15, center = 0)
plt.tick_params(axis = "y", labelright =True)
plt.show()


# In[ ]:





# ## The S&P 500 Dollar Triangle

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
plt.style.use("seaborn")
pd.options.display.float_format = '{:.0f}'.format


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date", 
                    usecols = ["Date", "Close"])


# In[ ]:


SP500.head()


# In[ ]:


SP500 = SP500.loc["1988-12-30":"2018-12-31"].copy()


# In[ ]:


SP500.head()


# In[ ]:


annual = SP500.resample("A", kind = "period").last()
annual


# In[ ]:


annual["Return"] = np.log(annual.Close / annual.Close.shift())


# In[ ]:


annual.dropna(inplace = True)


# In[ ]:


annual


# In[ ]:


years = annual.index.size
years


# In[ ]:


windows = [year for year in range(30, 0, -1)]
windows


# In[ ]:


#for year in windows:
    #annual["{}Y".format(year)] = annual.Return.rolling(year).mean()


# In[ ]:


for year in windows:
    annual["{}Y".format(year)] = np.exp(year * annual.Return.rolling(year).mean()) * 100


# In[ ]:


annual


# In[ ]:


triangle = annual.drop(columns = ["Close", "Return"])


# In[ ]:


triangle


# In[ ]:


plt.figure(figsize=(50,40))
sns.set(font_scale=1.8)
sns.heatmap(triangle, annot = True, fmt = ".0f",  cmap = "RdYlGn", 
            vmin =60, vmax = 140, center = 100)
plt.tick_params(axis = "y", labelright =True)
plt.show()


# In[ ]:





# ## The S&P 500 Return Radar

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date", 
                    usecols = ["Date", "Close"])


# In[ ]:


SP500.head()


# In[ ]:


SP500 = SP500.loc["1988-12-30":"2018-12-31"].copy()


# In[ ]:


SP500.head()


# In[ ]:


weekly = SP500.resample("W", kind = "period").last()
weekly


# In[ ]:


weekly["Return"] = np.log(weekly.Close / weekly.Close.shift())*52


# In[ ]:


weekly.dropna(inplace = True)


# In[ ]:


weekly


# In[ ]:


weeks = weekly.index.size
weeks


# In[ ]:


windows = [week for week in range(weeks, 0, -1)]
windows


# In[ ]:


for week in windows:
    weekly["{}W".format(week)] = weekly.Return.rolling(week).mean()


# In[ ]:


weekly


# In[ ]:


triangle = weekly.drop(columns = ["Close", "Return"])


# In[ ]:


triangle


# In[ ]:


plt.figure(figsize=(50,40))
sns.set(font_scale=1.8)
sns.heatmap(triangle, annot =False, cmap = "RdYlGn", 
            vmin = -0.10, vmax = 0.10, center = 0)
#plt.tick_params(axis = "y", labelright =True)
plt.show()


# In[ ]:





# ## Exponentially-weighted Moving Averages (EWMA)
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date", usecols= ["Date", "Close"])


# In[ ]:


SP500.head()


# In[ ]:


SP500 = SP500.loc["2008-12-31":"2018-12-31"].copy()


# In[ ]:


SP500.Close.rolling(window = 10).mean()


# In[ ]:


SP500.Close.ewm(span = 10, min_periods= 10).mean()


# In[ ]:


SP500["SMA"] = SP500.Close.rolling(window = 100).mean()
SP500["EMA"] = SP500.Close.ewm(span = 100, min_periods= 100).mean()


# In[ ]:


SP500


# In[ ]:


SP500.iloc[:,-2:].plot(figsize = (15,10), fontsize =15)
plt.legend(fontsize = 15)
plt.show()


# In[ ]:





# ### Expanding Windows

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date", usecols= ["Date", "Close"])


# In[ ]:


SP500 = SP500.loc["2008-12-31":"2018-12-31"].copy()


# In[ ]:


SP500.head()


# In[ ]:


SP500.Close.rolling(10).mean()


# In[ ]:


SP500.Close.expanding(min_periods = 1).mean()


# In[ ]:


SP500["SMA50"] = SP500.Close.rolling(50).mean()
SP500["EXP"] = SP500.Close.expanding().max()


# In[ ]:


SP500.head()


# In[ ]:


SP500.iloc[:, -2:].plot(figsize = (12, 8))
plt.show()


# In[ ]:





# ## Rolling Correlation

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


app_ba = stocks.loc["2009-12-31":"2018", ["AAPL", "BA"]]


# In[ ]:


app_ba.head()


# In[ ]:


month_ret = app_ba.resample("M", kind = "period").last().pct_change().dropna()


# In[ ]:


month_ret.head()


# In[ ]:


month_ret.tail()


# In[ ]:


month_ret.info()


# In[ ]:


month_ret.corr()


# In[ ]:


month_ret.AAPL.rolling(36).corr(month_ret.BA)


# In[ ]:


month_ret.AAPL.rolling(36).corr(month_ret.BA).plot(figsize = (12,8))
plt.show()


# In[ ]:





# ## rolling() with fixed-sized time offsets

# In[ ]:


app_ba.head(7)


# In[ ]:


app_ba.BA.rolling(window = 3).mean().head(7)


# In[ ]:


app_ba.head(7)


# In[ ]:


app_ba.BA.rolling(window = "3D", min_periods = 3).mean()


# In[ ]:





# ### Merging Time Series

# In[ ]:


import pandas as pd


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


aapl = stocks.loc["2010-01-01" : "2014-12-31", "AAPL"].to_frame()
aapl.head()


# In[ ]:


ba = stocks.loc["2012-01-01" : "2016-12-31", "BA"].to_frame()
ba.head()


# In[ ]:


aapl["BA"] = ba.BA


# In[ ]:


aapl.head()


# In[ ]:


aapl.tail()


# In[ ]:


aapl.dropna()


# In[ ]:


ba.reindex(aapl.index).dropna()


# In[ ]:


dis = stocks.loc["2010-01-01" : "2016-12-31", "DIS"].resample("W-Fri").last().to_frame()
dis.head()


# In[ ]:


aapl.head()


# In[ ]:


aapl["DIS"] = dis.DIS


# In[ ]:


aapl.head(10)


# In[ ]:


dis.reindex(aapl.index)


# In[ ]:


dis["AAPL"] = aapl.AAPL


# In[ ]:


dis.head(10)


# In[ ]:




