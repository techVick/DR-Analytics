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
plt.style.use('ggplot')

# reading salesforce DR report, SV Visit for GEnx product line
drGenx=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/report1493889006022_new1.csv")
#shopVisit=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/genxenginestatusasofapril25.csv")
#Changing the column names and date types
drGenx.rename(columns={'Date/Time Opened': 'openDate','Case Owner':'caseOwner','ATA Number':'ATANumber','Date/Time Closed':'closeDate','Engine Model':'endineModel','Case Origin':'caseOrigin','Case Record Type':'caseRecord','ATA Subtask':'ATASubtask','Age (Hours)':'Age','Account Name':'accountName','Life Limited Part':'LLP'}, inplace=True)
drGenx['openDate'] = pd.to_datetime(drGenx['openDate'])
#drGenxSort=drGenx.sort(['openDate'])
drGenxSort1617=drGenx.loc[drGenx['openDate'] >= '2017-01-01 00:00:00']
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-07-07 00:00:00']

value_list = ['GE CAL','GE CAL', 'GE CELMA', 'EGAT','Lufthansa Technik AG','GE ACSC','GE GEES - OWS','GE GEES - OWS LONDON','GE GEES - OWS Dallas','Lufthansa Technik AG','GE GEES - Hungary','GE GEES - OWS Hebron','GE GEES - Singapore']
value_list1=['RTCoE Airfoils','RTCoE CF6','RTCoE CFM/RES','RTCoE CRT','RTCoE GE90/GP','RTCoE GEMTC','RTCoE GEnx','RTCoE Structures']

#df.filter(col('bar').isin(['a','b']) == False).show()
drGenxFan=drGenxSort16[drGenxSort16.accountName.isin(value_list)]
fleet=drGenxFan[drGenxFan.Workgroup.isin(value_list1)==False]
repair=drGenxFan[drGenxFan.Workgroup.isin(value_list1)]

interim=fleet.loc[fleet['Closed'] == 1]
drGenxFanFinal=interim[['accountName','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

#frames=[jj]
#result = pd.concat(frames,axis=1)
#result.columns=["SDR"]
##plt.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
#result.plot(kind='bar',color='b', align='center',stacked=True);## Update

           
interim=repair.loc[repair['Closed'] == 1]
drGenxFanFinal=interim[['accountName','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
ll=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
mm=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()
           
frames=[jj,ll]
result1 = pd.concat(frames,axis=1)
result1.columns=["Fleet","Repair"]
result1.plot(kind='bar',title='2017 YTD Fleet and Repair SDR', align='center',stacked=True);## Update
plt.ylim((0,250))
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/FleetRepair2017.png',bbox_inches = 'tight') 

#drGenxSort=drGenx.sort(['openDate'])
drGenxSort1617=drGenx.loc[drGenx['openDate'] >= '2016-01-01 00:00:00']
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']

value_list = ['GE CAL','GE CAL', 'GE CELMA', 'EGAT','Lufthansa Technik AG','GE ACSC','GE GEES - OWS','GE GEES - OWS LONDON','GE GEES - OWS Dallas','Lufthansa Technik AG','GE GEES - Hungary','GE GEES - OWS Hebron','GE GEES - Singapore']
value_list1=['RTCoE Airfoils','RTCoE CF6','RTCoE CFM/RES','RTCoE CRT','RTCoE GE90/GP','RTCoE GEMTC','RTCoE GEnx','RTCoE Structures']

#df.filter(col('bar').isin(['a','b']) == False).show()
drGenxFan=drGenxSort16[drGenxSort16.accountName.isin(value_list)]
fleet=drGenxFan[drGenxFan.Workgroup.isin(value_list1)==False]
repair=drGenxFan[drGenxFan.Workgroup.isin(value_list1)]

interim=fleet.loc[fleet['Closed'] == 1]
drGenxFanFinal=interim[['accountName','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj1=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk1=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

frames=[jj1]
result2 = pd.concat(frames,axis=1)
result2.columns=["SDR"]
#plt.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
result2.plot(kind='bar',color='b', align='center',stacked=True);## Update

           
interim=repair.loc[repair['Closed'] == 1]
drGenxFanFinal=interim[['accountName','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
ll1=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
mm1=drGenxFanFinalPcr.groupby('accountName')['caseRecord'].count()

frames1=[jj1,ll1]
result3 = pd.concat(frames1,axis=1)
result3.columns=["Fleet","Repair"]
plt.ylim((0,250))
result3.plot(kind='bar',title='2016 Fleet and Repair SDR', align='center',stacked=True);## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/FleetRepair2016.png',bbox_inches = 'tight') 
    
frames=[jj1,ll1,jj,ll]
result4 = pd.concat(frames,axis=1)
result4.columns=["Fleet 2016","Repair 2016","Fleet YTD 2017","Repair YTD 2017"]
result4.plot(kind='bar',title='Fleet and Repair SDR', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/FleetRepairCombined.png',bbox_inches = 'tight') 
print(result1)
print(result3)

#result3=result3.sort(['Fleet'])

result3.rename(columns={'Fleet': 'Fleet 2016','Repair':'Repair 2016'}, inplace=True)
result1.rename(columns={'Fleet': 'Fleet YTD 2017','Repair':'Repair YTD 2017'}, inplace=True)
result=[result1,result3]
resultF=pd.concat(result,axis=1)
resultF=resultF.sort(['Fleet 2016'], ascending=False)
print(resultF)

fig, ax = plt.subplots()
resultF[['Fleet 2016', 'Repair 2016']].plot.bar(stacked=True, width=0.3, position=0.5, colormap="PiYG", ax=ax, alpha=0.7,align='center')
resultF[['Fleet YTD 2017', 'Repair YTD 2017']].plot.bar(stacked=True, width=0.3, position=-0.5, colormap="PiYG", ax=ax, alpha=0.7,align='center')
#df[['a', 'd']].plot.bar(stacked=True, width=0.1, position=0.5, colormap="BrBG", ax=ax, alpha=0.7)
plt.legend(loc="upper center")
plt.show()