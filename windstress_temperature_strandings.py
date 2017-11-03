# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:52:12 2017

@author: huimin
from xiaojian  CCB_fig12
"""

import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
from scipy import  interpolate
from mpl_toolkits.axes_grid1 import host_subplot
import csv
deep_temp_dk01=np.load('deep_temp_dk01.npy')
deep_temp_rm04=np.load('deep_temp_rm04.npy')
deep_temp2013=np.load('deep_temp2013.npy')
deep_time_dk01=np.load('deep_time_dk01.npy')
deep_time_rm04=np.load('deep_time_rm04.npy')
deep_time2013=np.load('deep_time2013.npy')
surf_temp2012=np.load('surf_temp2012.npy')
surf_temp2013=np.load('surf_temp2013.npy')
surf_time2012=np.load('surf_time2012.npy')
surf_time2013=np.load('surf_time2013.npy')
tuttle_time_num_u2012=np.load('tuttle_time_num_u2012.npy')
tuttle_time_num_u2013=np.load('tuttle_time_num_u2013.npy')
tuttle_time_num_v2012=np.load('tuttle_time_num_v2012.npy')
tuttle_time_num_v2013=np.load('tuttle_time_num_v2013.npy')
tuttle_time_u2012=np.load('tuttle_time_u2012.npy')
tuttle_time_u2013=np.load('tuttle_time_u2013.npy')
tuttle_time_v2012=np.load('tuttle_time_v2012.npy')
tuttle_time_v2013=np.load('tuttle_time_v2013.npy')
wind_time_u2012=np.load('wind_time_u2012.npy')
wind_time_u2013=np.load('wind_time_u2013.npy')
wind_time_v2012=np.load('wind_time_v2012.npy')
wind_time_v2013=np.load('wind_time_v2013.npy')
wind_u2012=np.load('wind_u2012.npy')
wind_u2013=np.load('wind_u2013.npy')
wind_v2012=np.load('wind_v2012.npy')
wind_v2013=np.load('wind_v2013.npy')
tt0=[]
tt1=[]
yy0=[]
yy1=[]
for b in np.arange(len(deep_time_dk01.tolist())):
    tt0.append((deep_time_dk01.tolist()[b]-datetime(2012,11,1)).days*24+(deep_time_dk01.tolist()[b]-datetime(2012,11,1)).seconds/float(60*60))
for b in np.arange(len(deep_time_rm04.tolist())):   
    tt1.append((deep_time_rm04.tolist()[b]-datetime(2012,11,1)).days*24+(deep_time_rm04.tolist()[b]-datetime(2012,11,1)).seconds/float(60*60))

ff0 = interpolate.interp1d(tt0, deep_temp_dk01.tolist(), kind='cubic')
ff1 = interpolate.interp1d(tt1, deep_temp_rm04.tolist(), kind='cubic')
nx = np.linspace(1, int(tt1[-1]), int(tt1[-1]))
tx=[]
for aa in np.arange(len(nx)):
    tx.append(datetime(2012,11,1)+timedelta(hours=nx[aa]))
    yy0.append((ff0(nx[aa]).tolist()+ff1(nx[aa]).tolist())/2.0)
    #yy1.append()

fig=plt.figure(figsize=(18,22))
#ax1=fig.add_subplot(2,2,1)
plt.subplots_adjust(hspace=0.2)
host = host_subplot(411, axes_class=AA.Axes)
plt.subplots_adjust(right=0.9)
host.set_title('2012 eastward wind stress and temperture vs strandings on Outer Cape towns',fontsize=15)
par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))
par2.axis["right"].toggle(all=True)

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)
host.set_xlabel("a",fontsize=500)
host.set_ylabel("pa",fontsize=15)
par1.set_ylabel("Degrees Celsius",fontsize=15)
par2.set_ylabel("number",fontsize=15)
p1, = host.plot(wind_time_u2012,wind_u2012,'g', label="eastward wind stress")

t2012m=[]
te2012m=[]
    #t2012m.append(np.mean(np.array(time2012).T)[a])
#p2, = par1.plot(emolt2014time,emolt2014tem, label="bottom Temperature(emolt)")
p2, = par1.plot(tx,yy0, label="bottom Temperature(emolt)")
p6, = par1.plot(surf_time2012,surf_temp2012, label="surface Temperature(fvcom)")

width1=datetime(2005,4,1,0,0,0)-datetime(2005,3,31,0,0,0)
par2.bar(tuttle_time_u2012.tolist(),tuttle_time_num_u2012.tolist(),width=0.8,alpha=0.5,label="the number of strandings per day")
host.legend(loc='upper left',fontsize=12)
#plt.draw()
'''
plt.savefig('2012uunew',dpi=300)
plt.show()
'''
############################################################################
#ax1=fig.add_subplot(2,2,2)
host = host_subplot(412, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
host.set_title('2012 northward wind stress and temperture vs strandings on Mid Cape towns',fontsize=15)

par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))
par2.axis["right"].toggle(all=True)

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)
host.set_xlabel("b",fontsize=50)
host.set_ylabel("pa",fontsize=15)
par1.set_ylabel("Degrees Celsius",fontsize=20000000000000000)
par2.set_ylabel("number",fontsize=15)
p1, = host.plot(wind_time_v2012,wind_v2012,'g', label="northward wind stress")

t2012m=[]
te2012m=[]
    #t2012m.append(np.mean(np.array(time2012).T)[a])
p2, = par1.plot(tx,yy0, label="bottom Temperature(emolt)")#,fontsize=20)
#p2.set_ylabel("Degrees Celsius",fontsize=20)
p6,= par1.plot(surf_time2012,surf_temp2012, label="surface Temperature(fvcom)")

width1=datetime(2005,4,1,0,0,0)-datetime(2005,3,31,0,0,0)
par2.bar(tuttle_time_v2012.tolist(),tuttle_time_num_v2012.tolist(),width=0.8,alpha=0.5,label="the number of strandings per day")
host.legend(loc='upper right',fontsize=12)
#plt.draw()

############################################################################
#ax1=fig.add_subplot(2,2,2)

host2 = host_subplot(413, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
host2.set_title('2013 eastward wind stress and temperture vs strandings on Outer Cape towns',fontsize=15)

par1 = host2.twinx()
par2 = host2.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))
par2.axis["right"].toggle(all=True)

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)
host2.set_xlabel("c",fontsize=30)
host2.set_ylabel("pa",fontsize=15)
par1.set_ylabel("Degrees Celsius",fontsize=15)
par2.set_ylabel("number",fontsize=15)
p1, = host2.plot(wind_time_u2013,wind_u2013,'g', label="eastward wind stress")

t2012m=[]
te2012m=[]
    #t2012m.append(np.mean(np.array(time2012).T)[a])
#p2, = par1.plot(emolt2014time,emolt2014tem, label="bottom Temperature(emolt)")
p2, = par1.plot(deep_time2013,deep_temp2013, label="bottom Temperature(emolt)")

p6, = par1.plot(surf_time2013,surf_temp2013, label="surface Temperature(fvcom)")

width1=datetime(2005,4,1,0,0,0)-datetime(2005,3,31,0,0,0)
par2.bar(tuttle_time_num_u2013.tolist(),tuttle_time_u2013.tolist(),width=0.8,alpha=0.5,label="the number of strandings per day")
host2.legend(loc='upper right',fontsize=12)
plt.draw()

############################################################################
#ax1=fig.add_subplot(2,2,2)

host2 = host_subplot(414, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
host2.set_title('2013 northward wind stress and temperture vs strandings on Mid Cape towns',fontsize=15)

par1 = host2.twinx()
par2 = host2.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))
par2.axis["right"].toggle(all=True)

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)
host2.set_xlabel("d",fontsize=30)
host2.set_ylabel("pa",fontsize=15)
par1.set_ylabel("Degrees Celsius",fontsize=15)
par2.set_ylabel("number",fontsize=15)
p1, = host2.plot(wind_time_v2013,wind_v2013,'g', label="north wind stress")

t2012m=[]
te2012m=[]
    #t2012m.append(np.mean(np.array(time2012).T)[a])
p2, = par1.plot(deep_time2013,deep_temp2013, label="bottom Temperature(emolt)")
p6, = par1.plot(surf_time2013,surf_temp2013, label="surface Temperature(fvcom)")

width1=datetime(2005,4,1,0,0,0)-datetime(2005,3,31,0,0,0)
par2.bar(tuttle_time_num_v2013.tolist(),tuttle_time_v2013.tolist(),width=0.8,alpha=0.5,label="the number of strandings per day")
host2.legend(loc='best',fontsize=12)
plt.draw()
plt.savefig('2012uunew',dpi=100)
plt.show()