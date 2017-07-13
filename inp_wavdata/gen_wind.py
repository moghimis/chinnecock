import netCDF4


nc  = netCDF4.Dataset('ww3.hwrf.201512_14_15.nc','r+')
ncv = nc.variables

sxx = ncv['sxx'][:]

ncv['uwnd'] = {}
ncv['uwnd'] = sxx[:]/100

ncv['vwnd'] = {}
ncv['vwnd'] = sxx/100

ncv['P']    = {}
ncv['P']    = sxx/100+10000

nc.close()



#Change time vector
nc  = netCDF4.Dataset('wind_atm_fin_ch_time_vec.nc','r+')
nc  = netCDF4.Dataset('ww3.Constant.20151214_sxy_ike_date.nc','r+')

ncv = nc.variables
tim = ncv['time'][:]
t2 = (tim - tim[0]) * 60 +tim[0]
ncv['time'][:] = t2
nc.close()
#####





#  new_ref   =   datetime.datetime(1990,01,01)   - (datetime.datetime(2015,12,14) - datetime.datetime(2008,8,23,0,0,0) )

#!/bin/bash
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/windx.mom.dta.nc  gr_windx.mom.dta.nc
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/windy.mom.dta.nc  gr_windy.mom.dta.nc
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/tair.mom.dta.nc   gr_tair.mom.dta.nc
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/pair.mom.dta.nc   gr_pair.mom.dta.nc
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/tdew.mom.dta.nc   gr_tdew.mom.dta.nc
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/prec.mom.dta.nc   gr_prec.mom.dta.nc
ncks -O -d lon,4.0,15.0 -d lat,51.0,59.0 /Reanalysis/reanalysis/SN_REMO/raw/2004/clour.mom.dta.nc  gr_clour.mom.dta.nc


ncks -O -v pair gr_pair.mom.dta.nc    gr_mom.dta.nc
ncks -A -v clour gr_clour.mom.dta.nc  gr_mom.dta.nc
ncks -A -v tair gr_tair.mom.dta.nc    gr_mom.dta.nc
ncks -A -v tdew gr_tdew.mom.dta.nc    gr_mom.dta.nc
ncks -A -v windx gr_windx.mom.dta.nc  gr_mom.dta.nc
ncks -A -v windy gr_windy.mom.dta.nc  gr_mom.dta.nc
ncks -A -v prec gr_prec.mom.dta.nc    gr_mom.dta.nc

ncrename   -v pair,slp -v tair,t2 -v tdew,dew2 -v windx,u10 -v windy,v10 -v clour,tcc  -v prec,precip  gr_mom.dta.nc
ncap -O -s slp=slp*100.   -s dew2=dew2+273.15   -s t2=t2+273.15   gr_mom.dta.nc gr_mom.dta2004_fin.nc
