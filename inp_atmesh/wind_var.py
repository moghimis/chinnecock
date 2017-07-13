import netCDF4
import numpy as np

#Change time vector
nc  = netCDF4.Dataset('wind_atm_fin_ch_time_vec.nc','r+')
ncv = nc.variables

uw = ncv['uwnd'][:]
vw = ncv['vwnd'][:]
pp = ncv['P'][:]
ut = np.linspace(0,5,len(uw))
ud = np.linspace(1,3,len(uw[0,:]))
for it in range(len(uw)):
    uw[it,:] =  ut[it] * ud
    vw[it,:] = -ut[it] * ud
    pp[it,:] = 1e5  + 10 * ut[it] * ud
ncv['uwnd'][:] = uw
ncv['vwnd'][:] = vw
ncv['P'   ][:] = pp
nc.close()
#####


