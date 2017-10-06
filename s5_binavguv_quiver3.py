#http://www.ngdc.noaa.gov/mgg/coast/
# coast line data extractor

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:27:09 2012

@author: vsheremet
"""
import numpy as np
#from pydap.client import open_url
import matplotlib.pyplot as plt
#from SeaHorseLib import *
#from datetime import *
#from scipy import interpolate
#import sys
#from SeaHorseTide import *
#import shutil
import matplotlib.mlab as mlab
import matplotlib.cm as cm
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
"""
from netCDF4 import Dataset

# read in etopo5 topography/bathymetry.
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
etopodata = Dataset(url)

topoin = etopodata.variables['ROSE'][:]
lons = etopodata.variables['ETOPO05_X'][:]
lats = etopodata.variables['ETOPO05_Y'][:]
# shift data so lons go from -180 to 180 instead of 20 to 380.
topoin,lons = shiftgrid(180.,topoin,lons,start=False)
"""



"""
BATHY=np.genfromtxt('necscoast_noaa.dat',dtype=None,names=['coast_lon', 'coast_lat'])
coast_lon=BATHY['coast_lon']
coast_lat=BATHY['coast_lat']
"""

#BATHY=np.genfromtxt('coastlineNE.dat',names=['coast_lon', 'coast_lat'],dtype=None,comments='>')
#coast_lon=BATHY['coast_lon']
#coast_lat=BATHY['coast_lat']


# www.ngdc.noaa.gov
# world vector shoreline ascii
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


FN='binned_drifter01.npz'
#FN='binned_model.npz'
Z=np.load(FN) 
xb=Z['xb']
yb=Z['yb']
ub_mean=Z['ub_mean']
ub_median=Z['ub_median']
ub_std=Z['ub_std']
ub_num=Z['ub_num']
vb_mean=Z['vb_mean']
vb_median=Z['vb_median']
vb_std=Z['vb_std']
vb_num=Z['vb_num']
Z.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
fig,axes=plt.subplots(2,2,figsize=(15,10))
#plt.figure()
plt.subplots_adjust(wspace=0.07,hspace=0.07)
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=axes[0,0].quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=axes[0,0].quiverkey(Q,0.1,0.45,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')

#plt.plot(coast_lon,coast_lat,'b.')
axes[0,0].plot(CL['lon'],CL['lat'])
axes[0,0].set_xlabel('a')
"""
axes[0,0].text(-65.8,44.5,'Bay of Fundy',fontsize=12)
#axes[1].text(-67.5,41.5,'Georges Bank',fontsize=7)
axes[0,0].plot([-68.8,-68.5],[44.4,44.7],'y-')
axes[0,0].plot([-65.8,-66.3],[44.5,44.7],'y-')
axes[0,0].plot([-67,-68],[43.4,43.5],'y-')
axes[0,0].plot([-70.8,-70],[44,42.8],'y-')
axes[0,0].plot([-70.2,-70],[43.85,43.75],'y-')
axes[0,0].plot([-69.8,-69.8],[44.25,44.1],'y-')
axes[0,0].plot([-67.5,-67.6],[45.25,45.15],'y-')
axes[0,0].plot([-66.1,-66.2],[45.25,45.25],'y-')
axes[0,0].plot([-68.85,-70],[44.6,44.7],'y-')
#axes[1].text(-70.5,44.7,'Penobscot River',fontsize=7)
axes[0,0].text(-66.9,45.24,'St. John River',fontsize=12)
axes[0,0].text(-67.85,45.1,'St. Croix River',fontsize=12)
axes[0,0].text(-67.7,44.8,'Eastern',fontsize=12)
axes[0,0].text(-67.7,44.72,'Maine',fontsize=12)
#axes[1].text(-69.4,44.2,'Western',fontsize=7)
#axes[1].text(-69.4,44.1,'Maine',fontsize=7)
#axes[1].text(-70.4,44.3,'Kennebec River',fontsize=7)
#axes[1].text(-70.7,45,'Maine',fontsize=7)
#axes[0].text(-70.6,43.9,'Casco Bay',fontsize=7)
#axes[1].text(-67,43.4,'Jordan Basin',fontsize=7)
axes[0,0].text(-67.8,45,'Grand Manan',fontsize=12)
axes[0,0].text(-67.65,44.92,'Island',fontsize=12)
axes[0,0].plot([-67.5,-66.8],[44.99,44.7],'y-')
#axes[1].text(-69,44.7,'Penobscot Bay',fontsize=7)
axes[0,0].text(-66,44.0,'Nova Scotia',fontsize=12)
#axes[1].text(-70.9,44,'Wikkson Basin',fontsize=7)
"""
axes[0,0].axis([-70.75,-69.8,41.5,42.23])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
axes[0,0].xaxis.tick_top() 

#plt.show()
###################################################################################33
#FN='binned_drifter01.npz'
FN='binned_model01.npz'
Z1=np.load(FN) 
xb1=Z1['xb']
yb1=Z1['yb']
ub_mean1=Z1['ub_mean']
ub_median1=Z1['ub_median']
ub_std1=Z1['ub_std']
ub_num1=Z1['ub_num']
vb_mean1=Z1['vb_mean']
vb_median1=Z1['vb_median']
vb_std1=Z1['vb_std']
vb_num1=Z1['vb_num']
Z1.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
#fig,axes=plt.subplots(3,2,figsize=(7,5))
#plt.figure()
ub1 = np.ma.array(ub_mean1, mask=np.isnan(ub_mean1))
vb1 = np.ma.array(vb_mean1, mask=np.isnan(vb_mean1))
Q=axes[0,1].quiver(xxb,yyb,ub1.T,vb1.T,scale=5.)
qk=axes[0,1].quiverkey(Q,0.1,0.45,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')
axes[1,0].set_xticklabels([])
axes[1,0].set_xlabel('c')
axes[0,1].set_xlabel('b')
#plt.plot(coast_lon,coast_lat,'b.')
axes[0,1].plot(CL['lon'],CL['lat'])
axes[0,1].axis([-70.75,-69.8,41.5,42.23])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
#axes[1,0].xaxis.tick_top() 

for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -70.75<xxb[0][a]<-69.8 and 41.5<yyb[b][0]<42.23 and ub_num[a][b]!=0:
            #plt.text(xxb[0][a],yyb[b][0],ubn[a][b],fontsize='smaller')
            axes[1,0].text(xxb[0][a]-0.03,yyb[b][0]-0.03,ub_num[a][b],fontsize=10)
            #axes[1,1].scatter(xxb[0][a],yyb[b][0],s=ubn[a][b]/float(100),color='red',marker='o')
axes[1,0].plot(CL['lon'],CL['lat'])
axes[1,0].axis([-70.75,-69.8,41.5,42.23])
axes[0,1].xaxis.tick_top() 
axes[0,1].set_yticklabels([])
###########################################
data = np.genfromtxt('sea.csv',dtype=None,names=['x','y','h'],delimiter=',')    
x=[]
y=[]
h=[]
x=data['x']
y=data['y']
h=data['h']
xi = np.arange(-70.75,-69.8,0.03)
yi = np.arange(41.5,42.23,0.03)
xb,yb,hb_mean,hb_median,hb_std,hb_num = sh_bindata(x, y, h, xi, yi)
xxxb,yyyb = np.meshgrid(xb, yb)
for a in np.arange(len(hb_mean)):
    for b in np.arange(len(hb_mean[0])):
        if hb_mean[a][b]>100000:
            hb_mean[a][b]=0
CS=axes[1,1].contour(xxxb, yyyb, -abs(hb_mean.T),colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5'),levels=[-100,-60,-30,-20,-10])
axes[1,1].clabel(CS, inline=1, fontsize=12,fmt='%4.0f')
axes[1,1].plot(CL['lon'],CL['lat'])
axes[1,1].axis([-70.75,-69.8,41.5,42.23])
#axes.xaxis.tick_top() 
axes[1,1].set_xticklabels([])
axes[1,1].set_yticklabels([])
axes[1,1].set_xlabel('d')
'''
for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -67.5<xxb[0][a]<-66.38 and 44.4<yyb[b][0]<44.9 and ub_num[a][b]!=0:
            #plt.text(xxb[0][a],yyb[b][0],ubn[a][b],fontsize='smaller')
            axes[1,1].text(xxb[0][a],yyb[b][0],ub_num1[a][b],fontsize=12)
            #axes[1,1].scatter(xxb[0][a],yyb[b][0],s=ubn[a][b]/float(100),color='red',marker='o')
axes[1,1].plot(CL['lon'],CL['lat'])
axes[1,1].axis([-67.5,-66.37,44.4,44.9])
#axes.xaxis.tick_top() 
axes[1,1].set_xticklabels([])
axes[1,1].set_xlabel('d')
'''
#plt.title('binned_drifter_num')
plt.savefig('drifter4_6to7_8xinn',dpi=400)
"""
#################################################################################################
FN='binned_drifter12067.npz'
#FN='binned_model.npz'
Z2=np.load(FN) 
xb2=Z2['xb']
yb2=Z2['yb']
ub_mean2=Z2['ub_mean']
ub_median2=Z2['ub_median']
ub_std2=Z2['ub_std']
ub_num2=Z2['ub_num']
vb_mean2=Z2['vb_mean']
vb_median2=Z2['vb_median']
vb_std2=Z2['vb_std']
vb_num2=Z2['vb_num']
Z2.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
#fig,axes=plt.subplots(3,2,figsize=(7,5))
#plt.figure()
ub2 = np.ma.array(ub_mean2, mask=np.isnan(ub_mean2))
vb2 = np.ma.array(vb_mean2, mask=np.isnan(vb_mean2))
Q=axes[1,0].quiver(xxb,yyb,ub2.T,vb2.T,scale=5.)
qk=axes[1,0].quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')
axes[1,0].set_yticklabels([])
#plt.plot(coast_lon,coast_lat,'b.')
axes[1,0].plot(CL['lon'],CL['lat'])
axes[1,0].axis([-67.875,-64.75,43.915,45.33])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
axes[1,0].xaxis.tick_top() 
#############################################################################################
FN='binned_drifter12078.npz'
#FN='binned_model.npz'
Z3=np.load(FN) 
xb3=Z3['xb']
yb3=Z3['yb']
ub_mean3=Z3['ub_mean']
ub_median3=Z3['ub_median']
ub_std3=Z3['ub_std']
ub_num3=Z3['ub_num']
vb_mean3=Z3['vb_mean']
vb_median3=Z3['vb_median']
vb_std3=Z3['vb_std']
vb_num3=Z3['vb_num']
Z3.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
#fig,axes=plt.subplots(3,2,figsize=(7,5))
#plt.figure()
ub3 = np.ma.array(ub_mean3, mask=np.isnan(ub_mean3))
vb3 = np.ma.array(vb_mean3, mask=np.isnan(vb_mean3))
Q=axes[1,1].quiver(xxb,yyb,ub3.T,vb3.T,scale=5.)
qk=axes[1,1].quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')
axes[1,1].set_yticklabels([])
#plt.plot(coast_lon,coast_lat,'b.')
axes[1,1].plot(CL['lon'],CL['lat'])
axes[1,1].axis([-67.875,-64.75,43.915,45.33])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
axes[1,1].xaxis.tick_top() 
#############################################################################################
FN='binned_drifter12089.npz'
#FN='binned_model.npz'
Z4=np.load(FN) 
xb4=Z4['xb']
yb4=Z4['yb']
ub_mean4=Z4['ub_mean']
ub_median4=Z4['ub_median']
ub_std4=Z4['ub_std']
ub_num4=Z4['ub_num']
vb_mean4=Z4['vb_mean']
vb_median4=Z4['vb_median']
vb_std4=Z4['vb_std']
vb_num4=Z4['vb_num']
Z4.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
#fig,axes=plt.subplots(3,2,figsize=(7,5))
#plt.figure()
ub4 = np.ma.array(ub_mean4, mask=np.isnan(ub_mean4))
vb4 = np.ma.array(vb_mean4, mask=np.isnan(vb_mean4))
Q=axes[2,0].quiver(xxb,yyb,ub4.T,vb4.T,scale=5.)
qk=axes[2,0].quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')
axes[2,0].set_yticklabels([])
#plt.plot(coast_lon,coast_lat,'b.')
axes[2,0].plot(CL['lon'],CL['lat'])
axes[2,0].axis([-67.875,-64.75,43.915,45.33])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
axes[2,0].xaxis.tick_top() 
plt.savefig('drifter45678',dpi=400)
"""
#############################################################################################
"""

fig,axes=plt.subplots(1,1)#plt.figure()#figsize=(6.25*2,2.83*2))
data = np.genfromtxt('sea.csv',dtype=None,names=['x','y','h'],delimiter=',')    
x=[]
y=[]
h=[]
x=data['x']
y=data['y']
h=data['h']
xi = np.arange(-71.,-64.75,0.03)
yi = np.arange(42.5,45.33,0.03)
xb,yb,hb_mean,hb_median,hb_std,hb_num = sh_bindata(x, y, h, xi, yi)
xxxb,yyyb = np.meshgrid(xb, yb)
for a in np.arange(len(hb_mean)):
    for b in np.arange(len(hb_mean[0])):
        if hb_mean[a][b]>100000:
            hb_mean[a][b]=0
CS=plt.contour(xxxb, yyyb, -abs(hb_mean.T),levels=[-200,-180,-150,-120,-100,-50])
plt.clabel(CS, inline=1, fontsize=5,fmt='%4.0f')

plt.plot(CL['lon'],CL['lat'])
plt.text(-66.7,44.7,'Bay of Fundy',fontsize=7)
plt.text(-67.5,41.5,'Georges Bank',fontsize=7)
plt.plot([-68.8,-68.5],[44.4,44.7],'y-')
plt.text(-68,43.5,'Jordan Basin',fontsize=7)
plt.text(-68.5,45,'Grand Manan Island',fontsize=7)
plt.plot([-67.8,-66.8],[44.99,44.7],'y-')
plt.text(-69,44.7,'Penobscot Bay',fontsize=7)
plt.text(-66,44.0,'Nova Scotia',fontsize=7)
plt.text(-70,42.8,'Wikkson Basin',fontsize=7)
plt.axis([-71,-64.75,42.5,45.33])
axes.xaxis.tick_top() 
plt.savefig('waters',dpi=700)
plt.show()
####################################################################################333
plt.figure()
ub = np.ma.array(ub_std, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_std, mask=np.isnan(vb_mean))
Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=plt.quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

plt.title(FN[:-4]+', std')

#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])
plt.axis([-71,-64.75,42.5,45.33])
plt.savefig('drifter_std120',dpi=700)
plt.show()


"""
fig,axes=plt.subplots(1,1,figsize=(7,5))
for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -68<xxb[0][a]<-64.75 and 44<yyb[b][0]<45.33 and ub_num[a][b]!=0:
            #plt.text(xxb[0][a],yyb[b][0],ubn[a][b],fontsize='smaller')
            axes.text(xxb[0][a],yyb[b][0],ub_num[a][b],fontsize=4)
            #axes[1,1].scatter(xxb[0][a],yyb[b][0],s=ubn[a][b]/float(100),color='red',marker='o')
axes.plot(CL['lon'],CL['lat'])
axes.axis([-68,-64.75,44,45.33])
axes.xaxis.tick_top() 
#axes.set_xlabel('b')
#plt.title('binned_drifter_num')
plt.savefig('drifter_number4_6',dpi=400)#plt.savefig('binned_drifter_num1207777777777778888888888888',dpi=700)
fig,axes=plt.subplots(1,1,figsize=(7,5))
for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -68<xxb[0][a]<-64.75 and 44<yyb[b][0]<45.33 and ub_num[a][b]!=0:
            #plt.text(xxb[0][a],yyb[b][0],ubn[a][b],fontsize='smaller')
            axes.text(xxb[0][a],yyb[b][0],ub_num1[a][b],fontsize=4)
            #axes[1,1].scatter(xxb[0][a],yyb[b][0],s=ubn[a][b]/float(100),color='red',marker='o')
axes.plot(CL['lon'],CL['lat'])
axes.axis([-68,-64.75,44,45.33])
axes.xaxis.tick_top() 
#axes.set_xlabel('b')
#plt.title('binned_drifter_num')
plt.savefig('drifter_number6_8',dpi=400)

fig, ax = plt.subplots(1,2,figsize=(15,5))
ub1 = np.ma.array(ub_std, mask=np.isnan(ub_mean))
vb1 = np.ma.array(vb_std, mask=np.isnan(vb_mean))
p = ax[0].pcolor(xxb, yyb, ub1.T)#, cmap=matplotlib.cm.RdBu, vmin=((dvf-mvf).T).min(), vmax=((dvf-mvf).T).max())
cb = fig.colorbar(p, ax=ax[0])
ax[0].plot(CL['lon'],CL['lat'])
ax[0].axis([-67.875,-64.75,43.915,45.33])
Q=plt.quiver(xxb,yyb,ub1.T,vb1.T,scale=5.)
"""
qk=axes[1].quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

