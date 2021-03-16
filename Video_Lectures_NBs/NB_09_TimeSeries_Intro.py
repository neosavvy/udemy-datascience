#!/usr/bin/env python
# coding: utf-8

# # Time Series Basics

# ## Importing Time Series Data from csv-Files

# In[ ]:


import pandas as pd


# In[ ]:


temp = pd.read_csv("temp.csv", parse_dates = ["datetime"], index_col= "datetime")


# In[ ]:


temp.head()


# In[ ]:


temp.info()


# In[ ]:


type(temp.iloc[0, 0])


# In[ ]:


temp.index


# In[ ]:


temp.index[0]


# In[ ]:





# ## Converting strings to datetime objects with pd.to_datetime()

# In[ ]:


import pandas as pd


# In[ ]:


temp = pd.read_csv("temp.csv")


# In[ ]:


temp.head()


# In[ ]:


temp.info()


# In[ ]:


temp.datetime[0]


# In[ ]:


pd.to_datetime(temp.datetime)


# In[ ]:


temp = temp.set_index(pd.to_datetime(temp.datetime)).drop("datetime", axis = 1)


# In[ ]:


temp.head()


# In[ ]:


temp.info()


# In[ ]:


temp.index[0]


# In[ ]:


pd.to_datetime("2015-05-20 10:30:20")


# In[ ]:


pd.to_datetime("20150520")


# In[ ]:


pd.to_datetime("2015/05/20")


# In[ ]:


pd.to_datetime("2015 05 20")


# In[ ]:


#pd.to_datetime("2015-20-05")


# In[ ]:


pd.to_datetime("2015 May 20")


# In[ ]:


pd.to_datetime("May 2015 20")


# In[ ]:


pd.to_datetime("2015 20th may")


# In[ ]:


pd.to_datetime(["2015-05-20", "Feb 20 2015"])


# In[ ]:


pd.to_datetime(["2015-05-20", "Feb 20 2015", "Elephant"], errors="coerce")


# In[ ]:





# ## Initial Analysis / Visual Inspection of Time Series

# In[ ]:


temp.head()


# In[ ]:


temp.tail()


# In[ ]:


temp.info()


# In[ ]:


temp.describe()


# In[ ]:


temp.LA.value_counts()


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


temp.plot(figsize = (15, 7), subplots=True, layout=(1, 2), sharey=True)
plt.show()


# In[ ]:





# ## Indexing and Slicing Time Series

# In[ ]:


import pandas as pd


# In[ ]:


temp = pd.read_csv("temp.csv", parse_dates= ["datetime"], index_col= "datetime")


# In[ ]:


temp.head()


# In[ ]:


temp.info()


# In[ ]:


temp.loc["2013-01-01 01:00:00"]


# In[ ]:


temp.loc["2015"]


# In[ ]:


temp.loc["2015-05"]


# In[ ]:


temp.loc["2015-05-20"].shape


# In[ ]:


temp.loc["2015-05-20 10:00:00"]


# In[ ]:


#temp.loc["2015-05-20 10:30:00"]


# In[ ]:


temp.loc["2015-01-01" : "2015-12-31"]


# In[ ]:


temp.loc["2015-01-01" : "2015-12-31"].equals(temp.loc["2015"])


# In[ ]:


temp.loc["2015-04-15" : "2016-02-23"]


# In[ ]:


temp.loc["2015-05-20":]


# In[ ]:


temp.loc[:"2015-05-20"]


# In[ ]:


temp.loc["20FEBRUARY2015"]


# In[ ]:


#temp.loc[["2015-05-20 10:00:00", "2015-05-20 12:00:00"]]


# In[ ]:


two_timestamps = pd.to_datetime(["2015-05-20 10:00:00", "2015-05-20 12:00:00"])
two_timestamps


# In[ ]:


temp.loc[two_timestamps]


# In[ ]:





# ## Creating a customized DatetimeIndex with pd.date_range()

# In[ ]:


import pandas as pd


# In[ ]:


pd.to_datetime(["2015-05-20", "Feb 20 2015"])


# In[ ]:


pd.date_range(start = "2015-07-01", end = "2015-07-31", freq= "D")


# In[ ]:


pd.date_range(start = "2015-07-01", periods = 31, freq = "D")


