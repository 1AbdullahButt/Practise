#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Attributes are characteristics of an object, while methods are functions that act on an object


# In[2]:


df = pd.read_csv('C:\\Users\\avata\\Desktop\\New folder\\EDA\\Case Study\\COVID clinical trials (1).csv')

df


# ###### 1. Read Dataset and Explore the dataset by checking shape, columns, see the first/last 'n' rows using head/tail. (n= 5,15,30) (6)  

# In[3]:


df.shape


# In[4]:


df.columns


# In[5]:


df.head(5)


# In[6]:


df.head(15)


# In[7]:


df.head(30)


# In[8]:


df.tail(5)


# In[9]:


df.tail(15)


# In[10]:


df.tail(30)


# ###### 2. Filter numeric columns and summarize their statistics and do the same for categorical columns(4)  

# In[11]:


df.info()


# In[12]:


df.describe()


# In[13]:


df.describe(include = 'object')


# ###### 3. Utilize str.strip() to remove leading and trailing spaces and str.replace() to correct specific character issues in the 'Conditions' column of the dataset.

# In[14]:


df.columns


# In[15]:


df['Conditions'].str.strip()


# In[16]:


df['Conditions'].str.replace('Covid19','Covid-19')


# ###### 4. Solve following question by using Groupby(10)
# ###### What is the average enrollment for each status?
# ###### How many studies are there for each phase of the trial?
# ###### What is the average enrollment for studies grouped by gender?
# ###### What is the earliest start date for each study type? 
# ###### What is the distribution of statuses in the dataset?
# 

# In[17]:


# What is the average enrollment for each status?
df.groupby(['Status'])['Enrollment'].mean()


# In[18]:


# How many studies are there for each phase of the trial?
df.groupby(['Study Results'])['Status'].value_counts()


# In[19]:


# What is the average enrollment for studies grouped by gender?
df.groupby(['Gender'])['Enrollment'].mean().astype(int) # To make it whole number changed to int


# In[20]:


# What is the earliest start date for each study type?
df['Start Date']= pd.to_datetime(df['Start Date'],format='mixed')


# In[21]:


df.groupby(['Study Type'])['Start Date'].min()


# In[22]:


# df[df['Study Type'] == 'Expanded Access']


# In[23]:


# What is the distribution of statuses in the dataset?
df['Status'].value_counts()


# ###### 5. Solve following question by using qcut(10)
# ###### Enrollment Quantile Categories: How are trials distributed across four quantiles based on enrollment numbers?
# ###### Start Date Year Quantiles: What are the time periods represented by four quantiles of trial start years?
# ###### Completion Time Frame Categories: How do trial durations distribute across four quantiles from start to completion date?
# ###### Outcome Measures Count Quantiles: How are trials categorized into four quantiles based on the number of outcome measures?
# ###### Trial Update Frequency Quantiles: What does the distribution of trial update frequencies look like across four quantiles?

# In[24]:


# Enrollment Quantile Categories: How are trials distributed across four quantiles based on enrollment numbers?



df['Enrollment1'] = pd.qcut(df['Enrollment'], q=4)
print(df[['Enrollment', 'Enrollment1']])


# In[40]:


df['Enrollment1'].value_counts().sort_index()


# In[65]:


# Start Date Year Quantiles: What are the time periods represented by four quantiles of trial start years?

df['Start Year'] = pd.qcut(df['Start Date'], q=4)
print(df[['Start Year', 'Start Date']])


# In[31]:


# Completion Time Frame Categories: How do trial durations distribute across four quantiles from start to completion date?
df['Completion Date']= pd.to_datetime(df['Completion Date'],format='mixed')


# In[36]:


df['Duration'] = ((df['Completion Date'] - df['Start Date'])/np.timedelta64(1, 'D'))
df['Duration']


# In[42]:


df['Duration1'] = pd.qcut(df['Duration'], q=4)
print(df[['Duration1', 'Duration']])


# In[88]:


# Outcome Measures Count Quantiles: How are trials categorized into four quantiles based on the number of outcome measures?
df['Outcome Measures'].value_counts()
Trails_Outcome = df['Outcome Measures'].str.count('|') + 1
df['Trails Outcome'] = pd.qcut(Trails_Outcome, q=4)
print(df[['Trails Outcome', 'Outcome Measures']])


# In[56]:


df['Trails Outcome'].value_counts().sort_index()


# In[57]:


# Trial Update Frequency Quantiles: What does the distribution of trial update frequencies look like across four quantiles?
df['Last Update Posted']= pd.to_datetime(df['Last Update Posted'],format='mixed')
df['Results First Posted']= pd.to_datetime(df['Results First Posted'],format='mixed')


# In[59]:


df['Update Frequency'] = pd.qcut(df['Last Update Posted'], q=4)
print(df[['Update Frequency', 'Last Update Posted']])


# ###### 6. Completion Time Frame Grouping: Apply the cut function to categorize the completion time frames of trials into distinct intervals. What are the characteristics of trials within each time frame group?

# In[72]:


bins = [0, 30, 60, 90, 120, float('inf')]

labels = ['0-30 days', '31-60 days', '61-90 days', '91-120 days', 'Over 120 days']

df['Completion Time Frame'] = pd.cut(df['Duration'], bins = bins, labels = labels)

print(df[['Completion Time Frame','Duration']])


# In[73]:


df['Completion Time Frame'].value_counts()


# ###### 7. Enrollment Distribution Analysis: Use Matplotlib's hist() function to create a histogram visualizing the distribution of the 'Enrollment' column in the dataset.

# In[74]:


df['Enrollment']


# In[80]:


plt.hist(df['Enrollment'])

# Adding labels and title
plt.xlabel('Enrollment')
plt.ylabel('Frequency')
plt.title('Enrollment Distribution')

# Displaying the plot
plt.show()


# In[82]:


df['Enrollment']


# In[83]:


plt.hist(df['Enrollment'])


# In[85]:


# Apply logarithmic transformation to enrollment data
log_enrollment = np.log1p(df['Enrollment'])

# Plot histogram with logarithmic transformation
plt.hist(log_enrollment, bins=20, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Log(Enrollment)')
plt.ylabel('Frequency')
plt.title('Logarithmic Enrollment Distribution')

# Displaying the plot
plt.show()

