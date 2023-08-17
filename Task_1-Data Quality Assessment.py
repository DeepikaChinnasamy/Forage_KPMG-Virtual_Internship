#!/usr/bin/env python
# coding: utf-8

# # KPMG VIRTUAL INTERNSHIP PROJECT
# 
# ## TASK: 1 - Data Quality Assessment
# 
# ### Assessment of data quality and completeness in preparation for analysis.
# 
# ##### The client provided KPMG with 3 datasets:
# 
# ###### 1.Customer Demographic
# 
# ###### 2.Customer Addresses
# 
# ###### 3.Transactions data in the past 3 months

# In[1]:


import pandas as pd


# ## Exploring Transactions

# In[3]:


df = pd.read_excel('C:/Users/USER/Desktop/PYTHON/Mainboot/Raw.xlsx',sheet_name=1) #Transactions sheet according to index

df


# In[4]:


df.shape


# In[5]:


df.head()


# In[8]:


df.columns


# In[11]:


df.dtypes


# In[13]:


df.describe()


# In[14]:


df.info()


# In[15]:


df.nunique()


# In[17]:


df.isnull().sum()


# In[18]:


df.duplicated().sum() #There is no duplicate


# In[24]:


# convert date column from float type into datetime
df['product_first_sold_date']=pd.to_datetime(df['product_first_sold_date'],unit='s')
df['product_first_sold_date']


# In[ ]:


# Values(product_first_sold_date) shown in sheet is not correct - its a date which is happend in same date with different timing


# In[34]:


df['product_first_sold_date'].head(20)


# In[25]:


df.info()


# In[ ]:


#Exploring columns (Object)


# In[28]:


df['order_status'].value_counts()


# In[29]:


df['brand'].value_counts()


# In[31]:


df['product_line'].value_counts()


# In[32]:


df['product_class'].value_counts()


# In[33]:


df['product_size'].value_counts()


# In[35]:


df.head()


# # Exploring NewCustomerList

# In[2]:


Newcust = pd.read_excel('C:/Users/USER/Desktop/PYTHON/Mainboot/Raw.xlsx',sheet_name=2) # NewCoustomerList sheet according to index

Newcust


# In[3]:


Newcust.head()


# In[4]:


Newcust.columns


# In[5]:


Newcust.describe()


# In[6]:


Newcust.dtypes


# In[7]:


Newcust.info()


# In[8]:


Newcust.isnull().sum()


# In[9]:


#Dropping unnamed columns
Newcust.drop(['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20'],axis=1,inplace=True)


# In[10]:


Newcust.info()


# In[51]:


Newcust.shape


# In[11]:


Newcust.duplicated().sum() #there is no duplicate


# In[12]:


Newcust.nunique()


# In[13]:


Newcust.info()


# In[15]:


#exploring Columns
Newcust.columns


# In[22]:


Newcust['gender'].value_counts()


# In[26]:


Newcust[Newcust.gender=='U'] #there are 17 unknown gender 


# In[28]:


Newcust['DOB'].value_counts()


# In[30]:


Newcust['job_title'].value_counts()


# In[31]:


Newcust['job_industry_category'].value_counts()


# In[32]:


Newcust['wealth_segment'].value_counts()


# In[33]:


Newcust['deceased_indicator'].value_counts()


# In[34]:


Newcust['owns_car'].value_counts()


# In[36]:


Newcust['state'].value_counts()


# In[37]:


Newcust['country'].value_counts()


# # Exploring CustomerDemographic

# In[39]:


CDemo = pd.read_excel('C:/Users/USER/Desktop/PYTHON/Mainboot/Raw.xlsx',sheet_name=3)

CDemo


# In[40]:


CDemo.head()


# In[41]:


CDemo.columns


# In[42]:


CDemo.info()


# In[43]:


CDemo.describe()


# In[44]:


CDemo.isnull().sum()


# In[47]:


CDemo.duplicated().sum()#There is no duplicate


# In[48]:


CDemo.nunique()


# In[ ]:


# Exploring columns


# In[51]:


CDemo.columns


# In[53]:


CDemo['gender'].value_counts() #Gender is not treated well so renameing gender categories


# In[55]:


CDemo['gender']=CDemo['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female')


# In[56]:


CDemo['gender'].value_counts()


# In[57]:


CDemo['DOB'].value_counts()


# In[58]:


CDemo['job_title'].value_counts()


# In[59]:


CDemo['job_industry_category'].value_counts()


# In[60]:


CDemo['wealth_segment'].value_counts()


# In[61]:


CDemo['deceased_indicator'].value_counts()


# In[62]:


CDemo['default'].value_counts() #values are inconsistent so drop default column


# In[63]:


CDemo=CDemo.drop('default', axis=1)


# In[64]:


CDemo.head()


# In[65]:


CDemo['owns_car'].value_counts()


# In[66]:


CDemo['tenure'].value_counts()


# # Exploring CustomerAddress

# In[67]:


CAdd = pd.read_excel('C:/Users/USER/Desktop/PYTHON/Mainboot/Raw.xlsx',sheet_name=4)

CAdd


# In[68]:


CAdd.head()


# In[70]:


CAdd.columns


# In[71]:


CAdd.info()


# In[72]:


CAdd.describe()


# In[74]:


CAdd.isnull().sum()


# In[75]:


CAdd.duplicated().sum() #There is no duplicate


# In[76]:


CAdd.nunique()


# In[77]:


#Exploring columns
CAdd['state'].value_counts()


# In[78]:


CAdd['country'].value_counts()


# In[79]:


#All columns are consistent in CustomerAddress


# In[ ]:




