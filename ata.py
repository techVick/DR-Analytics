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
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00']## Update

drGenxSort16["ATANumber"] = drGenxSort16["ATANumber"].str[:5]

value_list = ['72-00','72-02', '72-03', '72-09','72-21','72-23','72-24','72-25','72-26','72-30','72-31','72-32','72-40','72-41','72-42','72-43','72-50','72-51','72-52','72-53','72-54','72-55','72-56','72-57','72-58','72-59','72-60','72-61','72-62','72-63','72-64']

drGenxFan=drGenxSort16[drGenxSort16.ATANumber.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
workgrops=['CEO GEnx BEC PSE','CEO GENX Polska PSE','CEO GENX PSE','CEO GENX GEIQ PSE']
interim2=interim[interim.Workgroup.isin(workgrops)]
drGenxFanFinal=interim2[['ATANumber','caseRecord']]


drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ii=drGenxFanFinalPcr.groupby('ATANumber')['caseRecord'].count()

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('ATANumber')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('ATANumber')['caseRecord'].count()

frames=[ii,jj+kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","DR"]
result.plot(kind='bar',title='ATA Module Level DR and PCR Distribution 2017', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/ATA2017.png',bbox_inches = 'tight') 