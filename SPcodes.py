
# coding: utf-8

# In[4]:

import csv
import pandas as pd
import string
al=string.ascii_uppercase

# In[5]:

df=pd.read_csv("2018.csv")


# In[12]:

import re


# In[260]:

sec=input("what is sector number (Enter 2 numbers)? : Like 10,15,20,25,.....  ")
sector_code=[]
n=0
for i in range(len(df)):
    sector=re.compile(r'^'+sec+'\d{2}')
    sector_re=sector.search(str(df.iloc[i][2]).strip())
    if sector_re != None:
      
        sector_code.append(al[n])
        print(al[n])
        print(sector_re.group())
        n=n+1       
#print(item for item in sector_code)


# In[258]:

industry_group_code=[]
industry_group_ticker=[]
aa=[]
ind_group=input("what is industry group number (Enter 4 numbers? : enter a number appeared front  ")
n=0
for i in range(len(df)):
    group=re.compile(r'^'+ind_group+'\d{2}')
    group_re=group.search(str(df.iloc[i][4]).strip())
    if group_re != None:
        industry_group_code.append(al[n])
        print(al[n])
        industry_group_ticker.append(al[n]+'I')
        aa.append(group_re.group())
        print(group_re.group())
        n=n+1       
#print(item for item in industry_group_code)
#print(item for item in industry_group_ticker)


# In[256]:

industry_code=[]
ind=input("which one do you want? : enter index(enter the one you want from previous enter index not the number)  ")
code=industry_group_code[int(ind)]
industry_ticker=[]
n=0
for i in range(len(df)):
    industry=re.compile(r'^'+aa[int(ind)]+'\d{2}')
    industry_re=industry.search(str(df.iloc[i][6]).strip())
    if industry_re != None:
      
        industry_code.append(al[n])
        
        industry_ticker.append(code+al[n])
        print(industry_re.group())
        print(code+al[n])
        n=n+1       
#print(item for item in industry_code)


# In[257]:

#print(item for item in industry_ticker)



