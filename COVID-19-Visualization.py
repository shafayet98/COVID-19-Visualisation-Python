#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
from matplotlib.pyplot import figure


# In[127]:


df = pd.read_csv('2019_nCoV_data.csv') # read from csv
country_name = list(df.Country.unique())
df['Date'] = pd.to_datetime(df['Date']).dt.date # remove the time from date&time

# SPAIN
df_spain = df.loc[df['Country'] == 'Spain'] # took one country
df_spain= df_spain.groupby(['Date'], as_index=False, sort=True)['Deaths'].sum()
df_spain = df_spain.tail(10)
df_spain['Date'] = pd.DatetimeIndex(df_spain['Date']).day 
df_spain


# In[122]:


# Iran
df_iran = df.loc[df['Country'] == 'Iran'] # took one country
df_iran= df_iran.groupby(['Date'], as_index=False, sort=True)['Deaths'].sum()
df_iran = df_iran.tail(10)
df_iran['Date'] = pd.DatetimeIndex(df_iran['Date']).day 
df_iran


# In[99]:


# Germany
df_germany = df.loc[df['Country'] == 'Germany'] # took one country
df_germany= df_germany.groupby(['Date'], as_index=False, sort=True)['Deaths'].sum()
df_germany = df_germany.tail(10)
df_germany['Date'] = pd.DatetimeIndex(df_germany['Date']).day 
df_germany


# In[100]:


# US
df_us = df.loc[df['Country'] == 'US'] # took one country
df_us= df_us.groupby(['Date'], as_index=False, sort=True)['Deaths'].sum()
df_us = df_us.tail(10)
df_us['Date'] = pd.DatetimeIndex(df_us['Date']).day 
df_us


# In[142]:


# France
df_france = df.loc[df['Country'] == 'France'] # took one country
df_france= df_france.groupby(['Date'], as_index=False, sort=True)['Deaths'].sum()
df_france = df_france.tail(10)
df_france['Date'] = pd.DatetimeIndex(df_france['Date']).day 
df_france


# In[253]:


df_dict_date = {'deaths':df_us.iloc[:,0]}
df_data_date = pd.DataFrame(df_dict_date)
df_data_date 


# In[262]:


# PLOT
# plot(x,y)
figure(num=None, figsize=(8, 8))
plt.grid(False)
plt.style.use('dark_background')
plt.plot(df_data_date.iloc[:,0],df_spain.iloc[:,1], label='Spain',
        color='cyan', marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_iran.iloc[:,1],label='Iran',
        color="r", marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_germany.iloc[:,1], label='Germany',
        color='wheat',marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_us.iloc[:,1], label='USA',
        color='azure',marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_france.iloc[:,1], label='France',
        color='lightblue',marker='o',linewidth=0.7,markersize=1.5)

plt.xlabel("Date")
plt.ylabel("Deaths")
plt.title("COVID-19 (Death Case)")
plt.ylim(-500,1500)
plt.xlim(11,20)
plt.legend()
plt.savefig('covid-19-death-case.png', dpi=1000)
plt.show()


# In[230]:


df_new = pd.read_csv('2019_nCoV_data.csv') # read from csv
df_new['Date'] = pd.to_datetime(df_new['Date']).dt.date # remove the time from date&time

df_new
# SPAIN
df_spain_conf = df_new.loc[df['Country'] == 'Spain'] # took one country
df_spain_conf = df_spain_conf.groupby(['Date'], as_index=False, sort=True)['Confirmed'].sum()
df_spain_conf = df_spain_conf.tail(10)
df_spain_conf['Date'] = pd.DatetimeIndex(df_spain_conf['Date']).day 
df_spain_conf


# In[231]:


# Iran
df_iran_conf = df_new.loc[df['Country'] == 'Iran'] # took one country
df_iran_conf = df_iran_conf.groupby(['Date'], as_index=False, sort=True)['Confirmed'].sum()
df_iran_conf = df_iran_conf.tail(10)
df_iran_conf['Date'] = pd.DatetimeIndex(df_iran_conf['Date']).day 
df_iran_conf


# In[232]:


# Germany
df_ger_conf = df_new.loc[df['Country'] == 'Germany'] # took one country
df_ger_conf = df_ger_conf.groupby(['Date'], as_index=False, sort=True)['Confirmed'].sum()
df_ger_conf = df_ger_conf.tail(10)
df_ger_conf['Date'] = pd.DatetimeIndex(df_ger_conf['Date']).day 
df_ger_conf


# In[233]:


# France
df_france_conf = df_new.loc[df['Country'] == 'France'] # took one country
df_france_conf = df_france_conf.groupby(['Date'], as_index=False, sort=True)['Confirmed'].sum()
df_france_conf = df_france_conf.tail(10)
df_france_conf['Date'] = pd.DatetimeIndex(df_france_conf['Date']).day 
df_france_conf


# In[234]:


# us
df_us_conf = df_new.loc[df['Country'] == 'US'] # took one country
df_us_conf = df_us_conf.groupby(['Date'], as_index=False, sort=True)['Confirmed'].sum()
df_us_conf = df_us_conf.tail(10)
df_us_conf['Date'] = pd.DatetimeIndex(df_us_conf['Date']).day 
df_us_conf


# In[263]:


# PLOT Confirmed Case
# plot(x,y)
figure(num=None, figsize=(8, 8))
plt.grid(False)
plt.style.use('dark_background')
plt.plot(df_data_date.iloc[:,0],df_spain_conf.iloc[:,1], label='Spain',
        color='cyan', marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_iran_conf.iloc[:,1],label='Iran',
        color="r", marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_ger_conf.iloc[:,1], label='Germany',
        color='wheat',marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_us_conf.iloc[:,1], label='USA',
        color='azure',marker='o',linewidth=0.7,markersize=1.5)
plt.plot(df_data_date.iloc[:,0],df_france_conf.iloc[:,1], label='France',
        color='lightblue',marker='o',linewidth=0.7,markersize=1.5)

plt.xlabel("Date")
plt.ylabel("Confirmed Case")
plt.title("COVID-19 (Confirmed Case)")
plt.ylim(1000,21000)
plt.xlim(11,20)
plt.legend()
plt.savefig('covid-19-confirmed-case.png', dpi=1000)
plt.show()

