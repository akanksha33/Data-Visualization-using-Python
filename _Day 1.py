
# coding: utf-8

# # DAY 1 Assignment : Line Graph
# 
# Question 1 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


x = np.arange(0,10)
y = x*x


# In[3]:


x


# In[4]:


y


# In[5]:


plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y)


# In[28]:


plt.title("2D-Diagram",size="18",color='Blue')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y,'bo-',color="Green",linewidth='1',markersize='10')


# Question2

# In[32]:


#line plot showing the sales trend in company 1 and 2:
days = [1,2,3,4,5,6,7]
sales_1 = [250,190,120,245,160,121,180]
sales_2 = [90,100,160,150,140,105,200]
plt.plot(days,sales_1,'b-',color='Blue',label='Sales of company 1')
plt.plot(days,sales_2,'r-',color='Green',label='sales of company 2')
plt.title("Sales Distribution b/w Company 1 and 2",color="RED",size="18")
plt.xlabel("Days of the week",)
plt.ylabel("Company Sales")
plt.legend()
plt.show()


# In[36]:


#question 3 

#subplots

x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]

plt.suptitle('CREATING SUB-PLOTS',fontsize=15)

plt.subplot(3,3,1)
plt.plot(x,y1,'r-')
plt.xlabel('X')
plt.ylabel('Y1')

plt.subplot(3,3,2)
plt.plot(x,y2,'r--')
plt.xlabel('X')
plt.ylabel('Y2')

plt.subplot(3,3,3)
plt.plot(x,y3,'g-')
plt.xlabel('X')
plt.ylabel('Y3')

plt.subplot(3,3,4)
plt.plot(x,y4,'go--')
plt.xlabel('X')
plt.ylabel('Y4')


