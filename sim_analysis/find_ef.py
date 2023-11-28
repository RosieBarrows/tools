import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import sys
import scipy.spatial as sp
import copy
import csv
import argparse

# !! CHECK NUM BEATS AND LOADSTEPPING ARE AS EXPECTED !!
num_beats = 5
loadStepping = 40

from sim_utils import *
parser = argparse.ArgumentParser(description='To run: python3 find_ef.py [path_to_cycle_folder] [BCL] [AV_delay]')
parser.add_argument("path_to_cycle_folder")
parser.add_argument("BCL")
parser.add_argument("AV_delay", default=100)
args = parser.parse_args()
cycleFolder = args.path_to_cycle_folder
BCL = args.BCL
AV_delay = args.AV_delay

LV_pres_full,RV_pres_full,LA_pres_full,RA_pres_full = prepare_pres_data(cycleFolder)
LV_vol_full,RV_vol_full,LA_vol_full,RA_vol_full = prepare_vol_data(cycleFolder)

LV_vol = last_full_beat(LV_vol_full,BCL,AV_delay,num_beats,loadStepping)
RV_vol = last_full_beat(RV_vol_full,BCL,AV_delay,num_beats,loadStepping)
LA_vol = last_full_beat(LA_vol_full,BCL,AV_delay,num_beats,loadStepping)
RA_vol = last_full_beat(RA_vol_full,BCL,AV_delay,num_beats,loadStepping)

time = np.arange(0,len(LV_vol),1)

EDVs = [max(LV_vol), max(RV_vol), max(LA_vol), max(RA_vol)]

ESVs = [min(LV_vol), min(RV_vol), min(LA_vol), min(RA_vol)]

LVEF = 100*((EDVs[0]-ESVs[0])/EDVs[0])
RVEF = 100*((EDVs[1]-ESVs[1])/EDVs[1])

LA_preAC_vol = LA_vol[0]
LA_postAC_vol = min(LA_vol)
LA_EV = LA_preAC_vol - LA_postAC_vol	# LA emptying volume

RA_preAC_vol = RA_vol[0]
RA_postAC_vol = min(RA_vol)
RA_EV = RA_preAC_vol - RA_postAC_vol	# RA emptying volume

LAEF = 100*(LA_EV/LA_preAC_vol)
RAEF = 100*(RA_EV/RA_preAC_vol)

# plt.plot(time,RA_vol)
# plt.plot(time[0],RA_preAC_vol,'*')
# plt.plot(time[np.argmin(RA_vol)],RA_postAC_vol,'*')
# plt.show()

print("\n EDVs: \n \t LV = "+str(EDVs[0])+" ml \n \t RV = "+str(EDVs[1])+" ml \n \t LA = "+str(EDVs[2])+" ml \n \t RA = "+str(EDVs[3])+" ml \n")

print("\n ESVs: \n \t LV = "+str(ESVs[0])+" ml \n \t RV = "+str(ESVs[1])+" ml \n \t LA = "+str(ESVs[2])+" ml \n \t RA = "+str(ESVs[3])+" ml \n")

print("\n Stroke volume: \n \t LV = "+str(EDVs[0]-ESVs[0])+" ml \n")

print("\n LV ejection fraction: \n \t "+str(LVEF)+" % \n")

print("\n RV ejection fraction: \n \t "+str(RVEF)+" % \n")

print("\n LA ejection fraction: \n \t "+str(LAEF)+" % \n")

print("\n RA ejection fraction: \n \t "+str(RAEF)+" % \n")

LV_pres = last_full_beat(LV_pres_full,BCL,AV_delay,num_beats,loadStepping)

LV_max = max(LV_pres_full)

print("\n LV max pressure: \n \t "+str(LV_max)+" mmHg \n")


