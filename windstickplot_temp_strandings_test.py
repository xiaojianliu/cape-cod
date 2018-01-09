# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:46:51 2017

@author: huimin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num,DateFormatter,WeekdayLocator, MONDAY

year=2014
deep_temp=np.load('deep_temp.npy')
deep_time=np.load('deep_time.npy')
surf_temp=np.load('surf_temp.npy')
surf_time=np.load('surf_time.npy')
tuttle_time_num_u=np.load('tuttle_time_num_u.npy')
tuttle_time_num_v=np.load('tuttle_time_num_v.npy')
tuttle_time_u=np.load('tuttle_time_u.npy')
tuttle_time_v=np.load('tuttle_time_v.npy')
wind_time=np.load('wind_time_u.npy')
wind_u=np.load('wind_u.npy')
wind_v=np.load('wind_v.npy')

fig=plt.figure(figsize=(15,16))
ax1=fig.add_subplot(311)
ax1.set_title(str(year)+' wind stickplot',fontsize=15)
ax1.set_xlabel("a",fontsize=13)

def stick_plot(time, u, v, **kw):
    width = kw.pop('width', 0.002)
    headwidth = kw.pop('headwidth', 0)
    headlength = kw.pop('headlength', 0)
    headaxislength = kw.pop('headaxislength', 0)
    angles = kw.pop('angles', 'uv')
    ax = kw.pop('ax', None)
    
    if angles != 'uv':
        raise AssertionError("Stickplot angles must be 'uv' so that"
                             "if *U*==*V* the angle of the arrow on"
                             "the plot is 45 degrees CCW from the *x*-axis.")

    time, u, v = map(np.asanyarray, (time, u, v))
    if not ax:
        ax = ax1
    q = ax.quiver(date2num(time), [[0]*len(time)], u, v,
                  angles='uv',width=width,  headwidth=headwidth,
                  headlength=headlength, headaxislength=headaxislength,
                  **kw)

    ax.axes.get_yaxis().set_visible(True)
    #ax.set_xlim(-max(u),max(u))
    plt.xticks()
    return q
stick_plot(wind_time,wind_u,wind_v,color='green')
mondays = WeekdayLocator(MONDAY)
ax1.xaxis.set_major_locator(mondays)
weekFormatter = DateFormatter('%b %d %Y')
ax1.xaxis_date()
ax1.xaxis_font = {'size':'13'}
ax1.xaxis.set_major_formatter(weekFormatter)
ax1.axes.get_xaxis().set_ticks([])
ax1.set_xlim(wind_time[0],wind_time[-25])
###########################################

ax2=fig.add_subplot(312)
ax2.set_title(str(year)+' temperture vs strandings on Outer Cape towns',fontsize=15)
ax2.set_xlabel("b",fontsize=13)
ax2.plot(deep_time,deep_temp, label="bottom temperature (emolt)")
ax2.plot(surf_time,surf_temp, label="surface temperature (fvcom)")

ax2.legend(loc='upper right',fontsize=12)
ax21=ax2.twinx()
ax21.bar(tuttle_time_num_u.tolist(),tuttle_time_u.tolist(),width=0.8,alpha=0.5,label="the number of strandings per day")
ax2.set_ylim(7,14)
ax21.set_ylim(0,180)
ax2.set_ylabel("Degrees Celsius",fontsize=15)
ax21.set_ylabel("number",fontsize=15)

ax2.xaxis_font = {'size':'13'}
ax2.xaxis.set_major_locator(mondays)
ax2.xaxis_date()
ax2.xaxis.set_major_formatter(weekFormatter)
plt.xticks(fontsize=13)
ax2.axes.get_xaxis().set_ticks([])
###########################################
ax3=fig.add_subplot(313)
ax3.set_title(str(year)+' temperture vs strandings on Mid Cape towns',fontsize=15)
ax3.set_xlabel("c",fontsize=13)

ax3.plot(deep_time,deep_temp, label="bottom temperature (emolt)")
ax3.plot(surf_time,surf_temp, label="surface temperature (fvcom)")
ax31=ax3.twinx()
ax31.bar(tuttle_time_num_v.tolist(),tuttle_time_v.tolist(),width=0.8,alpha=0.5,label="the number of strandings per day")
ax3.legend(loc='upper right',fontsize=12)
ax3.set_ylim(7,14)
ax31.set_ylim(0,60)
ax3.set_ylabel("Degrees Celsius",fontsize=15)
ax31.set_ylabel("number",fontsize=15)
ax3.xaxis_font = {'size':'13'}
ax3.xaxis.set_major_locator(mondays)
ax3.xaxis_date()
ax3.xaxis.set_major_formatter(weekFormatter)
plt.xticks(fontsize=13)

plt.draw()
plt.savefig(str(year)+'_windstickplot_temp_stranding',dpi=200,bbox_inches = "tight")
plt.show()