#!/usr/bin/env python
# coding: utf-8

# # Financial Data - Essential Workflows

# ## Importing and Exporting Stock Price Data from Yahoo Finance

# In[ ]:


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# In[ ]:


ticker = ["AAPL", "BA", "KO", "IBM", "DIS", "MSFT" ]


# In[ ]:


stocks = yf.download(ticker, start = "2010-01-01", end = "2019-02-06")


# In[ ]:


stocks.head()


# In[ ]:


stocks.tail()


# In[ ]:


stocks.info()


# In[ ]:


stocks.to_csv("stocks.csv")


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0, 1], index_col = [0], parse_dates = [0])


# In[ ]:


stocks.head()


# In[ ]:


stocks.columns = stocks.columns.to_flat_index()


# In[ ]:


stocks.columns


# In[ ]:


stocks.columns = pd.MultiIndex.from_tuples(stocks.columns)


# In[ ]:


stocks.head()


# In[ ]:


stocks.swaplevel(axis = 1).sort_index(axis = 1)


# In[ ]:





# ## Initial Inspection and Visualization

# In[ ]:


import pandas as pd


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0])


# In[ ]:


stocks.head()


# In[ ]:


stocks.tail()


# In[ ]:


stocks.info()


# In[ ]:


stocks.describe()


# In[ ]:


close = stocks.loc[:, "Close"].copy()


# In[ ]:


close.head()


# In[ ]:


import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


close.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:





# ## Normalizing Time Series to a Base Value (100)

# In[ ]:


close.head()


# In[ ]:


close.iloc[0,0]


# In[ ]:


close.AAPL.div(close.iloc[0,0]).mul(100)


# In[ ]:


close.iloc[0]


# In[ ]:


norm = close.div(close.iloc[0]).mul(100)
norm


# In[ ]:


norm.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:





# ## The shift() method

# In[ ]:


close.head()


# In[ ]:


aapl = close.AAPL.copy().to_frame()


# In[ ]:


aapl.head()


# In[ ]:


aapl.shift(periods = 1)


# In[ ]:


aapl["lag1"] = aapl.shift(periods = 1)


# In[ ]:


aapl.head()


# In[ ]:


aapl.AAPL.sub(aapl.lag1)


# In[ ]:


aapl["Diff"] = aapl.AAPL.sub(aapl.lag1)


# In[ ]:


aapl.head()


# In[ ]:


aapl.AAPL.div(aapl.lag1).sub(1).mul(100)


# In[ ]:


aapl["pct_change"] = aapl.AAPL.div(aapl.lag1).sub(1).mul(100)


# In[ ]:


aapl.head()


# In[ ]:





# ## The methods diff() and pct_change()

# In[ ]:


aapl.head()


# In[ ]:


aapl.AAPL.diff(periods = 2)


# In[ ]:


aapl["Diff2"] = aapl.AAPL.diff(periods = 1)


# In[ ]:


aapl.head(10)


# In[ ]:


aapl.Diff.equals(aapl.Diff2)


# In[ ]:


aapl["pct_change2"] = aapl.AAPL.pct_change(periods = 1).mul(100)


# In[ ]:


aapl.head()


# In[ ]:


aapl.AAPL.resample("BM").last().pct_change(periods =1).mul(100)


# In[ ]:





# ## Measuring Stock Perfromance with MEAN Return and STD of Returns

# In[ ]:


import numpy as np


# In[ ]:


aapl = close.AAPL.copy().to_frame()


# In[ ]:


aapl.head()


# In[ ]:


aapl.pct_change().dropna()


# In[ ]:


ret = aapl.pct_change().dropna()
ret.head()


# In[ ]:


ret.info()


# In[ ]:


ret.plot(kind = "hist", figsize = (12 ,8), bins = 100)
plt.show()


# In[ ]:


daily_mean_Return = ret.mean()
daily_mean_Return


# In[ ]:


var_daily_Returns = ret.var()
var_daily_Returns


# In[ ]:


std_daily_Returns = np.sqrt(var_daily_Returns)
std_daily_Returns


# In[ ]:


ret.std()


# In[ ]:


ann_mean_Return = ret.mean() * 252
ann_mean_Return


# In[ ]:


ann_var_Returns = ret.var() * 252
ann_var_Returns


# In[ ]:


ann_std_Returns = np.sqrt(ann_var_Returns)
ann_std_Returns


# In[ ]:


ret.std() * np.sqrt(252)


# In[ ]:





# ## Financial Time Series - Return and Risk

# In[ ]:


import numpy as np


# In[ ]:


norm.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


close.head()


# In[ ]:


close.pct_change().dropna()


# In[ ]:


ret = close.pct_change().dropna()


# In[ ]:


ret.head()


# In[ ]:


ret.describe().T.loc[:, ["mean", "std"]]


# In[ ]:


summary = ret.describe().T.loc[:, ["mean", "std"]]
summary


# In[ ]:


summary["mean"] = summary["mean"]*252
summary["std"] = summary["std"] * np.sqrt(252)


# In[ ]:


summary


# In[ ]:


summary.plot(kind = "scatter", x = "std", y = "mean", figsize = (15,12), s = 50, fontsize = 15)
for i in summary.index:
    plt.annotate(i, xy=(summary.loc[i, "std"]+0.002, summary.loc[i, "mean"]+0.002), size = 15)
plt.xlabel("ann. Risk(std)", fontsize = 15)
plt.ylabel("ann. Return", fontsize = 15)
plt.title("Risk/Return", fontsize = 20)
plt.show()


# In[ ]:





# ## Financial Time Series - Covariance and Correlation

# In[ ]:


ret.head()


# In[ ]:


ret.cov()


# In[ ]:


ret.corr()


# In[ ]:


import seaborn as sns


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(ret.corr(), cmap = "Reds", annot = True, annot_kws={"size":15}, vmax = 0.6)
plt.show()


# In[ ]:




