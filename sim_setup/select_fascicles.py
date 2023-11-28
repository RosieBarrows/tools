import os
import sys
import json
from SIMULATION_library.electrode_utils import *
from SIMULATION_library.file_utils import *

heart_folder = "/data/Dropbox/af_hearts/02-henry/"

f = open("./fascicles_settings.json","r")
fascicles_settings = json.load(f)
f.close()
electrodes_folder = "./electrodes"
os.system("mkdir "+electrodes_folder)
os.system("mkdir "+electrodes_folder+"/tmp/")

combine_uvc(heart_folder+"/surfaces_uvc/BiV/uvc/BiV.uvc_z.dat",
				heart_folder+"/surfaces_uvc/BiV/uvc/BiV.uvc_rho.dat",
				heart_folder+"/surfaces_uvc/BiV/uvc/BiV.uvc_phi.dat",
				heart_folder+"/surfaces_uvc/BiV/uvc/BiV.uvc_ven.dat",
				heart_folder+"/surfaces_uvc/BiV/uvc/COMBINED_COORDS_Z_RHO_PHI_V.dat")

define_fascicles(heart_folder+"/surfaces_uvc/BiV/BiV.nod",
				 heart_folder+"/surfaces_uvc/BiV/uvc/COMBINED_COORDS_Z_RHO_PHI_V.dat",
				 heart_folder+"/surfaces_uvc/myocardium_bayer_60_-60.pts",
				 fascicles_settings,
				 electrodes_folder+"/tmp/")
print('===============================================')
print('Converting vtx to pts using non-refined mesh...')
print('===============================================')
for f in fascicles_settings:
	vtx2pts_electrodes(electrodes_folder+"/tmp/"+f,heart_folder+"/surfaces_uvc/myocardium_bayer_60_-60.pts")
# print('===============================================')
# print('Mapping electrodes to refined mesh...')
# print('===============================================')
# for f in fascicles_settings:
# 	map_electrodes(electrodes_folder+"/tmp/"+f+".vtx",
# 				   "./UVCs/case19_original.pts",
# 				   "./UVCs/case19_original_refined.pts",
# 				   electrodes_folder+"/"+f+".vtx")
# 	vtx2pts(electrodes_folder+"/"+f+".vtx","./UVCs/case19_original_refined.pts")
print('===============================================')
print('Combining LV electrode in one vtx...')
print('===============================================')
combine_electrode([electrodes_folder+"/tmp/LVant.vtx",electrodes_folder+"/tmp/LVpost.vtx",electrodes_folder+"/tmp/LVsept.vtx"],
				   electrodes_folder+"/fascicles_lv.vtx")
print('===============================================')
print('Combining RV electrode in one vtx...')
print('===============================================')
combine_electrode([electrodes_folder+"/tmp/RVsept.vtx",electrodes_folder+"/tmp/RVmod.vtx"],
				   electrodes_folder+"/fascicles_rv.vtx")

print('===============================================')
print('Writing pts file for visualisation in paraview')
print('===============================================')
vtx2pts_electrodes(electrodes_folder+"/fascicles_lv",heart_folder+"/surfaces_uvc/myocardium_bayer_60_-60.pts")
vtx2pts_electrodes(electrodes_folder+"/fascicles_rv",heart_folder+"/surfaces_uvc/myocardium_bayer_60_-60.pts")