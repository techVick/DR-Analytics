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
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
#drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
#drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## 
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
#drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
#drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
#drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
#drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
#drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['GE CALEDONIAN LTD','GE GEES - CALEDONIAN', 'GE GEES - Celma', 'EVERGREEN AVIATION TECHNOLOGIES CORPORATION','Lufthansa Technik AG','GE GEES - Cincinnati','GE GEES - OWS','GE GEES - OWS LONDON','GE GEES - OWS Dallas','Lufthansa Technik AG','GE GEES - Hungary','GE GEES - OWS Hebron','GE GEES - Singapore','GE CAPITAL AVIATION SERVICES LLC']

drGenxFan=drGenxSort16[drGenxSort16.accountName.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['accountName','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

frames=[jj]
result = pd.concat(frames,axis=1)
result.columns=["SDR"]
result.plot(kind='bar',title='Shop SDR Volume 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Shop2016DR.png',bbox_inches = 'tight') 


drGenxSort16=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00']## Update
value_list = ['GE CALEDONIAN LTD','GE GEES - CALEDONIAN', 'GE GEES - Celma', 'EVERGREEN AVIATION TECHNOLOGIES CORPORATION','Lufthansa Technik AG','GE GEES - Cincinnati','GE GEES - OWS','GE GEES - OWS LONDON','GE GEES - OWS Dallas','Lufthansa Technik AG','GE GEES - Hungary','GE GEES - OWS Hebron','GE GEES - Singapore','GE CAPITAL AVIATION SERVICES LLC']

drGenxFan=drGenxSort16[drGenxSort16.accountName.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['accountName','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

frames=[jj]
result = pd.concat(frames,axis=1)
result.columns=["SDR"]
result.plot(kind='bar',title='Shop SDR Volume 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Shop2017DR.png',bbox_inches = 'tight') 

#GE CALEDONIAN LTD
#GE GEES - Celma
#Lufthansa Technik AG
#GE GEES - Cincinnati
#GE GEES - Hungary
#GE GEES - OWS Hebron
#EVERGREEN AVIATION TECHNOLOGIES CORPORATION
#GE GEES - CALEDONIAN
#GE GEES - Singapore
#GE CAPITAL AVIATION SERVICES LLC
#GE GEES - OWS
#GE GEES - OWS LONDON
#GE GEES - OWS Dallas
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
result.plot(kind='bar',title='GEnx Systems 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/Systems2017.png',bbox_inches = 'tight') 
#DR cycle time
interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
value_list = ['SDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
print(drGenxFan)
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))

interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
value_list = ['CDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
print(drGenxFan)
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
print(drGenxFan)
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))

interim=drGenxSort16.loc[drGenxSort16['Closed'] == 1]
interim=interim.loc[interim['LLP'] == 1]
print(interim)
value_list = ['CDR']
drGenxFan=interim[interim.caseRecord.isin(value_list)]
print(drGenxFan)
postGrind=drGenxFan['difference']
print(postGrind.max())
print(postGrind.min())
print(postGrind.mean())
print(postGrind.quantile(0.9))



