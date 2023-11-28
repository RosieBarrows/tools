
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='To run: python check_unloading.py [first_sim] [last_sim]')
parser.add_argument("first_sim")
parser.add_argument("last_sim")
args = parser.parse_args()

original_mesh = "/data/Dropbox/af_hearts/02-henry/sims_folder/myocardium_AV_FEC_BB_lvrv"
basefolder = "/data/Dropbox/rosie_gsa/attempt2/unloading/output/"
chambers = ['lv_endo','rv_endo','la_endo','ra_endo']
start_sample = int(args.first_sim)
last_sample = int(args.last_sim)
output_file = basefolder+"unloaded_volumes.txt"
success_file = basefolder+"unloaded_successfully.txt"


def check_fourchamber_unloading(basefolder,
								chambers,
								start_sample,
								last_sample,
								output_file,
								original_mesh):

	vol_unloaded = np.zeros((last_sample-start_sample+1,len(chambers)),dtype=float)
	count = 0

	success_list = []

	os.system("mkdir "+basefolder+"/unloaded/")

	for i in range(start_sample,last_sample+1):	

		output, sim_failure = check_fourchamber_unloading_(basefolder+'/unloading_'+str(i)+'/',
											  chambers)

		if output[0]:
			print('unloading_'+str(i)+' successful...')
			success_list.append('unloading_'+str(i))

			for j in range(len(chambers)):
				vol_unloaded[count,j] = output[1+j]

			os.system("cp "+basefolder+"unloading_"+str(i)+"/cur_reference.pts "+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+".pts")
			os.system("cp "+original_mesh+".elem "+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+".elem")
			os.system("cp "+original_mesh+".lon "+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+".lon")
			os.system("cp "+original_mesh+".elem "+basefolder+"/unloading_"+str(i)+"/cur_reference.elem")
			os.system("cp "+original_mesh+".lon "+basefolder+"/unloading_"+str(i)+"/cur_reference.lon")

			os.system("meshtool convert -imsh="+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+" -omsh="+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+" -ofmt=carp_bin")
			os.system("meshtool convert -imsh="+basefolder+"/unloading_"+str(i)+"/cur_reference -omsh="+basefolder+"/unloading_"+str(i)+"/cur_reference -ofmt=carp_bin")


			os.system("cp "+basefolder+"unloading_"+str(i)+"/cur_reference.pts "+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+".pts")
			os.system("cp "+original_mesh+".elem "+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+".elem")
			os.system("cp "+original_mesh+".lon "+basefolder+"/unloaded/myocardium_AV_FEC_BB_lvrv_unloaded_"+str(i)+".lon")

	# 	elif sim_failure == 1:
	# 		print('unloading_'+str(i)+' failed by new error...')

	# 	else:
	# 		print('unloading_'+str(i)+' crashed...')

	# 	count += 1

	# np.savetxt(output_file,vol_unloaded,fmt="%g")

	# with open(basefolder+"unloaded_successfully.txt", 'w') as fp:
	# 	for sim in success_list:
	# 		fp.write("%s\n" % sim)
	# print('Saved success list')


def check_fourchamber_unloading_(simulation_folder,
								 chambers):
	sim_failure = 0

	converged_1 = False
	with open(simulation_folder+"unloading.log", 'r') as file:
		content = file.read()
		if "--- CONVERGED ---" in content:
			converged_1 = True

	converged_2 = False
	if not os.path.exists(simulation_folder+"temp/"):
		converged_2 = True

	converged = False
	if converged_1 and converged_2:
		converged = True

	output = [converged]
	for ch in chambers:
		if os.path.exists(simulation_folder+"current_data/"):
			if not os.path.exists(simulation_folder+"current_data/"+ch+".vol.dat"):
				raise Exception('Cannot find volume file '+simulation_folder+"current_data/"+ch+".vol.dat")
		else:
			sim_failure = 1

		if converged:
			vol = np.loadtxt(simulation_folder+"current_data/"+ch+".vol.dat",dtype=float,usecols=[1])
			output.append(vol[0])
		else:
			output.append(-1)


	return output, sim_failure

check_fourchamber_unloading(basefolder,chambers,start_sample,last_sample,output_file,original_mesh)


