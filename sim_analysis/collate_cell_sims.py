
import numpy as np
import os

N = 21

basefolder = "/data/Dropbox/python_libraries/atria_unloading/SS"
cell_sim_folders = ['converted_COURTEMANCHE/','ToRORd_dynCl/','ToRORd_dynCl_rv/']
cell_sims = ['converted_COURTEMANCHE_LandHumanStress','ToRORd_dynCl_LandHumanStress','ToRORd_dynCl_rv_LandHumanStress']
start_sample = 0
last_sample = N-1

def collate_cell_sims(basefolder,
								cell_sim_folders,
								cell_sims,
								start_sample,
								last_sample):


	os.system("mkdir "+basefolder+"/states/")

	for i in range(start_sample,last_sample+1):	

		os.system("cp "+basefolder+"/"+cell_sim_folders[0]+"/"+str(i)+"/"+str(i)+"_"+cell_sims[0]+".sv "+basefolder+"/states/")
		os.system("cp "+basefolder+"/"+cell_sim_folders[1]+"/"+str(i)+"/"+str(i)+"_"+cell_sims[1]+".sv "+basefolder+"/states/")
		os.system("cp "+basefolder+"/"+cell_sim_folders[2]+"/"+str(i)+"/"+str(i)+"_"+cell_sims[2]+".sv "+basefolder+"/states/")


collate_cell_sims(basefolder,
						cell_sim_folders,
						cell_sims,
						start_sample,
						last_sample)