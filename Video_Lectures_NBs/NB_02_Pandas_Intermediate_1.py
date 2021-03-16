#!/usr/bin/env python
# coding: utf-8

# # Pandas: Intermediate (Part 1)

# ## First Steps with Pandas Series

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.info()


# In[ ]:


titanic["age"]


# In[ ]:


type(titanic["age"])


# In[ ]:


titanic["age"].equals(titanic.age)


# In[ ]:


age = titanic["age"]


# In[ ]:


age.head(n=2)


# In[ ]:


age.tail()


# In[ ]:


age.dtype


# In[ ]:


#age.info()


# In[ ]:


age.shape


# In[ ]:


len(age)


# In[ ]:


age.index


# In[ ]:


age.describe()


# In[ ]:





# ##  Analyzing Numerical Series

# In[ ]:


age.dtype


# In[ ]:


age.count()


# In[ ]:


age.size


# In[ ]:


len(age)


# In[ ]:


age.sum(skipna=True)


# In[ ]:


sum(age)


# In[ ]:


age.mean(skipna = True)


# In[ ]:


age.std()


# In[ ]:


age.min()


# In[ ]:


age.max()


# In[ ]:


#age.ptp() ##deprecated##


# In[ ]:


age.median()


# In[ ]:


age.unique()


# In[ ]:


len(age.unique())


# In[ ]:


age.nunique(dropna = False)


# In[ ]:


age.value_counts()


# In[ ]:


age.value_counts(dropna = False)


# In[ ]:


age.value_counts(dropna = True, sort = True, ascending = False)


# In[ ]:


age.value_counts(dropna = True, sort = True, ascending = False, normalize = True)


# In[ ]:


age.value_counts(dropna = True, sort = True, ascending= False, bins = 5).head()


# In[ ]:





# ## Analyzing non-numerical Series

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv")


# In[ ]:


summer.head()


# In[ ]:


summer.info()


# In[ ]:


athlete = summer["Athlete"]


# In[ ]:


athlete.head()


# In[ ]:


athlete.tail(5)


# In[ ]:


type(athlete)


# In[ ]:


athlete.dtype


# In[ ]:


athlete.shape


# In[ ]:


athlete.describe()


# In[ ]:


athlete.size


# In[ ]:


athlete.count()


# In[ ]:


athlete.min()


# In[ ]:


athlete.unique()


# In[ ]:


len(athlete.unique())


# In[ ]:


athlete.nunique(dropna= False)


# In[ ]:


athlete.value_counts()


# In[ ]:


athlete.value_counts(sort = True, ascending=True)


# In[ ]:


athlete.value_counts(sort = True, ascending=False, normalize = True).head()


# In[ ]:





# ## The copy() method 

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


age = titanic.age.copy()


# In[ ]:


age.head()


# In[ ]:


age.iloc[2] = 29


# In[ ]:


age.head()


# In[ ]:


titanic.head()


# In[ ]:





# ## Sorting and introduction to the  inplace-parameter

# In[ ]:


import pandas as pd


# In[ ]:


dic = {1:10, 3:25, 2:6, 4:36, 5:2, 6:0, 7:None}
dic


# In[ ]:


sales = pd.Series(dic)
sales


# In[ ]:


sales.sort_index()


# In[ ]:


sales.sort_index(ascending = True, inplace= True)


# In[ ]:


sales


# In[ ]:


sales.sort_values(inplace=False)


# In[ ]:


sales.sort_values(ascending=False, na_position="last", inplace= True)


# In[ ]:


sales


# In[ ]:


dic = {"Mon":10, "Tue":25, "Wed":6, "Thu": 36, "Fri": 2}
dic


# In[ ]:


sales = pd.Series(dic)


# In[ ]:


sales


# In[ ]:


sales.sort_index(ascending=False)


# In[ ]:





# ## First Steps with Pandas Index Objects

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv", index_col="Athlete")


# In[ ]:


summer.head()


# In[ ]:


summer.tail()


# In[ ]:


summer.info()


# In[ ]:


summer.index


# In[ ]:


type(summer.index)


# In[ ]:


summer.columns


# In[ ]:


type(summer.columns)


# In[ ]:


summer.axes


# In[ ]:


summer.columns[:3]


# In[ ]:


summer.index[0]


# In[ ]:


summer.index[-1]


# In[ ]:


summer.index[100:102]


# In[ ]:


summer.columns.tolist()


# In[ ]:


summer.index.is_unique


# In[ ]:


summer.index.get_loc("DRIVAS, Dimitrios")


# In[ ]:





# ## Changing Row Index Labels

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv", index_col="Athlete")


# In[ ]:


summer.head()


# In[ ]:


summer.index


# In[ ]:


summer.reset_index(drop = False, inplace=True)


# In[ ]:


summer.head()


# In[ ]:


summer.set_index("Year", drop = True, inplace = True)


# In[ ]:


summer.head()


# In[ ]:


summer.index.is_unique


# In[ ]:


#summer.index[0] = 1894


# In[ ]:


#summer.index = "Before 2016"


# In[ ]:


summer.index.size


# In[ ]:


new_index = ["Medal_No{}".format(i) for i in range(1,summer.index.size+1)]
new_index


# In[ ]:


summer.index = new_index


# In[ ]:


summer.head()


# In[ ]:


summer.tail()


# In[ ]:


summer.index.is_unique


# In[ ]:


summer.index.name = "Medal_No"


# In[ ]:


summer.reset_index()


# In[ ]:





# ## Changing Column Labels

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.tail()


# In[ ]:


titanic.columns


# In[ ]:


titanic.columns[0]


# In[ ]:


#titanic.columns[0] = "Alive"


# In[ ]:


titanic.columns = ["Alive", "Class", "Sex", "Age", "SibSp", "ParChi", "Fare", "Emb", "Deck"]


# In[ ]:


titanic.head()


# In[ ]:


titanic.columns.name


# In[ ]:


titanic.columns.name = "Pass_Charact"


# In[ ]:


titanic.head()


# In[ ]:


titanic.index.name = "Passenger_no"


# In[ ]:





# ## Renaming Index & Column Labels

# In[ ]:


import pandas as pd


# In[ ]:


summer= pd.read_csv("summer.csv", index_col = "Athlete")


# In[ ]:


summer.head()


# In[ ]:


#summer.index[0] = 'HAYOS, Alfred'


# In[ ]:


summer.rename({"HAJOS, Alfred":'HAYOS, Alfred'}, axis = "index", inplace= True)


# In[ ]:


summer.head()


# In[ ]:


summer.rename({"Gender":'Sex', "City":"Host_City"}, axis = "columns", inplace=True)


# In[ ]:


summer.head()


# In[ ]:





# In[ ]:




