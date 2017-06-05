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
import csv

# reading salesforce DR report, SV Visit for GEnx product line
drGenx=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/report1495440707006.csv")
atalist=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/ata_list.csv")

#Changing the column names and date types
drGenx.rename(columns={'Part No.':'partNo','Date/Time Opened': 'openDate','Case Owner':'caseOwner','ATA Number':'ATANumber','Date/Time Closed':'closeDate','Engine Model':'endineModel','Case Origin':'caseOrigin','Case Record Type':'caseRecord','ATA Subtask':'ATASubtask','Age (Hours)':'Age','Account Name':'accountName','Life Limited Part':'LLP','Part Name':'PartName'}, inplace=True)
drGenx['openDate'] = pd.to_datetime(drGenx['openDate'])
#drGenxSort=drGenx.sort(['openDate'])
##################################################################################
##################################################################################
drGenxSort1617=drGenx.loc[drGenx['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-07-01 00:00:00']## Update
value_list = ['SDR', 'CDR']
drGenxFan=drGenxSort16[drGenxSort16.caseRecord.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
interim["partNo"] = interim["partNo"].str[:7]
interim["ATANumber"] = interim["ATANumber"].str[:5]

interim1=interim[['partNo']]
#interim1.sort('partNo').groupby('partNo').reset_index()
#interim1['partNo'].value_counts()
#Counter(interim1).values()
#
#
#ii=interim1.groupby(['partNo'], sort=False).count()
ii=interim.groupby('partNo')['caseOwner'].count().reset_index()
#ii=ii.nlargest(40)
ii=ii.sort(['caseOwner'], ascending=False)
ii=ii['partNo']
ii=ii.head(40)
interim2=interim
out_csv = 'C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/text8.csv'
with open('large5.csv','a') as f1:
    writer=csv.writer(f1, delimiter='\t',)
    csv_new = csv.writer(open('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/text1.csv', 'w'))
    for i in ii:
        interim=interim.loc[interim['partNo'] == i] ## Update
        ii=interim.groupby('ATASubtask')['caseOwner'].count().reset_index()
        jj=interim.groupby('ATASubtask')['Title'].agg(lambda x:x.value_counts().index[0]).reset_index()
        kk=interim.groupby('ATASubtask')['endineModel'].agg(lambda x:x.value_counts().index[0]).reset_index()
        ll=interim.groupby('ATASubtask')['caseOwner'].agg(lambda x:x.value_counts().index[0]).reset_index()
        mm=interim.groupby('ATASubtask')['partNo'].agg(lambda x:x.value_counts().index[0]).reset_index()
        nn=interim.groupby('ATASubtask')['PartName'].agg(lambda x:x.value_counts().index[0]).reset_index()
        frames=[ii,jj,kk,ll,mm,nn]
        print(frames)
        result = pd.concat(frames,axis=1)
        result.columns=["ATASubtask","caseOwner","ATASubtask","Title","ATASubtask","endineModel","ATASubtask","caseOwner","ATASubtask","partNo","ATASubtask","PartName"]
        writer.writerow([ii,jj,kk,ll,mm,nn])
        csv_new.writerow(i)
#       i.to_csv(out_csv,index=False,header=False,mode='a')#size of data to append for each loop
        result.to_csv(out_csv,index=False,header=False,mode='a')#size of data to append for each loop
        interim=interim2



    

    
#ii.plot(kind='bar',title='Part Number DR(CDR+SDR) Grouping', align='center');## Update
#plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/2017partGroup.png',bbox_inches = 'tight')   ### Update
