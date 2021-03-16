#!/usr/bin/env python
# coding: utf-8

# # Data Visualization with Matplotlib

# ## The plot() method

# In[ ]:


import pandas as pd


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.info()


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


titanic.plot(subplots= True, figsize=(15, 12), sharex= False, sharey=False)
plt.show()


# In[ ]:


titanic.age.plot(figsize=(12, 8))
plt.show()


# In[ ]:





# ## Customization

# In[ ]:


xticks = [x for x in range(0,901, 50)]
xticks


# In[ ]:


yticks = [y for y in range(0, 81, 5)]
yticks


# In[ ]:


plt.style.available


# In[ ]:


plt.style.use("classic")


# In[ ]:


titanic.age.plot(figsize = (12,8), fontsize= 13, c = "r", linestyle = "-",
                 xlim = (0,900), ylim = (0,80), xticks = xticks, yticks = yticks, rot = 45) 
plt.title("Titanic - Ages", fontsize = 15)
plt.legend(loc = 3, fontsize = 15)
plt.xlabel("Passenger No", fontsize = 13)
plt.ylabel("Age", fontsize = 13)
#plt.grid()
plt.show()


# In[ ]:





# ## Histograms

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.age.value_counts()


# In[ ]:


titanic.age.plot(kind = "hist", figsize = (12,8), fontsize = 15, bins = 80, density = True)
plt.show()


# In[ ]:


titanic.age.hist(figsize = (12,8), bins = 80, xlabelsize=15, ylabelsize= 15, cumulative = True)
plt.show()


# In[ ]:


plt.figure(figsize = (12,8))
plt.hist(titanic.age.dropna(), bins = 80, density = True, cumulative= True)
plt.show()


# In[ ]:





# ## Scatterplots

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


titanic = pd.read_csv("titanic.csv")


# In[ ]:


titanic.head()


# In[ ]:


titanic.plot(kind = "scatter", figsize = (15,8), x = "age", y = "fare", c = "pclass", marker = "x", s = 20, colormap= "viridis" ) 
plt.show()

