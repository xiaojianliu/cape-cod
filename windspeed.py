# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 20:55:51 2017

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
def sh_bindata(x, y, z, xbins, ybins):
    """
    Bin irregularly spaced data on a rectangular grid.

    """
    ix=np.digitize(x,xbins)
    iy=np.digitize(y,ybins)
    xb=0.5*(xbins[:-1]+xbins[1:]) # bin x centers
    yb=0.5*(ybins[:-1]+ybins[1:]) # bin y centers
    zb_mean=np.empty((len(xbins)-1,len(ybins)-1),dtype=z.dtype)
    zb_median=np.empty((len(xbins)-1,len(ybins)-1),dtype=z.dtype)
    zb_std=np.empty((len(xbins)-1,len(ybins)-1),dtype=z.dtype)
    zb_num=np.zeros((len(xbins)-1,len(ybins)-1),dtype=int)    
    for iix in range(1,len(xbins)):
        for iiy in range(1,len(ybins)):
#            k=np.where((ix==iix) and (iy==iiy)) # wrong syntax
            k,=np.where((ix==iix) & (iy==iiy))
            zb_mean[iix-1,iiy-1]=np.mean(z[k])
            zb_median[iix-1,iiy-1]=np.median(z[k])
            zb_std[iix-1,iiy-1]=np.std(z[k])
            zb_num[iix-1,iiy-1]=len(z[k])
            
    return xb,yb,zb_mean,zb_median,zb_std,zb_num

lon=np.load('lon.npy')
lat=np.load('lat.npy')
d=[]
num=np.load('numcope.npy')
FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

x=[]
y=[]
for a in np.arange(len(num)):
    x.append(lon[num[a]])
    y.append(lat[num[a]])
uwind=np.load('uwind_stress20141118.npy')
vwind=np.load('vwind_stress20141118.npy')

u=np.load('u20141118.npy')
v=np.load('v20141118.npy')

xi = np.arange(-70.75,-69.8,0.05)
yi = np.arange(41.5,42.23,0.05)

xb,yb,ub_mean,ub_median,ub_std,ub_num = sh_bindata(np.array(x), np.array(y), np.array(uwind), xi, yi)
xb,yb,vb_mean,vb_median,vb_std,vb_num = sh_bindata(np.array(x), np.array(y), np.array(vwind), xi, yi)

xb1,yb1,ub_mean1,ub_median1,ub_std1,ub_num1 = sh_bindata(np.array(x), np.array(y), np.array(u), xi, yi)
xb1,yb1,vb_mean1,vb_median1,vb_std1,vb_num1 = sh_bindata(np.array(x), np.array(y), np.array(v), xi, yi)


xxb,yyb = np.meshgrid(xb, yb)
fig=plt.figure(figsize=(15,10))
ax1=fig.add_subplot(2,2,1)#plt.figure()
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=ax1.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=ax1.quiverkey(Q,0.1,0.5,0.5, r'$0.1pa$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')

#plt.plot(coast_lon,coast_lat,'b.')
ax1.plot(CL['lon'],CL['lat'])
ax1.axis([-70.75,-69.8,41.5,42.23])

