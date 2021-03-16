#!/usr/bin/env python
# coding: utf-8

# # Pandas: Intermediate (Part 2)

# ## Sorting DataFrames with sort_index() and sort_values()

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.tail()


# In[ ]:


titanic.age.sort_values()


# In[ ]:


titanic.sort_values("age")


# In[ ]:


titanic.head()


# In[ ]:


titanic.sort_values("age", axis = 0, ascending = True, inplace = True)


# In[ ]:


titanic.head()


# In[ ]:


titanic.sort_values(["pclass", "sex", "age"], ascending = [True, False, True], inplace= True)


# In[ ]:


titanic.head()


# In[ ]:


titanic.tail()


# In[ ]:


titanic.sort_index(ascending=True, inplace = True)


# In[ ]:


titanic.head()


# In[ ]:





# ## nunique(), nlargest() and nsmallest() with DataFrames

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.tail()


# In[ ]:


titanic.age.unique()


# In[ ]:


titanic.nunique(axis = 1, dropna=False)


# In[ ]:


titanic.nunique(dropna = False)


# In[ ]:


titanic.nlargest(n = 5, columns = "fare")


# In[ ]:


titanic.sort_values("fare", ascending = False).head(5)


# In[ ]:


titanic.nsmallest(n = 1, columns = "age")


# In[ ]:


titanic.loc[titanic.age.idxmin()]


# In[ ]:





# ## Filtering DataFrames with one Condition

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head(10)


# In[ ]:


titanic.sex.head(10)


# In[ ]:


titanic.sex == "male"


# In[ ]:


titanic[titanic.sex == "male"]["fare"]


# In[ ]:


titanic.loc[titanic.sex == "male", "fare"]


# In[ ]:


mask1 = titanic.sex == "male"
mask1


# In[ ]:


titanic_male = titanic.loc[mask1]


# In[ ]:


titanic_male.head()


# In[ ]:


titanic.dtypes# == object


# In[ ]:


mask2 = titanic.dtypes == object
mask2


# In[ ]:


titanic.loc[:, ~mask2]


# In[ ]:


titanic.loc[mask1, ~mask2]


# In[ ]:





# ## Filtering DataFrames with many Conditions (AND)

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head(10)


# In[ ]:


mask1 = titanic.sex == "male"
mask1.head()


# In[ ]:


mask2 = titanic.age > 14
mask2.head()


# In[ ]:


(mask1 & mask2).head()


# In[ ]:


male_adult = titanic.loc[mask1 % mask2, ["survived", "pclass", "sex", "age"]]
male_adult.head(20)


# In[ ]:


male_adult.info()


# In[ ]:


male_adult.describe()


# In[ ]:


titanic.describe()


# In[ ]:





# ## Filtering DataFrames with many Conditions (OR)

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


mask1 = titanic.sex == "female"
mask1.head(20)


# In[ ]:


mask2 = titanic.age < 14
mask2.head(20)


# In[ ]:


(mask1 | mask2).head(11)


# In[ ]:


titanic.loc[mask1 | mask2]


# In[ ]:


wom_or_chi = titanic.loc[mask1 | mask2, ["survived", "pclass", "sex", "age"]]


# In[ ]:


wom_or_chi.head()


# In[ ]:


wom_or_chi.info()


# In[ ]:


wom_or_chi.describe()


# In[ ]:


titanic.describe()


# In[ ]:





# ## Advanced Filtering with between(), isin() and ~

# In[ ]:


import pandas as pd


# In[ ]:


summer = pd.read_csv("summer.csv")


# In[ ]:


summer.head()


# In[ ]:


og_1988 = summer.loc[summer.Year == 1988]


# In[ ]:


og_1988.head()


# In[ ]:


og_1988.tail()


# In[ ]:


og_1988.info()


# In[ ]:


og_since1992 = summer.loc[summer.Year >= 1992]


# In[ ]:


og_since1992.head()


# In[ ]:


og_since1992.tail()


# In[ ]:


summer.Year.between(1960, 1969).head()


# In[ ]:


og_60s = summer.loc[summer.Year.between(1960, 1969, inclusive=True)]


# In[ ]:


og_60s.head()


# In[ ]:


og_60s.tail()


# In[ ]:


my_favourite_games = [1972, 1996]


# In[ ]:


summer.Year.isin(my_favourite_games).head()


# In[ ]:


og_72_96 = summer.loc[summer.Year.isin(my_favourite_games)]


# In[ ]:


og_72_96.head()


# In[ ]:


og_72_96.tail()


# In[ ]:


og_not_72_96 = summer.loc[~summer.Year.isin(my_favourite_games)]


# In[ ]:


og_not_72_96.head()


# In[ ]:


og_not_72_96.Year.unique()


# In[ ]:





# ## any() and all()

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.sex == "male"


# In[ ]:


(titanic.sex == "male").any()


# In[ ]:


(titanic.sex == "male").all()


# In[ ]:


(titanic.age == 80.0).any()


# In[ ]:


pd.Series([-1, 0.5 , 1, -0.1, 0]).any()


# In[ ]:


titanic.fare.all()


# In[ ]:




