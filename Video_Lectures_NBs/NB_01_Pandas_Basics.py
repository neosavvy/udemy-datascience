#!/usr/bin/env python
# coding: utf-8

# # Pandas: Basics

# ### First Steps

# In[ ]:


import pandas as pd
pd.options.display.max_rows = 60
pd.options.display.min_rows = None


# In[ ]:


pd.read_csv("titanic.csv")


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic


# In[ ]:


print(titanic)


# In[ ]:


titanic.head(2)


# In[ ]:


titanic.head(10)


# In[ ]:


titanic.tail(2)


# In[ ]:


titanic.tail(10)


# In[ ]:


titanic.columns


# In[ ]:


titanic.index


# In[ ]:


titanic.info()


# In[ ]:


titanic.shape


# In[ ]:


titanic.describe()


# In[ ]:





# ### Built-in Functions, Attributes and Methods

# In[ ]:


titanic.head()


# In[ ]:


type(titanic)


# #### DataFrame and Built-in Functions

# In[ ]:


len(titanic)


# In[ ]:


round(titanic, 0).head()


# In[ ]:


#int(titanic)


# In[ ]:


min(titanic)


# #### DataFrame Attributes

# In[ ]:


titanic.shape


# In[ ]:


titanic.size


# In[ ]:


titanic.index


# In[ ]:


titanic.columns


# #### DataFrame Methods
# 

# In[ ]:


titanic.head()


# In[ ]:


titanic.info()


# In[ ]:


titanic.min()


# In[ ]:





# ### Selecting Columns

# In[ ]:


titanic.head()


# In[ ]:


titanic["age"]


# In[ ]:


type(titanic["age"])


# In[ ]:


titanic[["age"]]


# In[ ]:


type(titanic[["age"]])


# In[ ]:


#titanic["age", "sex"]


# In[ ]:


titanic[["age", "sex"]]


# In[ ]:


titanic[["sex", "age"]]


# In[ ]:


titanic[["sex", "age", "fare"]]


# In[ ]:


titanic.age


# In[ ]:


titanic.age.equals(titanic["age"])


# In[ ]:





# ### Selecting Rows with Square Brackets (not advisable)

# In[ ]:


titanic.head()


# In[ ]:


#titanic[0]


# In[ ]:


titanic[0:1]


# In[ ]:


titanic[4:5]


# In[ ]:


titanic[:10]


# In[ ]:


titanic.head(10)


# In[ ]:


titanic[-10:]


# In[ ]:





# ### Indexing Operator iloc (location based indexing) 

# In[ ]:


medals = pd.read_csv("summer.csv")


# In[ ]:


medals.head()


# In[ ]:


medals.tail()


# In[ ]:


medals.info()


# #### Selecting Rows with iloc

# In[ ]:


medals.iloc[0]


# In[ ]:


type(medals.iloc[0])


# In[ ]:


medals.iloc[1]


# In[ ]:


medals.iloc[-1]


# In[ ]:


medals.iloc[:5]


# In[ ]:


medals.iloc[-5:]


# In[ ]:


medals.iloc[456:459]


# In[ ]:


medals.iloc[[2,45,765]]


# #### Slicing Rows and Columns with iloc

# In[ ]:


medals.head()


# In[ ]:


medals.iloc[0,4]


# In[ ]:


medals.iloc[0,0:3]


# In[ ]:


medals.iloc[0,[0,2,6,8]]


# In[ ]:


medals.iloc[34:39,[0,2,6,8]]


# #### Selecting Columns with iloc

# In[ ]:


medals.iloc[:, 4].equals(medals.Athlete)


# In[ ]:


medals["Athlete"]


# In[ ]:





# ### Index Operator loc (label based indexing)

# In[ ]:


medals = pd.read_csv("summer.csv", index_col="Athlete")


# In[ ]:


medals.head()


# #### Selecting Rows with loc

# In[ ]:


medals.iloc[2]


# In[ ]:


medals.loc["DRIVAS, Dimitrios"]


# In[ ]:


medals.loc["PHELPS, Michael"]


# In[ ]:


medals.loc["PHELPS, Michael"].iloc[0]


# #### Slicing Rows and Columns with loc

# In[ ]:


medals.loc["PHELPS, Michael", "Medal"]


# In[ ]:


medals.loc["PHELPS, Michael", ["Event","Medal"]]


# In[ ]:


medals.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Event","Medal"]]


# In[ ]:


medals.head(10)


# In[ ]:


medals.loc[:"CHASAPIS, Spiridon"]


# In[ ]:


#medals.loc[:"PHELPS, Michael"]


# In[ ]:


#medals.loc["HAJOS, Alfred":]


# In[ ]:


medals.head(20)


# In[ ]:


medals.loc["DRIVAS, Dimitrios":"BLAKE, Arthur"]


# In[ ]:


medals.loc["HAJOS, Alfred", "Year":"Discipline"]


# In[ ]:


medals.loc[["PHELPS, Michael", "DUCK, Donald"]]


# In[ ]:


medals.loc["PHELPS, Michael", ["Year", "Age"]]


# In[ ]:





# ## Summary and Outlook

# #### Importing from CSV and first Inspection

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv")


# In[ ]:


summer.head()


# In[ ]:


summer.tail()


# In[ ]:


summer.info()


# #### Selecting one Column

# In[ ]:


summer.Athlete


# In[ ]:


summer["Athlete"]


# #### Selecting multiple Columns

# In[ ]:


summer[["Year", "Medal"]].loc[1]


# In[ ]:


summer.loc[1, ["Year", "Medal"]]


# #### Selecting positional rows

# In[ ]:


summer.iloc[10:21]


# #### Selecting labeled rows

# In[ ]:


summer = pd.read_csv("summer.csv", index_col = "Athlete")


# In[ ]:


summer.head()


# In[ ]:


summer.loc["LEWIS, Carl"]


# #### Putting it all together

# In[ ]:


summer[["Year", "Event", "Medal"]].loc["LEWIS, Carl"]


# In[ ]:


summer.loc["LEWIS, Carl"][["Year", "Event", "Medal"]]


# In[ ]:


summer.loc["LEWIS, Carl", ["Year", "Event", "Medal"]]


# #### Outlook Pandas Objects

# In[ ]:


summer.head()


# In[ ]:


type(summer)


# In[ ]:


summer["Year"]


# In[ ]:


type(summer["Year"])


# In[ ]:


summer.columns


# In[ ]:


type(summer.columns)


# In[ ]:


summer.index


# In[ ]:


type(summer.index)


# In[ ]:




