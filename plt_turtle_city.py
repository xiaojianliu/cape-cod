# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 00:37:37 2017

@author: xiaojian
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import  Axes3D
from matplotlib import  cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
import netCDF4
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import csv
import math
from matplotlib.path import Path
from scipy import  interpolate
from matplotlib.path import Path
from dateutil.parser import parse
from math import radians, cos, sin, atan, sqrt  
from matplotlib.dates import date2num,num2date
from sympy import * 
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
c2 = np.genfromtxt('strandings2012C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)  
cc2=[]
for a in c2['a3']:
    if a not in cc2:
        cc2.append(a)

clat2=[41.7353,41.7088,41.7898,41.7003,41.9948,41.8300,41.9305,41.7601,41.5265,41.5532,42.2918,41.9584,41.7615,41.7056,41.7590,41.7426,41.7413,41.2835,42.2418]
clon2=[-70.1939,-70.2134,-69.9897,-70.3002,-70.0490,-69.9740,-70.0310,-70.0828,-70.6731,-70.6086,-70.8745,-70.6673,-70.7197,-70.2287,-70.4939,-70.1620,-70.5989,-70.0995,-70.8898]

c3 = np.genfromtxt('strandings2013C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)  
cc3=[]
for a in c3['a3']:
    if a not in cc3:
        cc3.append(a)

clat3=[41.7601,41.7353,41.8300,42.0584,41.9305,41.9948,41.7003,41.7601,41.7898,41.3744]
clon3=[-70.0828,-70.1939,-69.9740,-70.1786,-70.0310,-70.0490,-70.3002,-70.0828,-69.9897,-70.4729]

c4 = np.genfromtxt('strandings2014C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)  
cc4=[]
for a in c4['a3']:
    if a not in cc4:
        cc4.append(a)
clat4=[41.9305,41.9948,41.3805,41.7003,41.7353,41.7601,41.7898,41.8300,42.3021,42.0584,41.7088,41.7413,41.7590,41.5532,41.2835,41.6821,41.6043,42.0393]
clon4=[-70.0310,-70.0490,-70.6455,-70.3002,-70.1939,-70.0828,-69.9897,-69.9740,-70.9078,-70.1786,-70.2134,-70.5989,-70.4939,-70.6086,-70.0995,-69.9598,-70.6345,-70.0972]

c5 = np.genfromtxt('strandings2015C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)  
cc5=[]
for a in c5['a3']:
    if a not in cc5:
        cc5.append(a)
clat5=[41.9305,41.9584,41.9948,41.7353,42.2418,41.7003,41.3812,41.7590,42.0584,41.8300,41.7898,42.3021,41.7601,41.7615,41.7056,41.5532,41.2835,42.0418]
clon5=[-70.0310,-70.6673,-70.0490,-70.1939,-70.8898,-70.3002,-70.6745,-70.4939,-70.1786,-69.9740,-69.9897,-70.9078,-70.0828,-70.7197,-70.2287,-70.6086,-70.0995,-70.6723]
ct=[]
lon=[]
lat=[]
for a in np.arange(len(cc2)):
    ct.append(cc2[a])
    lon.append(clon2[a])
    lat.append(clat2[a])
for a in np.arange(len(cc3)):
    ct.append(cc3[a])
    lon.append(clon3[a])
    lat.append(clat3[a])
for a in np.arange(len(cc4)):
    ct.append(cc4[a])
    lon.append(clon4[a])
    lat.append(clat4[a])
for a in np.arange(len(cc5)):
    ct.append(cc5[a])
    lon.append(clon5[a])
    lat.append(clat5[a])
ct1=[]
clon1=[]
clat1=[]
for a in ct:
    if a not in ct1:
        ct1.append(a)
index=[]
for a in np.arange(len(ct1)):
    for b in np.arange(len(ct)):
        if ct1[a]==ct[b]:
            index.append(b)
            #ct[b]='c%s'%(b)
for a in lon:
    if a not in clon1:
        clon1.append(a)
for a in lat:
    if a not in clat1:
        clat1.append(a)
lonx=[-70.1939,-70.2134,-69.9897,-70.3002,-70.0490,-69.9740,-70.0310,-70.0828,-70.6731,-70.6086,-70.8745,-70.6673,-70.7197,-70.2287,-70.4939,-70.1620,-70.5989,-70.0995,-70.8898,-70.1786,-70.4729,-70.6455,-70.9078,-69.9598,-70.6345,-70.0972,-70.6745,-70.6723]
latx=[41.7353,41.7088,41.7898,41.7003,41.9948,41.8300,41.9305,41.7601,41.5265,41.5532,42.2918,41.9584,41.7615,41.7056,41.7590,41.7426,41.7413,41.2835,42.2418,42.0584,41.3744,41.3805,42.3021,41.6821,41.6043,42.0393,41.3812,42.0418]
fig,axes=plt.subplots(1,1,figsize=(10,7))
#plt.scatter(lonx,latx,color='red')
for a in np.arange(len(ct1)):
    if ct1[a]=='Hull':
        plt.text(lonx[a]+0.03,latx[a]+0.01,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='Nantasket Beach':
        plt.text(lonx[a]+0.03,latx[a]-0.015,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='Hingham':
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='Duxbury':
        plt.text(lonx[a]-0.12,latx[a],ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='Wareham':
        plt.text(lonx[a],latx[a]+0.03,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='West Falmouth':
        pass
    elif ct1[a]=='East Dennis':
        pass
    elif ct1[a]=='Yarmouth Port':
        pass
    elif ct1[a]=='North Truro':
        pass
    elif ct1[a]=='Woods Hole':
        plt.text(lonx[a]-0.12,latx[a]+0.03,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='Chatham':
        plt.text(lonx[a]+0.04,latx[a]+0,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=='West Tisbury':
        plt.text(lonx[a]-0.22,latx[a]+0,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=="Martha's Vineyard":
        plt.text(lonx[a]-0.02,latx[a]-0.08,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=="Chappaquiddick":
        plt.text(lonx[a]+0.03,latx[a]-0.,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
    elif ct1[a]=="Nantucket":
        plt.text(lonx[a]-0.12,latx[a]+0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red',label='other towns')
    elif ct1[a]=="Barnstable":
        plt.text(lonx[a]-0.06,latx[a]+0.06,ct1[a])
        plt.scatter(lonx[a],latx[a],color='yellow')
    elif ct1[a]=="Yarmouth":
        plt.text(lonx[a]-0.06,latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='yellow')
    elif ct1[a]=="Brewster":
        plt.text(lonx[a]-0.04,latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='yellow')
    elif ct1[a]=="Provincetown":
        plt.text(lonx[a]-0.04,latx[a]+0.05,ct1[a])
        plt.scatter(lonx[a],latx[a],color='green')
    elif ct1[a]=="Truro":
        plt.text(lonx[a]+0.04,latx[a]+0.01,ct1[a])
        plt.scatter(lonx[a],latx[a],color='green')
    elif ct1[a]=="Wellfleet":
        plt.text(lonx[a]+0.05,latx[a]+0.0,ct1[a])
        plt.scatter(lonx[a],latx[a],color='green')
    elif ct1[a]=="Eastham":
        plt.text(lonx[a]+0.05,latx[a]+0.0,ct1[a])
        plt.scatter(lonx[a],latx[a],color='green',label="'Outer Cape' Towns")
    elif ct1[a]=="Orleans":
        plt.text(lonx[a]+0.06,latx[a]-0.02,ct1[a])
        plt.scatter(lonx[a],latx[a],color='green')
    elif ct1[a]=="Dennis":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='yellow')
    elif ct1[a]=="Sandwich":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='yellow',label="'Mid Cape' Towns")
    else:
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red')
FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])
plt.plot(CL['lon'],CL['lat'],'b-')
plt.axis([-71.00,-69.8,41.2,42.38])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
plt.legend()
axes.xaxis.tick_top() 
plt.savefig('turtle_city',dpi=400)