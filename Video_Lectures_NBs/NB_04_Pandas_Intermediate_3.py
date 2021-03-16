#!/usr/bin/env python
# coding: utf-8

# # Pandas: Intermediate (Part 3)

# ## Intro to NA Values

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


sales = pd.read_csv("sales.csv", index_col = 0)


# In[ ]:


sales


# In[ ]:


sales.info()


# In[ ]:


sales.loc["Steven", "Thu"]


# In[ ]:


sales.iloc[1,1] = None


# In[ ]:


sales


# In[ ]:


sales.iloc[2,2] = np.nan


# In[ ]:


sales


# In[ ]:


sales.info()


# In[ ]:





# ## Handling NA Values / missing Values

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.info()


# In[ ]:


titanic.isna().sum()


# In[ ]:


titanic.notna().sum()


# In[ ]:


titanic.loc[titanic.embarked.isna()]


# In[ ]:


titanic.shape


# In[ ]:


titanic.dropna()


# In[ ]:


titanic.dropna().shape


# In[ ]:


titanic.dropna(how = "all").shape


# In[ ]:


titanic.dropna(axis = 1, how = "any").shape


# In[ ]:


titanic.dropna(axis = 1, thresh = 500).shape


# In[ ]:


titanic.dropna(axis = 1, thresh = 500, inplace = True)


# In[ ]:


titanic.info()


# In[ ]:


titanic.loc[titanic.age.isna()]


# In[ ]:


mean_age = titanic.age.mean()
mean_age


# In[ ]:


titanic.age.fillna(value = mean_age, inplace = True)


# In[ ]:


titanic.age


# In[ ]:


titanic.info()


# In[ ]:





# ## Exporting DataFrames to csv

# In[ ]:


titanic.head()


# In[ ]:


titanic.to_csv("clean_df.csv", index = False)


# In[ ]:


pd.read_csv("clean_df.csv")


# In[ ]:





# ## Summary Statistics and Accumulations

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.describe()


# In[ ]:


titanic.count(axis = "columns")


# In[ ]:


titanic.count(axis = 1)


# In[ ]:


titanic.mean(axis = 1)


# In[ ]:


titanic.sum(axis = 0)


# In[ ]:


titanic.head()


# In[ ]:


titanic.fare.cumsum(axis = 0)


# In[ ]:


titanic.corr()


# In[ ]:


titanic.survived.corr(titanic.pclass)


# In[ ]:





# ## The agg() method

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.describe()


# In[ ]:


titanic.mean()


# In[ ]:


titanic.agg("mean")


# In[ ]:


titanic.agg(["mean", "std"])


# In[ ]:


titanic.agg(["mean", "std", "min", "max", "median"])


# In[ ]:


titanic.agg({"survived": "mean", "age":["min", "max"]})


# In[ ]:




