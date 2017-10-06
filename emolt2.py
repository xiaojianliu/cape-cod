# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 01:05:39 2017

@author: xiaojian
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pytz
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pytz import timezone
import numpy as np
import csv
from scipy import  interpolate
from matplotlib.dates import date2num,num2date
f = np.genfromtxt('eMOLT_2012_2016_CCBay.csv',dtype=None,names=['s','t','lat','lon','deep','tem'],delimiter=',',skip_header=1)  
n=[0]
for a in np.arange(len(f['s'])-1):
    if f['s'][a]!=f['s'][a+1]:
        n.append(a+1)
n.append(len(f)-1)

fig=plt.figure(figsize=(14,5))
axes1=fig.add_subplot(1,2,1)
axes2=fig.add_subplot(1,2,2)

#axes3=fig.add_subplot(2,2,3)
###############################################
#fig,axes=plt.subplots(1,2,figsize=(17,6))

lon10=np.linspace(-70.45,-70.2,10)
lat10=np.linspace(42.05,41.8,10)
axes1.axis([-70.75,-69.8,41.5,42.23])
axes1.scatter(lon10,lat10,color='red',s=7)


FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans
"""
nan nan
-77.953942	34.000067
-77.953949	34.000000
nan nan
-77.941035	34.000067
-77.939568	34.001241
-77.939275	34.002121
-77.938688	34.003001
-77.938688	34.003881
"""
label=['A','B','C','D','E','F','G','H','I','J']
dian=['a','b','c','d','e','f','g','h','i','j']


for a in np.arange(len(label)):
    axes1.text(lon10[a]-0.05,lat10[a]-0.03,label[a],fontsize=12)
CL=np.genfromtxt(FNCL,names=['lon','lat'])
axes2.axis([-70.75,-69.8,41.5,42.23])
"""
for a in np.arange(len(n)-1):
    if f['s'][n[a]]=='RM03' or f['s'][n[a]]=='BS02':
        pass
    elif f['s'][n[a]]=='AB01':
        axes2.scatter(f['lon'][n[a]],f['lat'][n[a]],s=7,color='red')
        axes2.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.04,f['s'][n[a]],fontsize=12)
    else:
        axes2.scatter(f['lon'][n[a]],f['lat'][n[a]],s=7,color='red')
        axes2.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=12)
"""
axes1.plot(CL['lon'],CL['lat'])
axes2.plot(CL['lon'],CL['lat'])
axes1.xaxis.tick_top() 
axes2.xaxis.tick_top()
#axes2.set_yticklabels([])
axes1.set_xlabel('a',fontsize=12)
axes2.set_xlabel('b',fontsize=12)
#axes3.set_xlabel('c',fontsize=12)

lat=np.linspace(41.8,42.4,10)
lon=np.linspace(-70.15,-70.75,10)

#CL=np.genfromtxt(FN,names=['lon','lat'])
#axes3.plot(CL['lon'],CL['lat'])
axes2.axis([-70.94,-70.0,41.52659,42.562711])
axes2.scatter(lon,lat,s=7,color='red')
for a in np.arange(len(lon)):
    axes2.text(lon[a]-0.05,lat[a],dian[a],fontsize=12)
axes2.xaxis.tick_top() 
plt.savefig('emolt2',dpi=400)


time=[]
for a in np.arange(len(f)):
    time.append(datetime.strptime(f['t'][a], '%Y-%m-%d'+'T'+'%H:%M:%SZ'))
for a in np.arange(len(n)-1):
    np.save(f['s'][n[a]],f['s'][n[a]:n[a+1]])
for a in np.arange(len(n)-1):
    np.save(f['s'][n[a]]+'time',time[n[a]:n[a+1]])
for a in np.arange(len(n)-1):
    np.save(f['s'][n[a]]+'tem',f['tem'][n[a]:n[a+1]])
plt.figure(figsize=(10,5))
t2012t=[]
ttem2012t=[]
tff2012=[]
for a in np.arange(len(n)-1):
    tf=np.load(f['s'][n[a]]+'.npy')
    t=np.load(f['s'][n[a]]+'time.npy')
    tem=np.load(f['s'][n[a]]+'tem.npy')
    tt=[]
    ttem=[]
    tff=[]
    for b in np.arange(len(t)):
        if t[b]>=datetime(2012,11,1) and t[b]<=datetime(2013,1,1):
            tt.append(t[b])
            ttem.append(tem[b])
            tff.append(tf[b])
    try:
        plt.plot(tt,ttem,label=tff[0])
        t2012t.append(tt)
        ttem2012t.append(ttem)
        tff2012.append(tff[0])
    except:
        continue