axes[1].set_xlabel('b')
axes[1].set_xticklabels([])#axes[1].xaxis.tick_top() 
#plt.plot(coast_lon,coast_lat,'b.')
axes[1].plot(CL['lon'],CL['lat'])
axes[1].axis([-67.875,-64.75,43.915,45.33])
plt.savefig('drifter_mean_std_xxxxxxx',dpi=700)
plt.show()

FN='binned_model12078.npz'
Z=np.load(FN) 
xb=Z['xb']
yb=Z['yb']
ub_mean=Z['ub_mean']
ub_median=Z['ub_median']
ub_std=Z['ub_std']
ub_num=Z['ub_num']
vb_mean=Z['vb_mean']
vb_median=Z['vb_median']
vb_std=Z['vb_std']
vb_num=Z['vb_num']
Z.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])


#fig,axes=plt.subplots(1,1)
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=axes[1].quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=axes[1].quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.title('''Mean current derived from FVCOM (1-20m)''')

#plt.plot(coast_lon,coast_lat,'b.')
axes[1].plot(CL['lon'],CL['lat'])
axes[1].set_xlabel('b')
axes[1].text(-65.8,44.5,'Bay of Fundy',fontsize=12)
#axes[1].text(-67.5,41.5,'Georges Bank',fontsize=7)
axes[1].plot([-68.8,-68.5],[44.4,44.7],'y-')
axes[1].plot([-65.8,-66.3],[44.5,44.7],'y-')
axes[1].plot([-67,-68],[43.4,43.5],'y-')
axes[1].plot([-70.8,-70],[44,42.8],'y-')
axes[1].plot([-70.2,-70],[43.85,43.75],'y-')
axes[1].plot([-69.8,-69.8],[44.25,44.1],'y-')
axes[1].plot([-67.5,-67.6],[45.25,45.15],'y-')
axes[1].plot([-66.1,-66.2],[45.25,45.25],'y-')
axes[1].plot([-68.85,-70],[44.6,44.7],'y-')
#axes[1].text(-70.5,44.7,'Penobscot River',fontsize=7)
axes[1].text(-66.7,45.25,'St. John River',fontsize=7)
axes[1].text(-67.8,45.1,'St. Croix River',fontsize=7)
axes[1].text(-67.7,44.8,'Eastern',fontsize=7)
axes[1].text(-67.7,44.7,'Maine',fontsize=7)
#axes[1].text(-69.4,44.2,'Western',fontsize=7)
#axes[1].text(-69.4,44.1,'Maine',fontsize=7)
#axes[1].text(-70.4,44.3,'Kennebec River',fontsize=7)
#axes[1].text(-70.7,45,'Maine',fontsize=7)
#axes[1].text(-70.6,43.9,'Casco Bay',fontsize=7)
#axes[1].text(-67,43.4,'Jordan Basin',fontsize=7)
axes[1].text(-67.7,45,'Grand Manan Island',fontsize=7)
axes[1].plot([-67.5,-66.8],[44.99,44.7],'y-')
#axes[1].text(-69,44.7,'Penobscot Bay',fontsize=7)
axes[1].text(-66,44.0,'Nova Scotia',fontsize=7)
#axes[1].text(-70.9,44,'Wikkson Basin',fontsize=7)
axes[1].axis([-67.875,-64.75,43.915,45.33])#axis([-71,-64.75,42.5,45.33])
#axes[1].axis([-71,-64.75,42.5,45.33])
axes[1].xaxis.tick_top() 
plt.savefig('model12011111111111112222222222222222277777777777777777788888888888',dpi=500)
plt.show()

