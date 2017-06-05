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
drGenxSort16=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00']## Update

#DR cycle time
interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
value_list = ['SDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))

interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
value_list = ['CDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))

## For LLP
interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
interim=interim.loc[interim['LLP'] == 1]
value_list = ['SDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))

interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
interim=interim.loc[interim['LLP'] == 1]
value_list = ['CDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
print(drGenxFan)
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))