# In[ ]:


pd.date_range(end = "2015-07-31", periods = 31, freq = "D")


# In[ ]:


pd.date_range(start = "2015-07-01", end = "2015-07-31", freq = "B")


# In[ ]:


pd.date_range(start = "2015-07-31", periods = 10, freq = "H")


# In[ ]:


pd.date_range(start = "2015-07-01", periods = 6,  freq = "W")


# In[ ]:


pd.date_range(start = "2015-07-01", periods = 6,  freq = "W-Wed")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "M")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "MS")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = pd.DateOffset(months = 1))


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "Q")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "QS")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "QS-May")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "A")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "AS")


# In[ ]:


pd.date_range(start = "2015-07-14", periods = 6,  freq = "AS-Jul")


# In[ ]:


pd.date_range(end = "2018-11-24", periods = 10,  freq = pd.DateOffset(years = 1))


# In[ ]:





# ## More on pd.date_range()

# In[ ]:


import pandas as pd


# In[ ]:


pd.date_range(start = "2015-07-01", periods = 10, freq = "3D8H")


# In[ ]:





# ## Downsampling Time Series with resample() (Part 1)

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


temp = pd.read_csv("temp.csv", parse_dates= ["datetime"], index_col = "datetime")


# In[ ]:


temp.head()


# In[ ]:


temp.info()


# In[ ]:


list(temp.resample("D"))[1][1]


# In[ ]:


temp.head(25)


# In[ ]:


temp.resample("D").sum()


# In[ ]:


temp.resample("2H").first()


# In[ ]:


temp.resample("W").mean()


# In[ ]:


temp.resample("W-Wed").mean()


# In[ ]:


temp.resample("M").mean()


# In[ ]:


temp.resample("MS").mean()


# In[ ]:


temp.resample("MS", loffset="14D").mean()


# In[ ]:


temp.resample("Q").mean()


# In[ ]:


temp.resample("Q-Feb").mean()


# In[ ]:


temp.resample("Y").mean()


# In[ ]:


temp.resample("YS").mean()


# In[ ]:





# ## Downsampling Time Series with resample (Part 2)

# In[ ]:


temp.resample("M", kind = "period").mean()


# In[ ]:


temp.resample("W", kind = "period").mean()


# In[ ]:


temp.resample("Q", kind = "period").mean()


# In[ ]:


temp.resample("A", kind = "period").mean()


# In[ ]:


temp_m = temp.resample("M", kind = "period").mean()


# In[ ]:


temp_m


# In[ ]:


temp_m.info()


# In[ ]:


temp_m.index[0]


# In[ ]:


temp_m.plot(figsize = (15, 8), fontsize = 15)
plt.show()


# In[ ]:


temp.plot(figsize = (15, 8), fontsize = 15)
plt.show()


# In[ ]:





# ## The PeriodIndex Object

# In[ ]:


import pandas as pd


# In[ ]:


temp = pd.read_csv("temp.csv", parse_dates= ["datetime"], index_col = "datetime")


# In[ ]:


temp.head()


# In[ ]:


temp.tail()


# In[ ]:


temp.info()


# In[ ]:


temp_m = temp.resample("M", kind = "period").mean()
temp_m.head(12)


# In[ ]:


temp_m.info()


# In[ ]:


temp_m.index


# In[ ]:


temp_m.loc["2013-01"]


# In[ ]:


temp_m.loc["2013-05":"2013-08"]


# In[ ]:


temp_m.loc["2013"]


# In[ ]:


temp_m.to_timestamp(how = "start")


# In[ ]:





# ## Advanced Indexing with reindex()

# In[ ]:


import pandas as pd


# In[ ]:


temp = pd.read_csv("temp.csv", parse_dates= ["datetime"], index_col = "datetime")


# In[ ]:


temp.head()


# In[ ]:


temp.tail()


# In[ ]:


temp_d = temp.resample("D").mean()
temp_d


# In[ ]:


birthd = pd.date_range(end = "2018-12-24", periods = 10,  freq = pd.DateOffset(years = 1))
birthd


# In[ ]:


temp_d.loc[birthd]


# In[ ]:


temp_d.reindex(birthd)


# In[ ]:


temp_d.head()


# In[ ]:


temp_d.tail()


# In[ ]:




