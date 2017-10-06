# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 21:15:37 2017

@author: xiaojian
"""
import sys
import datetime as dt
from matplotlib.path import Path
import netCDF4
import matplotlib.pyplot as plt
from dateutil.parser import parse
import numpy as np
import math
import pandas as pd
from datetime import datetime, timedelta
from math import radians, cos, sin, atan, sqrt  
from matplotlib.dates import date2num,num2date
timea2012=np.load('timea2012.npy')
timea2013=np.load('timea2013.npy')
timea2014=np.load('timea2014.npy')
timea2015=np.load('timea2015.npy')

timef2012=np.load('timef2012.npy')
timef2013=np.load('timef2013.npy')
timef2014=np.load('timef2014.npy')
timef2015=np.load('timef2015.npy')

tempf2015=np.load('tempf2015.npy')
tempf2014=np.load('tempf2014.npy')
tempf2013=np.load('tempf2013.npy')
tempf2012=np.load('tempf2012.npy')

tempa2015=np.load('tempa2015.npy')
tempa2014=np.load('tempa2014.npy')
tempa2013=np.load('tempa2013.npy')
tempa2012=np.load('tempa2012.npy')


t1x=np.load('t1x.npy')

t2x=np.load('t2x.npy')

time2012x=np.load('time2012x.npy')

time2013x=np.load('time2013x.npy')

f1temx=np.load('f1temx.npy')

f2temx=np.load('f2temx.npy')

temp2012x=np.load('temp2012x.npy')

temp2013x=np.load('temp2013x.npy')


fig,axes=plt.subplots(4,1,figsize=(12,10))
plt.subplots_adjust(wspace=0.1,hspace=0.35)
'''
TC1=[]
for a in np.arange(len(timea2012[0:-100])):
    TC1.append('%s/%s'%(timea2012[a].month,timea2012[a].day))
TC2=[]
for a in np.arange(len(timef2012[0:-100])):
    TC2.append('%s/%s'%(timef2012[a].month,timef2012[a].day))

data2004c=pd.Series(np.hstack(tempa2012[0:-99]),index=list(TC1))
data2004c.plot(linestyle='-',linewidth=1,ax=axes[0],label='Mooring A')
data2004=pd.Series(np.hstack(tempf2012[0:-99]),index=list(TC2))
data2004.plot(linestyle='-',linewidth=1,ax=axes[0],label='FVCOM')


TC3=[]
for a in np.arange(len(timea2013[0:-100])):
    TC3.append('%s/%s'%(timea2013[a].month,timea2013[a].day))
TC4=[]
for a in np.arange(len(timef2013[0:-100])):
    TC4.append('%s/%s'%(timef2013[a].month,timef2013[a].day))

data2004c1=pd.Series(np.hstack(tempa2013[0:-99]),index=list(TC3))
data2004c1.plot(linestyle='-',linewidth=1,ax=axes[1],label='Mooring A')
data20041=pd.Series(np.hstack(tempf2013[0:-99]),index=list(TC4))
data20041.plot(linestyle='-',linewidth=1,ax=axes[1],label='FVCOM')
'''
"""
axes[0].plot(timea2012[0:-100],tempa2012[0:-99],label='Mooring A')
axes[0].plot(timef2012[0:-100],tempf2012[0:-99],label='FVCOM')

axes[1].plot(timea2013[0:-100],tempa2013[0:-99],label='Mooring A')
axes[1].plot(timef2013[0:-100],tempf2013[0:-99],label='FVCOM')
"""
'''
axes[1,0].plot(timea2014[0:-1],tempa2014,label='Mooring A')
axes[1,0].plot(timef2014[0:-1],tempf2014,label='FVCOM')

axes[1,1].plot(timea2015[0:-1],tempa2015,label='Mooring A')
axes[1,1].plot(timef2015[0:-1],tempf2015,label='FVCOM')
'''
axes[0].plot(timea2012[0:-100],tempa2012[0:-99],label='Mooring A')
axes[1].plot(timea2013[0:-100],tempa2013[0:-99],label='Mooring A')
axes[0].plot(timef2012[0:-100],tempf2012[0:-99],label='FVCOM')
axes[1].plot(timef2013[0:-100],tempf2013[0:-99],label='FVCOM')

axes[0].set_ylabel('Degrees Celsius')
axes[1].set_ylabel('Degrees Celsius')
#axes[0].set_title('2012')
#axes[1].set_title('2013')
axes[0].set_xlabel('a')
axes[1].set_xlabel('b')
axes[0].legend()
axes[1].legend()

axes[2].plot(t1x,f1temx,label='RM04')
axes[3].plot(t2x,f2temx,label='RM04')
axes[2].plot(time2012x,temp2012x,label='FVCOM')
axes[3].plot(time2013x,temp2013x,label='FVCOM')

axes[2].set_ylabel('Degrees Celsius')
axes[3].set_ylabel('Degrees Celsius')
#axes[2].set_title('2012')
#axes[3].set_title('2013')
axes[2].set_xlabel('c')
axes[3].set_xlabel('d')
axes[2].legend()
axes[3].legend()
"""

axes[0].legend()
axes[1].legend()
axes[0].set_title('2012')
axes[1].set_title('2013')
axes[0].set_xlabel('a')
axes[1].set_xlabel('b')

axes[0].set_ylabel('Degrees Celsius')
axes[1].set_ylabel('Degrees Celsius')


plt.savefig('tempmf',dpi=300)
timeb2013=np.load('timeb2013.npy')
timebf2013=np.load('timebf2013.npy')
tempb2013=np.load('tempb2013.npy')
tempbf2013=np.load('tempbf2013.npy')

fig,axes=plt.subplots(1,1,figsize=(11,5))
axes.plot(timeb2013[0:-100],tempb2013[0:-99],label='Mooring A')
axes.plot(timebf2013[0:-100],tempbf2013[0:-99],label='FVCOM')
plt.legend()
plt.ylabel('Degrees Celsius')
"""
plt.savefig('tempmfxinbtest',dpi=300)