ax2=fig.add_subplot(2,2,2)#plt.figure()
ub1 = np.ma.array(ub_mean1, mask=np.isnan(ub_mean))
vb1 = np.ma.array(vb_mean1, mask=np.isnan(vb_mean))
Q=ax2.quiver(xxb,yyb,ub1.T,vb1.T,scale=5.)
qk=ax2.quiverkey(Q,0.1,0.4,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')

#plt.plot(coast_lon,coast_lat,'b.')
ax2.plot(CL['lon'],CL['lat'])
ax2.axis([-70.75,-69.8,41.5,42.23])
ax3=fig.add_subplot(2,2,3)#plt.figure()
##################################################################
####################################################################
c = np.genfromtxt('strandings20141118.csv',dtype=None,names=['a1','a2','a3','a4','a5','a6','a7','a8'],delimiter=',',skip_header=1)  
news=[]
for a in c['a6']:
    print a
    if a not in news:
        news.append(a)
num=[]
for a in np.arange(len(news)):
    j=0
    for b in np.arange(len(c['a6'])):
        if news[a]==c['a6'][b]:
            j=j+1
    num.append(j)
            
    news[a]
lon=[-70.0490,-69.9740,-69.9897,-70.0310,-69.9598,-70.0828,-70.1786,-70.6345,-70.5989,-70.1939,-70.0972,-70.9078]
lat=[41.9948,41.8300,41.7898,41.9305,41.6821,41.7601,42.0584,41.6043,41.7413,41.7353,42.0393,42.3021]
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
CL=np.genfromtxt(FNCL,names=['lon','lat'])
ax3.axis([-70.75,-69.8,41.5,42.23])
for a in np.arange(len(num)):
    ax3.scatter(lon[a],lat[a],s=num[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax3.plot(CL['lon'],CL['lat'])
ax3.text(lon[0]+0.05,lat[0],news[0])
ax3.text(lon[1]+0.05,lat[1],news[1])
ax3.text(lon[2]+0.06,lat[2],news[2])
ax3.text(lon[3]+0.05,lat[3],news[3])
ax3.text(lon[4]+0.03,lat[4],news[4])
ax3.text(lon[5]-0.05,lat[5]+0.05,news[5])
ax3.text(lon[6]-0.05,lat[6]+0.05,news[6])
ax3.text(lon[7]+0.005,lat[7]+0.01,news[7])
ax3.text(lon[8]+0.02,lat[8],news[8])
ax3.text(lon[9]-0.05,lat[9]-0.04,news[9])
ax3.text(lon[10]+0.04,lat[10]+0.01,news[10])
#ax0.xaxis.tick_top() 
ax1.xaxis.tick_top() 
ax2.xaxis.tick_top() 
ax3.xaxis.tick_top()
ax2.set_yticklabels([])
ax3.set_xticklabels([])
ax1.set_xlabel('a')
ax2.set_xlabel('b')
ax3.set_xlabel('c')
 
#############################################################
##############################################################
###########################################################
"""
ax4=fig.add_subplot(2,2,4)#plt.figure()
tt2014=np.load('tt2014.npy')
h2014=np.load('h2014.npy')
t2014=[]
h04=[]
#ttt.append('''%s/%s'''%(time2013[a].month,time2013[a].day))
"""
"""
for a in np.arange(len(tt2014)):
    t2014.append('''%s/%s'''%(tt2014[len(tt2014)-1-a].month,tt2014[len(tt2014)-1-a].day))
    h04.append(h2014[len(tt2014)-1-a])
data2010s=pd.Series(h04,index=list(t2014))
data2010s.plot(kind='bar',ax=ax4)#,label=dian[a])
"""
"""
ax4.set_title('2014')
ax4.bar(tt2014,h2014,width=0.5,label='retention')
"""
uwindx=np.load('uwind_stress201411_1_30.npy')
vwindx=np.load('vwind_stress201411_1_30.npy')
xb2,yb2,ub_mean2,ub_median2,ub_std2,ub_num2 = sh_bindata(np.array(x), np.array(y), np.array(uwindx), xi, yi)
xb2,yb2,vb_mean2,vb_median2,vb_std2,vb_num2 = sh_bindata(np.array(x), np.array(y), np.array(vwindx), xi, yi)

ax4=fig.add_subplot(2,2,4)#plt.figure()
ub2 = np.ma.array(ub_mean2, mask=np.isnan(ub_mean))
vb2 = np.ma.array(vb_mean2, mask=np.isnan(vb_mean))
Q=ax4.quiver(xxb,yyb,ub2.T,vb2.T,scale=5.)
qk=ax4.quiverkey(Q,0.1,0.4,0.5,r'$0.1pa$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')

#plt.plot(coast_lon,coast_lat,'b.')
ax4.plot(CL['lon'],CL['lat'])
ax4.axis([-70.75,-69.8,41.5,42.23])
ax4.set_yticklabels([])
ax4.set_xticklabels([])
ax4.set_xlabel('d')
plt.savefig('speedwind18x',dpi=300)