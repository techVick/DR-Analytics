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

shopvis=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/MASTER_GEnxMROWIP.csv")
shopvis['Induct'] = pd.to_datetime(shopvis['Induct'])
drGenxSort1617=shopvis.loc[shopvis['Induct'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['Induct'] <= '2016-10-31 00:00:00']## Update
kk=drGenxSort16.groupby('Site').count()
print(kk)