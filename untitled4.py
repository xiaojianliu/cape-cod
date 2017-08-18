# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 00:50:48 2017

@author: xiaojian
"""
import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import csv
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from math import sqrt
from netCDF4 import Dataset
"""
tt2012=np.load('tt2012.npy')
h2012=np.load('h2012.npy')
fig,axes=plt.subplots(3,1,figsize=(10,15))#,sharex=True)

axes[0].set_title('2012')
axes[0].bar(tt2012,h2012,width=0.5,label='retention')
#df=pd.DataFrame(np.array(h).T,index=list(tt))#,columns=pd.Index(['2004','2005','2006','2007','2008','2009','2010']))#,name='Genus'))
#df.plot(kind='bar',ax=axes[0])
ax01=axes[0].twinx()
dian=['A','B','C','D','E','F','G','H','I','J']
time2012=np.load('time2012.npy')
temp2012=np.load('temp2012.npy')
for a in np.arange(len(temp2012)):
    print 'b',a
    ax01.plot(time2012,temp2012[a],label='%s'%(dian[a]))
ax01.plot([time2012[0],time2012[-1]],[10,10],color='black')
ax01.legend()
ax01.set_ylim([0,14])

##################################################
tt2013=np.load('tt2013.npy')
h2013=np.load('h2013.npy')

axes[1].set_title('2013')
axes[1].bar(tt2013,h2013,width=0.5,label='retention')
#df=pd.DataFrame(np.array(h).T,index=list(tt))#,columns=pd.Index(['2004','2005','2006','2007','2008','2009','2010']))#,name='Genus'))
#df.plot(kind='bar',ax=axes[0])
ax02=axes[1].twinx()
dian=['A','B','C','D','E','F','G','H','I','J']
time2013=np.load('time2013.npy')
temp2013=np.load('temp2013.npy')
for a in np.arange(len(temp2013)):
    print 'b',a
    ax02.plot(time2013,temp2013[a],label='%s'%(dian[a]))
ax02.legend()
ax02.set_ylim([0,14])
ax02.plot([time2013[0],time2013[-1]],[10,10],color='black')

############################################################
tt2014=np.load('tt2014.npy')
h2014=np.load('h2014.npy')

axes[2].set_title('2014')
axes[2].bar(tt2014,h2014,width=0.5,label='retention')
#df=pd.DataFrame(np.array(h).T,index=list(tt))#,columns=pd.Index(['2004','2005','2006','2007','2008','2009','2010']))#,name='Genus'))
#df.plot(kind='bar',ax=axes[0])
ax03=axes[2].twinx()
ax03.set_ylim([0,14])
axes[0].set_ylim([0,200])
axes[1].set_ylim([0,200])
axes[2].set_ylim([0,200])
axes[0].set_ylabel('number')
axes[1].set_ylabel('number')
axes[2].set_ylabel('number')

ax01.set_ylabel('temperature')
ax02.set_ylabel('temperature')
ax03.set_ylabel('temperature')
#ax03.plot([time2014[0],time2014[-1]],[10,10],color='black')

dian=['A','B','C','D','E','F','G','H','I','J']
time2014=np.load('time2014.npy')
temp2014=np.load('temp2014.npy')
for a in np.arange(len(temp2014)):
    print 'b',a
    ax03.plot(time2014,temp2014[a],label='%s'%(dian[a]))
ax03.legend()
plt.savefig('zx',dpi=300)
"""
tt2014=np.load('tt2014.npy')
h2014=np.load('h2014.npy')

fig,axes=plt.subplots(1,1,figsize=(10,5))
axes.set_title('The number of turtles reaching cape cod bay every day')
axes.bar(tt2014,h2014,width=0.5,label='retention')
axes.set_ylabel('number')
plt.savefig('2014turtle',dpi=300)
