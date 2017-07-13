#!/bin/bash

module load intel
module load netcdf
module load nco

cp -fv ww3.Constant.20151214_sxy_ike_date.nc  wind_atm.nc

ncrename   -v sxx,uwnd   -v syy,vwnd  -v sxy,P    wind_atm.nc
ncap -O -s uwnd=uwnd*0.+8.0  -s vwnd=vwnd*0.-8  -s P=P*0.+100000  wind_atm.nc  wind_atm_fin.nc

ncatted -a _FillValue,uwnd,m,f,0   wind_atm_fin.nc
ncatted -a _FillValue,vwnd,m,f,0   wind_atm_fin.nc
ncatted -a _FillValue,P,m,f,1e5    wind_atm_fin.nc

# ncks -O -v sxx   ww3.Constant.201512_14_15_sxy.nc  wind_atm.nc
# ncks -A -v syy   ww3.Constant.201512_14_15_sxy.nc  wind_atm.nc
# ncks -A -v sxy   ww3.Constant.201512_14_15_sxy.nc  wind_atm.nc


