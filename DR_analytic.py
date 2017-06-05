"""
Vikulp Sharma
DR Analytics
"""
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from datetime import datetime, date
import seaborn as sns
from collections import Counter
from pandas import Series
from pylab import figure, axes, pie, title, show


# reading salesforce DR report, SV Visit for GEnx product line
drGenx=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/report1493227587647.csv")
shopVisit=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/genxenginestatusasofapril25.csv")
#Changing the column names and date types
drGenx.rename(columns={'Date/Time Opened': 'openDate','Case Owner':'caseOwner','ATA Number':'ATANumber','Date/Time Closed':'closeDate','Engine Model':'endineModel','Case Origin':'caseOrigin','Case Record Type':'caseRecord','ATA Subtask':'ATASubtask','Age (Hours)':'Age','Account Name':'accountName','Life Limited Part':'LLP'}, inplace=True)
drGenx['openDate'] = pd.to_datetime(drGenx['openDate'])
drGenxSort=drGenx.sort(['openDate'])

########################################################
##########    FAN MODULE   ############################
########################################################
### Fan Module 2016 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Pankaj Agrawal','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016.png',bbox_inches = 'tight')   ### Update

### Fan Module 2017 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Thomas Wimmer']
drGenxFan=drGenxSort1617[drGenxSort1617.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2017.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Pankaj Agrawal','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016firstQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Pankaj Agrawal','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016SecondQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 Third Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Pankaj Agrawal','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Third Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016thirdQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 Last Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Pankaj Agrawal','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016finalQ.png',bbox_inches = 'tight')   ### Update
           
### Fan Module 2017 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2017 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2017firstQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2017 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski','Thomas Wimmer']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2017 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2017secondQ.png',bbox_inches = 'tight')   ### Update

########################################################
##########    COMPRESSOR MODULE   ############################
########################################################
### Compressor Module 2016 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2016.png',bbox_inches = 'tight')   ### Update

### Compressor Module 2017 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort1617[drGenxSort1617.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2017.png',bbox_inches = 'tight')   ### Update

### Compressor Module 2016 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2016 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2016firstQ.png',bbox_inches = 'tight')   ### Update

### Compressor Module 2016 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2016 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2016SecondQ.png',bbox_inches = 'tight')   ### Update

### Compressor Module 2016 Third Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2016 Third Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2016thirdQ.png',bbox_inches = 'tight')   ### Update

### Compressor Module 2016 Last Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2016finalQ.png',bbox_inches = 'tight')   ### Update
           
### Compressor Module 2017 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2017 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2017firstQ.png',bbox_inches = 'tight')   ### Update

### Compressor Module 2017 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['Patrick Bell', 'MICHAL LALIK', 'Yashpal Patel']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Compressor Module 2017 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/compressorModule2017secondQ.png',bbox_inches = 'tight')   ### Update

########################################################
##########   Hot Section  ############################
########################################################
### GEnx Hot Section 2016 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2016.png',bbox_inches = 'tight')   ### Update

### GEnx Hot Section 2017 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort1617[drGenxSort1617.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2017.png',bbox_inches = 'tight')   ### Update

### GEnx Hot Section 2016 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2016 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2016firstQ.png',bbox_inches = 'tight')   ### Update

### GEnx Hot Section 2016 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2016 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2016SecondQ.png',bbox_inches = 'tight')   ### Update

### GEnx Hot Section 2016 Third Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2016 Third Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2016thirdQ.png',bbox_inches = 'tight')   ### Update

### GEnx Hot Section 2016 Last Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2016finalQ.png',bbox_inches = 'tight')   ### Update
           
### GEnx Hot Section 2017 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Hot Section 2017 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2017firstQ.png',bbox_inches = 'tight')   ### Update

### GEnx Hot Section 2017 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['Girish Goda','Greg Minges','James Caldwell','David Clausing']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='FGEnx Hot Section 2017 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/hotSection2017secondQ.png',bbox_inches = 'tight')   ### Update

########################################################
##########   Oil System, Frame and LPT  ############################
########################################################
### GEnx Oil System, Frame and LPT 2016 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2016.png',bbox_inches = 'tight')   ### Update

### GEnx Oil System, Frame and LPT 2017 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort1617[drGenxSort1617.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2017.png',bbox_inches = 'tight')   ### Update

### GEnx Oil System, Frame and LPT 2016 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2016 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2016firstQ.png',bbox_inches = 'tight')   ### Update

### GEnx Oil System, Frame and LPT 2016 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2016 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2016SecondQ.png',bbox_inches = 'tight')   ### Update

### GEnx Oil System, Frame and LPT 2016 Third Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2016 Third Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2016thirdQ.png',bbox_inches = 'tight')   ### Update

### GEnx Oil System, Frame and LPT 2016 Last Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2016finalQ.png',bbox_inches = 'tight')   ### Update
           
### GEnx Oil System, Frame and LPT 2017 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2017 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2017firstQ.png',bbox_inches = 'tight')   ### Update

### GEnx Oil System, Frame and LPT 2017 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['Alan Moulvi','Lukasz Brzezinski','Radoslaw Mrozek','Timothy Sambor']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Oil System, Frame and LPT 2017 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/oilEtc2017secondQ.png',bbox_inches = 'tight')   ### Update

########################################################
##########   Systems  ############################
########################################################
### GEnx Systems 2016 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2016.png',bbox_inches = 'tight')   ### Update

### GEnx Systems 2017 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort1617[drGenxSort1617.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2017.png',bbox_inches = 'tight')   ### Update

### GEnx Systems 2016 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2016 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2016firstQ.png',bbox_inches = 'tight')   ### Update

### GEnx Systems 2016 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2016 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2016SecondQ.png',bbox_inches = 'tight')   ### Update

### GEnx Systems 2016 Third Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2016 Third Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2016thirdQ.png',bbox_inches = 'tight')   ### Update

### GEnx Systems 2016 Last Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2016finalQ.png',bbox_inches = 'tight')   ### Update
           
### GEnx Systems 2017 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2017 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2017firstQ.png',bbox_inches = 'tight')   ### Update

### GEnx Systems 2017 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['Francisco Zamora','Homero Ramos','Joseph Allen','Kamal Sarda','Ron Luffy','Steve Molter','Todd Hanna','Yair Enrique Cruz']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='GEnx Systems 2017 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2017secondQ.png',bbox_inches = 'tight')   ### Update

           


#subprocess.call(["python", "C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fan.py"])
#           
#drGenx = drGenx[pd.notnull(drGenx['ATANumber'])]
##gg=drGenx[drGenx['ATANumber'].str.contains("70-" OR "72-" OR "73-")]
#gg=drGenx[drGenx['ATANumber'].str.contains("70-")]
#print(gg)

           
