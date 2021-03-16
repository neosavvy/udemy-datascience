#!/usr/bin/env python
# coding: utf-8

# # PART 4: Advanced Topics

# ## Helpful DatetimeIndex Attributes and Methods

# In[ ]:


import pandas as pd


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0])


# In[ ]:


stocks.head()


# In[ ]:


close = stocks.loc[:, "Close"].copy()


# In[ ]:


close.head()


# In[ ]:


close.info()


# In[ ]:


close.index


# In[ ]:


close.index.day


# In[ ]:


close.index.month


# In[ ]:


close.index.year


# In[ ]:


close.index.day_name()


# In[ ]:


close.index.weekday_name


# In[ ]:


close.index.month_name()


# In[ ]:


close.index.weekday


# In[ ]:


close.index.quarter


# In[ ]:


close.index.days_in_month


# In[ ]:


close.index.week


# In[ ]:


close.index.weekofyear


# In[ ]:


close.index.is_month_end


# In[ ]:


close["Day"] = stocks.index.day_name()
close["Quarter"] = stocks.index.quarter


# In[ ]:


close.head()


# In[ ]:





# ## Filling NA Values with bfill, ffill and interpolation

# In[ ]:


close.head()


# In[ ]:


close.tail()


# In[ ]:


all_days = pd.date_range(start = "2009-12-31", end = "2019-02-06", freq = "D")
all_days


# In[ ]:


close = close.reindex(all_days)


# In[ ]:


close.head(20)


# In[ ]:


close.Day = close.index.weekday_name
close.Quarter = close.index.quarter


# In[ ]:


close.fillna(method = "ffill", inplace= True)


# In[ ]:


close.head(15)


# In[ ]:


temp = pd.read_csv("temp.csv", parse_dates=["datetime"], index_col = "datetime")


# In[ ]:


temp.head(10)


# In[ ]:


temp = temp.resample("30 Min").mean()
temp.head(10)


# In[ ]:


temp.interpolate()


# In[ ]:





# ## resample() and agg()

# In[ ]:


import pandas as pd


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


stocks.resample("A", kind = "period").first()


# In[ ]:


stocks.resample("A", kind = "period").max()


# In[ ]:


stocks.resample("A", kind = "period").min()


# In[ ]:


stocks.resample("A", kind = "period").last()


# In[ ]:


stocks.resample("A", kind = "period").mean()


# In[ ]:


stocks.resample("A", kind = "period").agg(["first", "last"])


# In[ ]:


stocks.resample("A", kind = "period").agg({"AAPL": "first", "BA": "last", "DIS":["min", "max"]})


# In[ ]:





# ## resample() and ohlc()

# In[ ]:


import pandas as pd


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


stocks.resample("A", kind = "period").ohlc()


# In[ ]:





# ## Upsampling with resample()

# In[ ]:


import pandas as pd


# In[ ]:


stocks = pd.read_csv("stocks.csv", header = [0,1], index_col= [0], parse_dates= [0]).Close


# In[ ]:


stocks.head()


# In[ ]:


res_obj = stocks.resample("D")
res_obj


# In[ ]:


res_obj.asfreq()


# In[ ]:


res_obj.ffill()


# In[ ]:


res_obj.bfill()


# In[ ]:


res_obj.bfill(limit = 2)


# In[ ]:


res_obj.asfreq()


# In[ ]:


res_obj.interpolate()


# In[ ]:


stocks.resample("12H").asfreq()


# In[ ]:





# ## Timezones and Converting (Part 1)

# In[ ]:


import pandas as pd


# In[ ]:


ge = pd.read_csv("GE_prices.csv", parse_dates= ["date"], index_col= "date")


# In[ ]:


ge.head(30)


# In[ ]:


ge.info()


# In[ ]:


ge.index


# In[ ]:


print(ge.index.tz)


# In[ ]:


ge.tz_localize("UTC")


# In[ ]:


ge.tz_localize("America/New_York")


# In[ ]:


ge = ge.tz_localize("America/New_York")


# In[ ]:


ge.head()


# ## Timezones and Converting (Part 2)

# In[ ]:


ge.index.tz


# In[ ]:


ge.tz_convert("UTC")


# In[ ]:


ge.tz_convert("America/Los_Angeles")


# In[ ]:


ge_la = ge.tz_convert("America/Los_Angeles")


# In[ ]:


ge_la.head()


# In[ ]:


ge.head()


# In[ ]:


comb = pd.concat([ge, ge_la], axis = 1)


# In[ ]:


comb.head()


# In[ ]:


comb.index


# In[ ]:


comb["NY_time"] = comb.index.tz_convert("America/New_York")
comb["LA_time"] = comb.index.tz_convert("America/Los_Angeles")


# In[ ]:


comb.head()


# In[ ]:


import pytz


# In[ ]:


len(pytz.all_timezones)


# In[ ]:


pytz.common_timezones


# In[ ]:





# ## Shifting Dates with pd.DateOffeset()

# In[ ]:


import pandas as pd


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date")


# In[ ]:


SP500.index


# In[ ]:


#SP500.index + 2 


# In[ ]:


pd.DateOffset(days = 2)


# In[ ]:


type(pd.DateOffset(days = 2))


# In[ ]:


SP500.index


# In[ ]:


SP500.index + pd.DateOffset(days = 2)


# In[ ]:


SP500.index + pd.DateOffset(weeks = 3)


# In[ ]:


SP500.index + pd.DateOffset(months = 3)


# In[ ]:


SP500.index + pd.DateOffset(years = 10)


# In[ ]:


SP500.index + pd.DateOffset(years = 1, months = 2, days = 15, hours = 12, minutes = 30)


# In[ ]:


SP500.index - pd.DateOffset(days = 1)


# In[ ]:





# ## Advanced Time Shifting Methods

# In[ ]:


import pandas as pd


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date")


# In[ ]:


SP500.head()


# In[ ]:


SP500.index


# In[ ]:


pd.tseries.offsets.MonthEnd()


# In[ ]:


SP500.index + pd.tseries.offsets.MonthEnd()


# In[ ]:


SP500.index + pd.tseries.offsets.MonthEnd(n = 2)


# In[ ]:


SP500.index - pd.tseries.offsets.MonthEnd()


# In[ ]:


SP500.index + pd.tseries.offsets.BMonthEnd()


# In[ ]:


SP500.index + pd.tseries.offsets.QuarterEnd()


# In[ ]:


SP500.index + pd.tseries.offsets.YearBegin(2)


# In[ ]:





# ## The TimeDelta Object

# In[ ]:


import pandas as pd


# In[ ]:


aug = pd.to_datetime("2015-08-15")
aug


# In[ ]:


sep = pd.to_datetime("2015-09-02")
sep


# In[ ]:


delta = sep - aug
delta


# In[ ]:


type(delta)


# In[ ]:


aug + delta


# In[ ]:


sep - delta


# In[ ]:


aug - sep


# In[ ]:


pd.to_timedelta("1 Days")


# In[ ]:


pd.to_timedelta("10 days")


# In[ ]:


pd.to_timedelta("2 hours")


# In[ ]:


pd.to_timedelta("5 minutes")


# In[ ]:


pd.to_timedelta("29 seconds")


# In[ ]:


pd.to_timedelta("10 days, 2 hours, 5 minutes, 30 seconds")


# In[ ]:


pd.to_timedelta("10 D")


# In[ ]:


pd.to_timedelta("1 Y")


# In[ ]:


pd.to_timedelta("1 W")


# In[ ]:


pd.to_timedelta("1 M")


# In[ ]:


SP500 = pd.read_csv("SP500.csv", parse_dates= ["Date"], index_col= "Date")


# In[ ]:


SP500.head()


# In[ ]:


SP500["BQE"] = SP500.index + pd.tseries.offsets.BQuarterEnd()


# In[ ]:


SP500.head()


# In[ ]:


SP500["TDelta"] = SP500["BQE"] - SP500.index


# In[ ]:


SP500.head()


# In[ ]:


SP500.info()


# In[ ]:


SP500 = SP500.reset_index().set_index("TDelta")


# In[ ]:


SP500


# In[ ]:


SP500.info()


# In[ ]:


(SP500["BQE"] - SP500.index).equals(SP500["Date"])


# In[ ]:




