#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[6]:


series_obj=Series(np.arange(8),index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8'])
series_obj


# In[7]:


#retrieve all records with that lable-index
series_obj['row 7']


# In[8]:


#retrieve all records with the specified integer index
series_obj[[0,7]]


# In[11]:


import numpy as np
np.random.seed(25)
DF_obj =pd.DataFrame(np.random.rand(64).reshape((8,8)),index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8'],
columns=['column 1','column 2','column 3','column 4','column 5','column 6','column 7','column 8'])
print(DF_obj)


# In[120]:


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
print(brics)


# In[121]:


# Set the index for brics
d=brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(d)


# In[70]:


data = pd.read_table('http://bit.ly/chiporders')
print(data)


# In[15]:


#There are several ways to index a Pandas DataFrame. 
#One of the easiest ways to do this is by using square bracket notation.

data=pd.read_table('http://bit.ly/chiporders')
# Print out order_id column as Pandas Series
print(data['order_id'])


# In[13]:


# Print out oreder_id column as Pandas DataFrame
print(data[['order_id']])


# In[14]:


# Print out DataFrame with order_id and quantity columns
print(data[['order_id', 'quantity']])


# In[16]:


# Print out first 4 observations
print(data[0:4])


# In[18]:


# start from 4th it will to end
print(data[4:])


# In[19]:


# start from beginning till 4
print(data[:4])


# In[71]:


print(data[::])
#or print(data)


# In[64]:


#print(data[2,4])
#error

pd.data['item_name']


# In[26]:


#iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
print(data.iloc[2])


# In[27]:


print(data.iloc[2,2])


# In[56]:


data.iloc[2:,2:]


# In[46]:


#loc gets rows (or columns) with particular labels from the index.
print(data.loc[[0]])
print("\n\n")
#same
print(data.iloc[[0]])

#difference in [] or [[]]

print("\n\n")
print(data.iloc[0])
#same
print("\n\n")
print(data.iloc[0])


# In[54]:


data.loc[[0,3]]


# In[50]:


# slice the first three rows
data.iloc[:3]

#data.iloc[[:3]]
#invalid syntax


# In[52]:


#slicing the first three rows including 3
#3 is not index
data.loc[:3]

#data.loc[[:3]]
#invalid syntax


# In[96]:


print(brics)


# In[122]:


brics.loc[["IN"]]


# In[126]:


#brics.iloc["IN"]
#it will take only integer

brics.ix[:"IN"]
# behaves like loc given non-integer


# In[144]:


brics.index=["1","4","2","0","5"]
print(brics)


# In[112]:


brics.iloc[:4]


# In[170]:


#brics.loc[:4]
#at index 4 != 0
#brics.loc[:5]
#error


# In[153]:


brics.ix[:4]
# now behaves like iloc given integer


# In[154]:


brics.ix[:4,"capital"]
#combine of loc and iloc


# In[157]:


#brics.iloc[:4,"capital"]
#error
#brics.loc[:4,"capital"]
#error


# In[164]:


#brics.loc[[5]]
#error - None of [[5]] are in the [index]
#brics.iloc[[5]]
#error positional indexers are out-of-bounds
#brics.ix[[5]]
#error indices are out-of-bounds


# In[166]:


brics.loc[[4]]


# In[167]:


brics.iloc[[4]]


# In[168]:


brics.ix[[4]]


# In[176]:


brics.index=["a","b","c","1","2"]
print(brics)


# In[179]:


brics.loc[:"b"]


# In[183]:


#brics.loc[:1]
brics.iloc[:1]
#error


# In[184]:


brics.loc[:"1"]


# In[187]:


brics.loc[["a","b"],"capital"]


# In[193]:


brics.iloc[[-2]]
#brics.loc[[-2]]
#error


# In[204]:


brics.iloc[:-2]
#brics.loc[:-2]
#error


# In[216]:


brics.head()


# In[217]:


brics["country"].head()


# In[218]:


brics[["area","population"]].head(3)


# In[225]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[227]:


plt.hist(brics.area)


# In[228]:


plt.hist(brics.population)


# In[229]:


brics


# In[230]:


brics.shape


# In[231]:


brics.columns


# In[233]:


brics.info()


# In[11]:


df=brics["area"]


# In[10]:


import pandas as pd
import numpy as np
df.apply(np.sqrt)


# In[ ]:


df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])


# In[ ]:


df


# In[ ]:


df.apply(np.sum, axis=0)


# In[ ]:


df.apply(np.sum, axis=1)
#every single row to a function


# In[ ]:


df.replace(4,5)


# In[ ]:


df.replace(4,"data")


# In[251]:


k.info()


# In[ ]:




