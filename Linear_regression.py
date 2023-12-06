#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[19]:


df=pd.read_csv('Salary_Data.csv')


# In[20]:


df.head()


# In[30]:


x=df.iloc[:,:-1]
y=df.iloc[:,1]


# In[31]:


x.shape


# In[32]:


y.shape


# In[33]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=100)


# In[34]:


from sklearn.linear_model import LinearRegression


# In[35]:


lr=LinearRegression()


# In[41]:


lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)


# In[37]:


from sklearn import metrics


# In[45]:


print("R_squared={:.2f}".format(lr.score(x,y)*100))
print("mean_absolute_error=",metrics.mean_absolute_error(y_test,y_pred))
print("Mean_Squared_error=",metrics.mean_squared_error(y_test,y_pred))
print("rmse=",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


# In[53]:


plt.scatter(x,y)
plt.plot(x_train,lr.predict(x_train),color='red',linewidth=0.5)
plt.title('Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')


# In[56]:


plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,color='red',linewidth=0.5)
plt.title('Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')


# In[ ]:




