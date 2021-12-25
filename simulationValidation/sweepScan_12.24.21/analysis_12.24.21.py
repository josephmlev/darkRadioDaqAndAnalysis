#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:00:34 2021

@author: dark-radio
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from scipy.interpolate import interp1d

#52cd dipole 60N 60W 57V

freqArr = np.arange(50,300,0.1)


dip52CmFreq = pd.read_pickle('./52cmDip_pwr_n34dBm_60N_60W_57V.pkl').index.values
dip52CmPower = pd.read_pickle('./52cmDip_pwr_n34dBm_60N_60W_57V.pkl')['Power (dBm)'].to_numpy()
dip52CmInterp = interp1d(dip52CmFreq, dip52CmPower)

fGenCalFreq = pd.read_pickle('./fGenCalHiRes.pkl').index.values
fGenCalPower = pd.read_pickle('./fGenCalHiRes.pkl')['Power (dBm)'].to_numpy()
fGenCalInterp = interp1d(fGenCalFreq, fGenCalPower)

vswrfreq, vswr= np.loadtxt('52cmDip_vswr_60N_60W_57V.txt', delimiter = ',', unpack = True)
vswrInterp = interp1d(vswrfreq,vswr)

df_52cmDip_60N_60W_57V = pd.DataFrame()

df_52cmDip_60N_60W_57V['Frequency (MHz)'] = freqArr
df_52cmDip_60N_60W_57V['Dipole 52 CM Power (dBm)'] = dip52CmInterp(freqArr)
df_52cmDip_60N_60W_57V['VSWR'] = vswrInterp(freqArr)
df_52cmDip_60N_60W_57V['F. Gen Output (dBm)'] = fGenCalInterp(freqArr)
df_52cmDip_60N_60W_57V['Reflection Coefficient'] = (df_52cmDip_60N_60W_57V['VSWR'] - 1) /(df_52cmDip_60N_60W_57V['VSWR'] + 1)
df_52cmDip_60N_60W_57V['Return Loss (dB)'] = -10 * np.log10(df_52cmDip_60N_60W_57V['Reflection Coefficient'])
df_52cmDip_60N_60W_57V['Power to Antenna'] = df_52cmDip_60N_60W_57V['F. Gen Output (dBm)'] - df_52cmDip_60N_60W_57V['Return Loss (dB)']
df_52cmDip_60N_60W_57V['Normilized Dipole Power (dBm)'] = df_52cmDip_60N_60W_57V['Dipole 52 CM Power (dBm)'] -2 df_52cmDip_60N_60W_57V['Power to Antenna']