np.save('t2012t',t2012t)
np.save('ttem2012t',ttem2012t)
np.save('tff2012',tff2012)

plt.legend()
plt.savefig('2012emolt',dpi=400)
import numpy as np
#from scipy import interpolate
import matplotlib.pyplot as plt
from scipy import interpolate

plt.figure(figsize=(10,5))
for a in np.arange(len(n)-1):
    tf=np.load(f['s'][n[a]]+'.npy')
    t=np.load(f['s'][n[a]]+'time.npy')
    tem=np.load(f['s'][n[a]]+'tem.npy')
    tt=[]
    ttem=[]
    tff=[]
    for b in np.arange(len(t)):
        if t[b]>=datetime(2013,11,1) and t[b]<=datetime(2014,1,1):
            tt.append(t[b])
            ttem.append(tem[b])
            tff.append(tf[b])
    try:
        plt.plot(tt,ttem,label=tff[0])
    except:
        continue
plt.legend()
plt.savefig('2013emolt',dpi=400)
t2014=[]
tem2014=[]
plt.figure(figsize=(10,5))
for a in np.arange(len(n)-1):
    tf=np.load(f['s'][n[a]]+'.npy')
    t=np.load(f['s'][n[a]]+'time.npy')
    tem=np.load(f['s'][n[a]]+'tem.npy')
    tt=[]
    ttem=[]
    tff=[]
    tt0=[]
    for b in np.arange(len(t)):
        if t[b]>=datetime(2013,11,1) and t[b]<=datetime(2014,1,1):
            #print '2013'
            tt.append(t[b])
            ttem.append(tem[b])
            tff.append(tf[b])
            tt0.append((t[b]-datetime(2013,11,1)).days*24+(t[b]-datetime(2013,11,1)).seconds/float(60*60))
    print 'tt0',len(tt0)
    print 'ttem',len(ttem)
    print a
    if len(tt0)!=0:
        #try:
            
        ff = interpolate.interp1d(tt0, ttem, kind='cubic')
        nx = np.linspace(1, int(tt0[-1]), int(tt0[-1]))
        ny=[]
        for aa in np.arange(len(nx)):
            ny.append(ff(nx[aa]).tolist())
        print 'nx',len(nx),nx[0],nx[-1]
        print 'ny',len(ny),ny[0],ny[-1]
        print '2014',len(tt)
        t2014.append(nx)
        tem2014.append(ny)
        plt.plot(tt,ttem,label=tff[0])
        #plt.plot(nx,ny,color='black',label='Mean')
        #except:
        #    continue
plt.legend()
plt.savefig('2014emolt',dpi=400)
tt2014=[]
ttemp2014=[]
for a in np.arange(len(t2014)):
    ha1=[]
    ha=[]
    for b in np.arange(len(t2014[a])):
        ha.append(datetime(2013,11,1)+timedelta(hours=t2014[a][b]))
        ha1.append(tem2014[a][b])
    tt2014.append(ha)
    ttemp2014.append(ha1)
    
ttemp2014mean=[]
for a in np.arange(947):#len(ttemp2014[0])-1):
    #print '201420142014'
    #print ttemp2014[0][a],ttemp2014[1][a],ttemp2014[2][a],ttemp2014[3][a],ttemp2014[4][a],ttemp2014[5][a]
    #print a
    ttemp2014mean.append((ttemp2014[0][a]+ttemp2014[1][a]+ttemp2014[2][a]+ttemp2014[3][a]+ttemp2014[4][a]+ttemp2014[5][a])/float(6))
plt.figure(figsize=(10,5))
plt.plot(tt2014[0][0:947],ttemp2014mean,color='black')
plt.savefig('2013temp_mean',dpi=700)
np.save('2013mean_temp',ttemp2014mean)
np.save('2013mean_time',tt2014[0][0:947])


plt.figure(figsize=(10,5))
for a in np.arange(len(n)-1):
    tf=np.load(f['s'][n[a]]+'.npy')
    t=np.load(f['s'][n[a]]+'time.npy')
    tem=np.load(f['s'][n[a]]+'tem.npy')
    tt=[]
    ttem=[]
    tff=[]
    for b in np.arange(len(t)):
        if t[b]>=datetime(2015,11,1) and t[b]<=datetime(2016,1,1):
            tt.append(t[b])
            ttem.append(tem[b])
            tff.append(tf[b])
    try:
        plt.plot(tt,ttem,label=tff[0])
    except:
        continue
plt.legend()
plt.savefig('2015emolt',dpi=400)

