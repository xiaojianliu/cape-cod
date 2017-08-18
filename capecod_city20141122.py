# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 02:29:45 2017

@author: xiaojian
"""
import numpy as np
import matplotlib.pyplot as plt

c = np.genfromtxt('strandings20141122.csv',dtype=None,names=['a1','a2','a3','a4','a5','a6','a7','a8'],delimiter=',',skip_header=1)  
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
lon=[-70.0490,-69.9740,-69.9897,-70.0828,-70.0310,-70.1786]
lat=[41.9948,41.8300,41.7898,41.7601,41.9305,42.0584]
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
plt.axis([-70.75,-69.8,41.5,42.23])
for a in np.arange(len(num)):
    plt.scatter(lon[a],lat[a],s=num[a]*7,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])