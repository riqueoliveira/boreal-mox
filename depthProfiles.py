# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%% importing and merging depth profiles with 13C data depth profiles

import pandas as pd

path_dir = r'C:\Users\henol98\OneDrive - Linköpings universitet\manuscripts\Boreal lakes Mox\metlake_database\METLAKE_DepthProfiles_2018-2020.xlsx'

depthProfiles = pd.read_excel(path_dir, header=1, skiprows=[2],index_col='Date')

list(depthProfiles.columns)


dp = depthProfiles[['Region',
 'Lake',
 'Depth1',
 'Depth',
 'PAR',
 'WaterTemperature',
 'DissolvedOxygen',
 'DissolvedOxygen.1',
 'pH',
 'Conductivity',
 'Temperature13CSample',
 'Temp',
 'Baro',
 'Depth.1',
 'pH.1',
 'pHmV',
 'ORP',
 'DO',
 'DO.1',
 'EC',
 'CH4aq',
 'CO2aq',
 'N2Oaq']]

type(dp.index)  # check index format
dp.index =  pd.to_datetime(dp.index, format='%Y%m%d') # change index format
dp.sort_index()



path_dir2 = r'C:\Users\henol98\OneDrive - Linköpings universitet\manuscripts\Boreal lakes Mox\metlake13Cdatabase_R_210618.xlsx'

d13CResults = pd.read_excel(path_dir2,header=0,index_col='Date')

metlake13C = d13CResults[d13CResults["Project"] == "METLAKE"] 

depthProfile13C = metlake13C[metlake13C["type"] == "depth_profile"]

list(depthProfile13C.columns)

dp13C = depthProfile13C[["Depth",
                         "Lake",
                         "Water_temp_headspace", 
                         "LakeID","CH4_final_ppm",
                         "d13CH4_‰","CO2_final_ppm",
                         "d13CO2_‰"]]


type(dp13C.index)  # check index format
dp13C.index =  pd.to_datetime(dp13C.index, format='%Y%m%d') # change index format
dp13C.sort_index()

type(dp13C.index) # re-check index format


dpAll = dp.merge(dp13C, on=['Date', 'Lake','Depth'], how='outer')



#%% Data manipulation and exploring plots


import matplotlib.pyplot as plt
import numpy as np

list(dpAll.columns)

dpAll['Lake'].unique()  # to check the existing Lakes in the df
dpAll['Lake'].unique().tolist() # another way to check the existing Lakes in the df


dpNAS = dpAll[dpAll['Lake'] == 'Nastjarn'] #subset only one lake

dpNAS[['Depth']].describe()  # statistical summary of a specific numeric variable





dpNAS.WaterTemperature.plot()
plt.gca().invert_yaxis()




