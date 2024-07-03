import lkTables
import numpy as np
import glob
lookupT=lkTables.scattTables()

bwy=[32.1,32.1,18.1,18.1,16.,15.6,15.6,7.2,7.2]
bwx=[19.4,19.4,10.9,10.9,9.7,9.4,9.4,4.4,4.4]
bwx=np.array(bwx)
bwy=np.array(bwy)

def antenna_pattern(bwx, bwy):
    bpatt=np.zeros((9,7),float)
    for i in range(9):
        for j in range(7):
            ddx=(i-4)*5
            ddy=(j-3)*5
            y2=(((ddx/bwx)**2+(ddy/bwy)**2)*4*np.log(2.))
            bpatt[i,j]=np.exp(-y2)
    return bpatt

ant_pattL=[]
for i in range(9):
    ant_patt=antenna_pattern(bwx[i], bwy[i])
    ant_pattL.append(ant_patt/ant_patt.sum())

import netCDF4 as nc
def readCMB(fname): # reads relevant data from the CMB file
    fh_cmb=nc.Dataset(fname)
    qv=fh_cmb["KuKaGMI/vaporDensity"][:,:,:]
    press=fh_cmb["KuKaGMI/airPressure"][:,:,:]
    envNodes=fh_cmb["KuKaGMI/envParamNode"][:,:,:]
    airTemp=fh_cmb["KuKaGMI/airTemperature"][:,:,:]
    skTemp=fh_cmb["KuKaGMI/skinTemperature"][:,:]
    binNodes=fh_cmb["KuKaGMI/phaseBinNodes"][:,:]
    pwc=fh_cmb["KuKaGMI/precipTotWaterCont"][:,:,:]
    sfcEmiss=fh_cmb["KuKaGMI/surfEmissivity"][:,:,:]
    dm=fh_cmb["KuKaGMI/precipTotDm"][:,:,:]
    cldw=fh_cmb["KuKaGMI/cloudLiqWaterCont"][:,:,:]
    sfcBin=fh_cmb["KuKaGMI/Input/surfaceRangeBin"][:,:,:]
    zCorrected=fh_cmb["KuGMI/correctedReflectFactor"][:,:,:]
    pType=fh_cmb["KuKaGMI/Input/precipitationType"][:,:]
    lon=fh_cmb["KuKaGMI/Longitude"][:,:]
    lat=fh_cmb["KuKaGMI/Latitude"][:,:]
    return qv,press,envNodes,airTemp,skTemp,binNodes,pwc,sfcEmiss,dm,cldw,sfcBin,zCorrected,pType,lon,lat

import radtran as rt