plt.figure()
ub = np.ma.array(ub_std, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_std, mask=np.isnan(vb_mean))
Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=plt.quiverkey(Q,0.9,0.6,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

plt.title(FN[:-4]+', std')

#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])
plt.axis([-71,-64.75,42.5,45.33])
plt.savefig('model_std120',dpi=700)
plt.show()

fig,axes=plt.subplots(1,1)#plt.figure()
for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -68<xxb[0][a]<-64.75 and 44<yyb[b][0]<45.33 and ub_num[a][b]!=0:
            #plt.text(xxb[0][a],yyb[b][0],ubn[a][b],fontsize='smaller')
            plt.text(xxb[0][a],yyb[b][0],ub_num[a][b],fontsize=4)
            #axes[1,1].scatter(xxb[0][a],yyb[b][0],s=ubn[a][b]/float(100),color='red',marker='o')
plt.plot(CL['lon'],CL['lat'])
plt.axis([-68,-64.75,44,45.33])
axes.xaxis.tick_top() 
#plt.title('binned_drifter_num')
plt.savefig('binned_drifter_num1207777777777778888888888888',dpi=700)
plt.show()

plt.figure()
#plt.plot(xxb+0.015,yyb+0.015,'r-')
#plt.plot((xxb+0.015).T,(yyb+0.015).T,'r-')
#Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
#qk=plt.quiverkey(Q,0.8,0.1,0.5, r'$50cm/s$', fontproperties={'weight': 'bold'})
for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -71<xxb[0][a]<-67.875 and 43.915<yyb[b][0]<45.33 and  ub_num[a][b]!=0 :
            plt.text(xxb[0][a],yyb[b][0],ub_num[a][b],fontsize=6)
plt.plot(CL['lon'],CL['lat'])
plt.axis([-71,-67.875,43.915,45.33])
plt.title('binned_drifter_num_1')
plt.savefig('binned_num120_1')
plt.show()

plt.figure()
#plt.plot(xxb+0.015,yyb+0.015,'r-')
#plt.plot((xxb+0.015).T,(yyb+0.015).T,'r-')
#Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
#qk=plt.quiverkey(Q,0.8,0.1,0.5, r'$50cm/s$', fontproperties={'weight': 'bold'})
for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -67.875<xxb[0][a]<-64.75 and 43.915<yyb[b][0]<45.33 and  ub_num[a][b]!=0 :
            plt.text(xxb[0][a]-0.06,yyb[b][0],ub_num[a][b],fontsize=4.2)
plt.plot(CL['lon'],CL['lat'])
plt.axis([-67.875,-64.75,43.915,45.33])
plt.title('binned_drifter_num')
plt.savefig('binned_num120_2',dpi=700)
plt.show()
"""