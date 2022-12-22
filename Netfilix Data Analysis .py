#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


dataset = pd.read_csv(r"F:\python real work project 19-12-2022\8. Netflix Dataset.csv")


# In[3]:


dataset


# **`some basic information about the dataset`**

# In[4]:


dataset.head()


# In[5]:


dataset.tail()


# In[6]:


dataset.shape


# In[7]:


dataset.size                                       # it is used to find count total element in dataset


# In[8]:


dataset.columns


# In[9]:


dataset.info()


# In[10]:


dataset.dtypes


# # TASK 1 

# > **Is There any duplicate record in this dataset ? If yes, Then remove the duplicate record.**

# In[11]:


dataset.head()


# In[12]:


dataset.duplicated()


# In[13]:


dataset[dataset.duplicated()]


# In[14]:


dataset.drop_duplicates(inplace=True)


# In[15]:


dataset[dataset.duplicated()]


# > `checking shape of dataset after droping duplicate record`

# In[16]:


dataset.shape


# # TASK 2

# > **`Is there any NUll value present in any column ? Show with Heat-Map`**

# In[17]:


dataset.head()


# In[18]:


dataset.shape


# In[19]:


dataset.isnull().sum()


# In[20]:


plt.figure(figsize = (15,10))
sns.heatmap(dataset.isnull())


# > `Check the how much percent null value present in dataset`

# In[21]:


dataset.isnull().sum()/dataset.shape[0]*100


# # Q.1) For 'House of Cards', what is the show id and who is the director of this show

# In[22]:


dataset.columns


# > methode 1 - using, **isin()**

# In[23]:


dataset[ dataset['Title'].isin(['House of Cards']) ]


# > methode 2 - using, **str.contains()**

# In[24]:


dataset[dataset['Title'].str.contains('House of Cards')]


# # Q.2) In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph 

# In[25]:


dataset.head()


# In[26]:


dataset.dtypes


# > **-to work on `Release_Date` column to change there data type `object` to `datetime` datatype** <br>
# **-add new column on dataset**

# > Function - **pd.to_datetime()**

# In[27]:


dataset['date_new'] = pd.to_datetime(dataset['Release_Date'])


# In[28]:


dataset.head()


# In[29]:


dataset.dtypes


# In[30]:


dataset['date_new'].dt.year


# In[31]:


dataset['date_new'].dt.year.value_counts()


# In[32]:


dataset['date_new'].dt.year.value_counts().plot(kind = 'bar', color ='black' )


# # Q.3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph

# In[33]:


dataset.head()


# In[34]:


dataset.groupby('Category').Category.count()


# > `methode = 1`

# In[35]:


dataset.groupby('Category').Category.count().plot(kind='bar', color = 'r')


# > `methode = 2`

# In[36]:


sns.countplot(dataset['Category'])


# # Q.4) Show all the Movies that were reliesed in year 2000.

# In[37]:


dataset.head()


# In[38]:


dataset['year'] = dataset['date_new'].dt.year


# In[39]:


dataset.head(2)


# In[40]:


dataset[ (dataset['Category']== 'Movie') & (dataset['year'] == 2000) ]


# > `their is no any movie released on year 2000`

# **find the Movies released on year 2020**

# In[41]:


dataset[ (dataset['Category']== 'Movie') & (dataset['year'] == 2020) ]


# # Q.5) Show only the Titles of all TV Shows that were released in india only

# In[42]:


dataset.head(2)


# In[43]:


dataset[ (dataset['Category'] == 'TV Show') & (dataset['Country'] == 'India') ] ['Title']


# # Q.6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[44]:


dataset.head(2)


# In[45]:


dataset['Director'].value_counts().head(10)


# # Q.7) Show all the Recordes, where 'Category is movie and type is Comedies' or 'Country is United Kingdom'.

# In[46]:


dataset.head(2)


# In[47]:


dataset[ (dataset['Category'] == 'Movie') & (dataset['Type'] == 'Comedies') | (dataset['Country'] == 'United Kingdom') ]


# # Q.8) In how many movies/show. Tom Cruise was cast ?

# In[48]:


dataset.head(2)


# In[49]:


dataset[ dataset['Cast'].str.contains('Tom Cruise' ) ]


# > **Note - `Here is no datarecords show for 'Tom Cruise', because str.contains() not contain NA/NaN values because of that we need to remove the null records from dataset`**

# > check after remove all null values from dataset 

# In[50]:


new_df = dataset.dropna()


# In[51]:


new_df.head(2)


# In[52]:


new_df[new_df['Cast'].str.contains('Tom Cruise')]


# # Q.9) What are the different Rating defined by netflix ?

# In[53]:


dataset['Rating'].nunique()


# In[54]:


dataset['Rating'].unique()


# # How many Movies got the 'TV-14' rating in Canada

# In[55]:


dataset[ (dataset['Category'] == 'Movie') & (dataset['Rating'] == 'TV-14') & (dataset['Country']== 'Canada') ]


# In[56]:


dataset[ (dataset['Category'] == 'Movie') & (dataset['Rating'] == 'TV-14') & (dataset['Country']== 'Canada') ].shape


# # How many TV Shows got the 'R' rating, after year 2018 ?

# In[57]:


dataset[ (dataset['Category'] == 'TV Show') & (dataset['Rating'] == 'R') & (dataset['year'] > 2018)]


# In[58]:


dataset[ (dataset['Category'] == 'TV Show') & (dataset['Rating'] == 'R') & (dataset['year'] > 2018)].shape


# # Q.10) What is the maximum duration of a Movie/show on Netflix ?

# In[59]:


dataset.head(2)


# In[60]:


dataset['Duration'].dtypes


# In[61]:


dataset.Duration.unique()


# In[62]:


dataset[['Minute', 'unit']] = dataset['Duration'].str.split(' ', expand=True)


# In[63]:


dataset.head()


# In[64]:


dataset['Minute'].max()


# # Q.11) Which individual country has the highest No. of TV Shows ?

# In[65]:


dataset.head(2)


# In[66]:


data_tvshow = dataset[dataset['Category']== 'TV Show']


# In[67]:


data_tvshow.head()


# In[68]:


data_tvshow['Country'].value_counts().head()


# In[69]:


data_tvshow['Country'].value_counts().head(1)


# # Q.12) How can we sort the Dataset by Year ?

# In[70]:


dataset.sort_values('year').head()    # here sort ascending


# In[71]:


dataset.sort_values(by = 'year', ascending = False) 


# # Q.13) Category is 'Movie' and type is 'Dramas' or category is 'TV Show' and type is "kids'TV" 

# In[72]:


dataset[ (dataset['Category'] == 'Movie') & (dataset['Type']== 'Dramas') 
        | (dataset['Category'] == 'TV Show') & (dataset['Type']== "Kids'TV")]


# In[ ]:





# In[ ]:




