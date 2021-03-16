#!/usr/bin/env python
# coding: utf-8

# # Data Visualization with Seaborn

# ## First Steps

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=2, palette= "viridis")
sns.countplot(data = titanic, x = "sex", hue = "pclass")
plt.show()


# In[ ]:





# ## Categorical Plots

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.stripplot(data = titanic, x = "sex", y = "age", jitter = True, hue = "pclass", dodge = True)
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.swarmplot(data = titanic, x = "sex", y = "age", hue = "pclass", dodge = True)
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.violinplot(data = titanic, x = "sex", y = "age", hue = "pclass", dodge = True)
sns.swarmplot(data = titanic, x = "sex", y = "age", hue = "pclass", dodge = True, color = "black")
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.violinplot(data = titanic, x = "pclass", y = "age", hue = "sex", dodge = True, split = True )
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.barplot(data = titanic, x = "pclass", y = "age", hue = "sex", dodge = True)
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.pointplot(data = titanic, x = "pclass", y = "age", hue = "sex", dodge = True)
plt.show()


# In[ ]:





# ## Jointplots / Regression

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


sns.set(font_scale=1.5)
sns.jointplot(data = titanic, x = "age", y = "fare", height = 8, kind = "reg")
plt.show()


# In[ ]:


sns.set(font_scale=1.5)
sns.lmplot(data = titanic, x = "age", y = "fare", aspect= 1, height=8, col = "sex")
plt.show()


# In[ ]:


sns.set(font_scale=1.5)
sns.lmplot(data = titanic, x = "age", y = "survived", aspect= 1, height=8, col = "sex", logistic= True)
plt.show()


# In[ ]:


sns.set(font_scale=1.5)
sns.lmplot(data = titanic, x = "age", y = "survived", aspect= 1, height=8, col = "pclass", logistic= True)
plt.show()


# In[ ]:





# ## Matrixplots / Heatmaps

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


pd.crosstab(titanic.sex, titanic.pclass)


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(pd.crosstab(titanic.sex, titanic.pclass), annot= True, fmt = "d", cmap = "Reds", vmax = 150)
plt.show()


# In[ ]:


pd.crosstab(titanic.sex, titanic.pclass, values= titanic.survived, aggfunc= "mean")


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(pd.crosstab(titanic.sex, titanic.pclass, values= titanic.survived, aggfunc= "mean"), annot= True, cmap = "Reds")
plt.show()


# In[ ]:


titanic.corr()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(titanic.corr(), annot= True, cmap = "Reds")
plt.show()


# In[ ]:




