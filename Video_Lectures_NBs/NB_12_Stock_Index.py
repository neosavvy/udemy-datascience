#!/usr/bin/env python
# coding: utf-8

# # (Stock) Index Creation and Analysis

# ## Data Import, Visualization & Normalization

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use("seaborn")
pd.options.display.float_format = '{:.2f}'.format


# In[ ]:


stocks = yf.download(["AMZN", "BA", "DIS", "IBM", "KO", "MSFT"], 
                     start = "2014-01-01", end = "2018-12-31")


# In[ ]:


stocks.head()


# In[ ]:


stocks.tail()


# In[ ]:


stocks.to_csv("index_stocks.csv")


# In[ ]:


stocks = pd.read_csv("index_stocks.csv", header = [0,1], index_col = [0], parse_dates = [0]).Close


# In[ ]:


stocks


# In[ ]:


stocks.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm = stocks.div(stocks.iloc[0]).mul(100)
norm


# In[ ]:


norm.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:





# ## Creating a Price-weighted Index

# In[ ]:


stocks.head()


# In[ ]:


norm.head()


# In[ ]:


stocks.sum(axis = 1)[0]


# In[ ]:


stocks.sum(axis = 1).div(stocks.sum(axis = 1)[0]).mul(100) 


# In[ ]:


norm["PWI"] = stocks.sum(axis = 1).div(stocks.sum(axis = 1)[0]).mul(100)


# In[ ]:


norm.head()


# In[ ]:


norm.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm.loc[:, ["AMZN", "PWI"]].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm.loc[:, ["KO", "PWI"]].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


stocks.head()


# In[ ]:


stocks.div(stocks.sum(axis = 1), axis = "rows")


# In[ ]:


weights_PWI = stocks.div(stocks.sum(axis = 1), axis = "rows")


# In[ ]:


weights_PWI.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:





# ## Creating an Equal-weighted Index

# In[ ]:


stocks.head()


# In[ ]:


norm.head()


# In[ ]:


ret = stocks.pct_change().dropna()


# In[ ]:


ret.head()


# In[ ]:


ret["Mean_ret"] = ret.mean(axis = 1)


# In[ ]:


ret.head()


# In[ ]:


norm["EWI"] = 100


# In[ ]:


norm.head()


# In[ ]:


ret.Mean_ret.add(1).cumprod().mul(100)


# In[ ]:


norm.iloc[1:, -1] = ret.Mean_ret.add(1).cumprod().mul(100)


# In[ ]:


norm


# In[ ]:


norm.iloc[:, [0, 1, 2, 3, 4, 5, 7]].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm.loc[:, ["AMZN", "EWI"]].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm.iloc[:, -2:].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


weights_EWI = stocks.copy()


# In[ ]:


weights_EWI.iloc[:,:] = (1/6)


# In[ ]:


weights_EWI


# In[ ]:


weights_EWI.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:





# ## Creating a Value-weighted Index (Part 1)

# In[ ]:


stocks.head()


# In[ ]:


norm.head()


# In[ ]:


listings = pd.read_csv("listings_clean.csv")


# In[ ]:


listings.head()


# In[ ]:


listings.tail()


# In[ ]:


listings.info()


# In[ ]:


listings.set_index("Symbol", inplace = True)


# In[ ]:


listings.head()


# In[ ]:


ticker = ["AMZN", "BA", "DIS", "IBM", "KO", "MSFT"]


# In[ ]:


listings = listings.loc[ticker, ["Last_Price", "Market_Cap"]]


# In[ ]:


listings


# In[ ]:


listings.Market_Cap.div(listings.Last_Price)


# In[ ]:


listings["Shares"] = listings.Market_Cap.div(listings.Last_Price)


# In[ ]:


listings


# In[ ]:


stocks.head()


# In[ ]:


stocks.tail()


# In[ ]:


mcap = stocks.mul(listings.Shares, axis = "columns")


# In[ ]:


mcap.head()


# In[ ]:


mcap.tail()


# In[ ]:


mcap.info()


# In[ ]:


mcap.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


stocks.plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:





# ## Creating a Value-weighted Index (Part 2)

# In[ ]:


mcap.head()


# In[ ]:


mcap.sum(axis = 1)


# In[ ]:


mcap.div(mcap.sum(axis = 1), axis = "index")


# In[ ]:


weights_vwi = mcap.div(mcap.sum(axis = 1), axis = "index")


# In[ ]:


weights_vwi.tail()


# In[ ]:


weights_vwi.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.title("VWI - Weights", fontsize = 15)
plt.show()


# In[ ]:


ret = stocks.pct_change().dropna()
ret


# In[ ]:


weights_vwi.shift().dropna()


# In[ ]:


ret.mul(weights_vwi.shift().dropna()).sum(axis = 1)


# In[ ]:


norm["VWI"] = 100
norm.head()


# In[ ]:


ret.mul(weights_vwi.shift().dropna()).sum(axis = 1).add(1).cumprod().mul(100)


# In[ ]:


norm.iloc[1:, -1] = ret.mul(weights_vwi.shift().dropna()).sum(axis = 1).add(1).cumprod().mul(100)


# In[ ]:


norm


# In[ ]:


norm.iloc[:, [0, 1, 2, 3, 4, 5, 8]].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm.head()


# In[ ]:





# ## Comparison of weighting methods

# In[ ]:


norm.head()


# In[ ]:


norm.iloc[:, -3:].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


norm.iloc[:, :-3].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


weights_PWI.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.title("PWI - Weights", fontsize = 15)
plt.show()


# In[ ]:


weights_vwi.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


weights_EWI.plot(figsize = (15, 8), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:


summary = norm.pct_change().dropna().agg(["mean", "std"]).T


# In[ ]:


summary.head()


# In[ ]:


summary.columns = ["Return", "Risk"]


# In[ ]:


summary["Return"] = summary["Return"]*252
summary["Risk"] = summary["Risk"] * np.sqrt(252)


# In[ ]:


summary


# In[ ]:


summary.plot(kind = "scatter", x = "Risk", y = "Return", figsize = (15, 8), s = 50, fontsize = 15)
for i in summary.index:
    plt.annotate(i, xy=(summary.loc[i, "Risk"]+0.002, summary.loc[i, "Return"]+0.002), size = 15)
plt.xlabel("ann. Risk(std)", fontsize = 15)
plt.ylabel("ann. Return", fontsize = 15)
plt.title("Risk/Return", fontsize = 20)
plt.show()


# In[ ]:





# ## Price Index vs. Performance/Total Return Index

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")
pd.options.display.float_format = '{:.2f}'.format


# In[ ]:


stocks = pd.read_csv("index_stocks.csv", header = [0,1], index_col = [0], parse_dates = [0])


# In[ ]:


stocks.head()


# In[ ]:


adj_close = stocks["Adj Close"].copy()


# In[ ]:


total_return = adj_close.pct_change().dropna()


# In[ ]:


total_return.head()


# In[ ]:


close = stocks["Close"].copy()


# In[ ]:


weights = close.div(close.sum(axis = 1), axis = "index")


# In[ ]:


weights.head()


# In[ ]:


norm["PWI_perf"] = 100
norm.head()


# In[ ]:


norm.iloc[1:, -1] = total_return.mul(weights.shift().dropna()).sum(axis = 1).add(1).cumprod().mul(100)


# In[ ]:


norm


# In[ ]:


summary = norm.pct_change().dropna().agg(["mean", "std"]).T


# In[ ]:


summary["mean"] = summary["mean"]*252
summary["std"] = summary["std"] * np.sqrt(252)


# In[ ]:


summary


# In[ ]:


norm.iloc[:, [6, 9]].plot(figsize = (15, 8 ), fontsize = 13)
plt.legend(fontsize = 13)
plt.show()


# In[ ]:




