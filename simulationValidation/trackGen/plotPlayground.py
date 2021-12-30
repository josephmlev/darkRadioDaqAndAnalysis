#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:02:58 2021

@author: joseph
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.close('all')

startFreq = 5 * 10**6 #Hz
stopFreq = 300 * 10**6 #Hz
nPoints = 10000 
freqArr = np.linspace(startFreq/1e6, stopFreq/1e6, nPoints)

df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4 = pd.read_pickle('30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4.pkl')

df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4 = pd.read_pickle('30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4.pkl')

df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2 = pd.read_pickle('30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2.pkl')

df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2 = pd.read_pickle('30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2.pkl')

df_30cmDipClip_allChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4 = pd.read_pickle('30cmDipClip_allChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4.pkl')

df_30cmDipBananna_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4 = pd.read_pickle('30cmDipBananna_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4.pkl')

df_30cmDipBananna_noChokes_60N60E57V_20dBattAtFeed_rbw10k_DANLn100pm3dB_avg4 = pd.read_pickle('30cmDipBananna_noChokes_60N60E57V_20dBattAtFeed_rbw10k_DANLn100pm3dB_avg4.pkl')



Raw_2chokesDiff_v2 = df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Raw Antenna Power (dBm)'] - df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)']

plt.figure()
plt.title('No chokes Raw power v1 - v2')
plt.plot(freqArr, Raw_2chokesDiff_v2)

plt.figure()
plt.title('2 chokes Raw power v1 vs v2')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'], 'r')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Raw Antenna Power (dBm)'])




Raw_noChokesDiff_v2 = df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'] - df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Raw Antenna Power (dBm)']

plt.figure()
plt.title('No chokes Raw power v1 - v2')
plt.plot(freqArr, Raw_noChokesDiff_v2)

plt.figure()
plt.title('No chokes Raw power v1 vs v2')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Raw Antenna Power (dBm)'], 'r')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'])

plt.figure()
plt.title('No chokes Matching Loss v1 vs v2')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Matching Loss'], 'r')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Matching Loss'])

plt.figure()
plt.title('No chokes NOrmilized power v1 vs v2')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Normilized Antenna Power (dBm)'], 'r')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'])

plt.figure()
plt.title('2 chokes N0rmilized power v1 vs v2')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4_v2['Normilized Antenna Power (dBm)'], 'r')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'])

plt.figure()
plt.title('No chokes vs 2 vs All,  N0rmilized power')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = 'none')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = '2')
plt.plot(freqArr, df_30cmDipClip_allChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = 'all')
plt.legend()


plt.figure()
plt.title('No chokes vs 2 vs All, raw power')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'], label = 'none')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'], label = '2')
plt.plot(freqArr, df_30cmDipClip_allChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'], label = 'all')
plt.legend()

plt.figure()
plt.title('No chokes vs 2 vs All, Mismatch Loss')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Matching Loss'], label = 'none')
plt.plot(freqArr, df_30cmDipClip_2chokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Matching Loss'], label = '2')
plt.plot(freqArr, df_30cmDipClip_allChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Matching Loss'], label = 'all')
plt.legend()


plt.figure()
plt.title('Raw power, bananna attenuator at feed vs on spec analizer')
plt.plot(freqArr, df_30cmDipBananna_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'], label = 'spec')
plt.plot(freqArr, df_30cmDipBananna_noChokes_60N60E57V_20dBattAtFeed_rbw10k_DANLn100pm3dB_avg4['Raw Antenna Power (dBm)'], label = 'at feed')
plt.legend()


plt.figure()
plt.title('Raw power, bananna attenuator at feed vs on spec analizer')
plt.plot(freqArr, df_30cmDipBananna_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = 'spec')
plt.plot(freqArr, df_30cmDipBananna_noChokes_60N60E57V_20dBattAtFeed_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = 'at feed')
plt.legend()


plt.figure()
plt.title('Normilized power, bananna vs clip no choke not att.')
plt.plot(freqArr, df_30cmDipClip_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = 'clip')
plt.plot(freqArr, df_30cmDipBananna_noChokes_60N60E57V_20dBatt_rbw10k_DANLn100pm3dB_avg4['Normilized Antenna Power (dBm)'], label = 'bananna')
plt.legend()

























































