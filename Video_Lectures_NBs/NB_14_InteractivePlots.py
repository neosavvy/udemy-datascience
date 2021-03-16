#!/usr/bin/env python
# coding: utf-8

# # Interactive Plotting with Plotly and Cufflinks

# ## Creating Offline Graphs in Jupyter Notebooks

# In[ ]:


import pandas as pd
import cufflinks as cf


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


norm = stocks.div(stocks.iloc[0, :]).mul(100)


# In[ ]:


norm


# In[ ]:


cf.set_config_file(offline = True)


# In[ ]:


cf.go_offline()


# In[ ]:


norm.iplot()


# In[ ]:





# ## Interactive Price Charts with Plotly

# In[ ]:


import pandas as pd
import cufflinks as cf


# In[ ]:


cf.set_config_file(offline = True)


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


norm = stocks.div(stocks.iloc[0, :]).mul(100)


# In[ ]:


norm


# In[ ]:


norm.iplot()


# In[ ]:





# ## Customizing Plotly Charts

# In[ ]:


norm.head()


# In[ ]:


norm.iplot(kind = "line", fill = True)


# In[ ]:


cf.colors.scales()


# In[ ]:


norm.iplot(kind = "line", fill = True, colorscale= "reds")


# In[ ]:


cf.getThemes()


# In[ ]:


norm.iplot(kind = "line", fill = True, colorscale= "rdylbu", theme= "solar")


# In[ ]:


norm.iplot(kind = "line", fill = True, colorscale= "rdylbu", theme= "solar", 
             title= "US Stocks", xTitle= "Time", yTitle= "Stock Price")


# In[ ]:


norm[["AAPL", "BA"]].iplot(kind = "spread", fill = True, colorscale= "set3", theme= "solar",
                             title= "AAPL vs. BA", xTitle= "Time", yTitle= "Stock Price")


# In[ ]:





# ## Creating Interactive Histograms

# In[ ]:


stocks.head()


# In[ ]:


ret = stocks.pct_change().dropna()


# In[ ]:


ret.head()


# In[ ]:


ret.iplot(kind = "histogram", bins = (-0.15, 0.1, 0.001), histnorm= "percent")


# In[ ]:





# ## Interactive Candlestick and OHLC Charts 

# In[ ]:


import pandas as pd
import cufflinks as cf


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0])


# In[ ]:


stocks.head()


# In[ ]:


aapl = stocks.swaplevel(axis = 1).AAPL


# In[ ]:


aapl.head()


# In[ ]:


aapl.loc["5-2017":"9-2017"].iplot(kind= "candle")


# In[ ]:





# ## Adding SMA and Bollinger Bands 

# In[ ]:


aapl.head()


# In[ ]:


qf = cf.QuantFig(df = aapl.loc["5-2017":"9-2017"])


# In[ ]:


type(qf)


# In[ ]:


qf.iplot(title = "AAPL", name = "AAPL")


# In[ ]:


qf.add_sma(periods = 20)


# In[ ]:


qf.iplot(title = "AAPL", name = "AAPL")


# In[ ]:


qf.add_bollinger_bands(periods = 20, boll_std= 2)


# In[ ]:


qf.iplot(title = "AAPL", name = "AAPL")


# In[ ]:





# ## Adding more Technical Indicators

# In[ ]:


qf = cf.QuantFig(df = aapl.loc["5-2017":"9-2017"])


# In[ ]:


qf.add_bollinger_bands(periods = 20, boll_std= 2)
qf.add_sma(periods = 20)
qf.add_macd()
qf.add_volume()
qf.add_dmi()


# In[ ]:


qf.iplot(title = "AAPL", name = "AAPL")


# In[ ]:




