#!/usr/bin/env python
# coding: utf-8

# # Pandas: Advanced Topics (Part 2)

# ## Understanding GroupBy objects

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.tail()


# In[ ]:


titanic.info()


# In[ ]:


titanic_slice = titanic.iloc[:10, [2,3]]


# In[ ]:


titanic_slice


# In[ ]:


titanic_slice.groupby("sex")


# In[ ]:


gbo = titanic_slice.groupby("sex")


# In[ ]:


type(gbo)


# In[ ]:


gbo.groups


# In[ ]:


l = list(gbo)


# In[ ]:


l


# In[ ]:


len(l)


# In[ ]:


l[0]


# In[ ]:


type(l[0])


# In[ ]:


l[0][0]


# In[ ]:


l[0][1]


# In[ ]:


type(l[0][1])


# In[ ]:


l[1]


# In[ ]:


titanic_slice.loc[titanic_slice.sex == "female"]


# In[ ]:


titanic_slice_f = titanic_slice.loc[titanic_slice.sex == "female"]
titanic_slice_f


# In[ ]:


titanic_slice_m = titanic_slice.loc[titanic_slice.sex == "male"]
titanic_slice_m


# In[ ]:


titanic_slice_f.equals(l[0][1])


# In[ ]:


for element in gbo:
    print(element[1])


# In[ ]:





# ## Splitting with many Keys

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv")


# In[ ]:


summer.head()


# In[ ]:


summer.info()


# In[ ]:


summer.Country.nunique()


# In[ ]:


split1 = summer.groupby("Country")


# In[ ]:


l = list(split1)
l


# In[ ]:


len(l)


# In[ ]:


l[100][1]


# In[ ]:


split2 = summer.groupby(by = ["Country", "Gender"])


# In[ ]:


l2 = list(split2)
l2


# In[ ]:


len(l2)


# In[ ]:


l2[104]


# In[ ]:


l2[104][0]


# In[ ]:


l2[104][1]


# In[ ]:





# ## split-apply-combine explained

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic_slice = titanic.iloc[:10, [2,3]]


# In[ ]:


titanic_slice


# In[ ]:


list(titanic_slice.groupby("sex"))[0][1]


# In[ ]:


list(titanic_slice.groupby("sex"))[1][1]


# In[ ]:


titanic_slice.groupby("sex").mean()


# In[ ]:


titanic.groupby("sex").survived.sum()


# In[ ]:


titanic.groupby("sex")[["fare", "age"]].max()


# In[ ]:


new_df = titanic.groupby("sex").mean()


# In[ ]:


new_df


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


new_df.plot(kind = "bar", subplots = True, figsize = (8,15), fontsize = 13)
plt.show()


# In[ ]:





# ## split-apply-combine applied

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv")


# In[ ]:


summer.head()


# In[ ]:


summer.info()


# In[ ]:


medals_per_country = summer.groupby("Country").Medal.count().nlargest(n = 20)
medals_per_country


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


medals_per_country.plot(kind = "bar", figsize = (14, 8), fontsize = 14)
plt.xlabel("Country", fontsize = 13)
plt.ylabel("No. of Medals", fontsize = 13)
plt.title("Summer Olympic Games (Total Medals per Country)", fontsize = 16)
plt.show()


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.info()


# In[ ]:


titanic.describe()


# In[ ]:


titanic.fare.mean()


# In[ ]:


titanic.groupby("pclass").fare.mean()


# In[ ]:


titanic.survived.sum()


# In[ ]:


titanic.survived.mean()


# In[ ]:


titanic.groupby("sex").survived.mean()


# In[ ]:


titanic.groupby("pclass").survived.mean()


# In[ ]:


titanic["ad_chi"] = "adult"


# In[ ]:


titanic.loc[titanic.age < 18, "ad_chi"] = "child"


# In[ ]:


titanic.head(20)


# In[ ]:


titanic.ad_chi.value_counts()


# In[ ]:


titanic.groupby("ad_chi").survived.mean()


# In[ ]:


titanic.groupby(["sex", "ad_chi"]).survived.count()


# In[ ]:


titanic.groupby(["sex", "ad_chi"]).survived.mean().sort_values(ascending = False)


# In[ ]:


w_and_c_first = titanic.groupby(["sex", "ad_chi"]).survived.mean().sort_values(ascending = False)


# In[ ]:


w_and_c_first.plot(kind = "bar", figsize = (14,8), fontsize = 14)
plt.xlabel("Groups", fontsize = 13)
plt.ylabel("Survival Rate", fontsize = 13)
plt.title("Titanic Survival Rate by Sex/Age-Groups", fontsize = 16)
plt.show()


# In[ ]:





# ## Hierarchical Indexing (MultiIndex) with Groupby

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv", usecols = ["survived", "pclass", "sex", "age", "fare"])


# In[ ]:


titanic


# In[ ]:


summary = titanic.groupby(["sex", "pclass"]).mean()


# In[ ]:


summary


# In[ ]:


summary.index


# In[ ]:


summary.loc[("female", 2), :]


# In[ ]:


summary.loc[("female", 2), "age"]


# In[ ]:


summary.swaplevel().sort_index()


# In[ ]:


summary.reset_index()


# In[ ]:





# ## stack() and unstack()

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv")


# In[ ]:


summer.head()


# In[ ]:


medals_by_country = summer.groupby(["Country", "Medal"]).Medal.count()


# In[ ]:


medals_by_country


# In[ ]:


medals_by_country.loc[("USA", "Gold")]


# In[ ]:


medals_by_country.shape


# In[ ]:


medals_by_country.unstack(level = -1)


# In[ ]:


medals_by_country = medals_by_country.unstack(level = -1, fill_value= 0)


# In[ ]:


medals_by_country.head()


# In[ ]:


medals_by_country.shape


# In[ ]:


medals_by_country = medals_by_country[["Gold", "Silver", "Bronze"]]


# In[ ]:


medals_by_country.sort_values(by = ["Gold", "Silver", "Bronze"], ascending = [False, False, False], inplace = True)


# In[ ]:


medals_by_country.head(10)


# In[ ]:


import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


medals_by_country.head(10).plot(kind = "bar", figsize = (12,8), fontsize = 13)
plt.xlabel("Country", fontsize = 13)
plt.ylabel("Medals", fontsize = 13)
plt.title("Medals per Country", fontsize = 16)
plt.legend(fontsize = 15)
plt.show()


# In[ ]:


medals_by_country.stack().unstack()


# In[ ]:




