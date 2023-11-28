import os
import subprocess
import sys
import json
import string
import glob
import pydicom as dicom
import numpy as np

print(np.__file__)

imaging_data = '/data/Dropbox/clinical_images_and_data/imaging_data/'

list_of_folders = sorted(filter(os.path.isdir, glob.glob(imaging_data + '*') ) )

for patient in list_of_folders:

	contents = os.path.join(patient, '*')

	lowest_folder_found = 0


	for candidate in glob.glob(contents):
	    if os.path.isdir(candidate):
	    	contents = candidate
	    else:
	    	image = candidate

	contents = os.path.join(contents, '*')

	for candidate in glob.glob(contents):
	    if os.path.isdir(candidate):
	    	contents = candidate
	    else:
	    	image = candidate

	contents = os.path.join(contents, '*')

	for candidate in glob.glob(contents):
	    if os.path.isdir(candidate):
	    	contents = candidate
	    else:
	    	image = candidate

	contents = os.path.join(contents, '*')

	for candidate in glob.glob(contents):
	    if os.path.isdir(candidate):
	    	contents = candidate
	    else:
	    	image = candidate

	contents = os.path.join(contents, '*')

	for candidate in glob.glob(contents):
	    if os.path.isdir(candidate):
	    	contents = candidate
	    else:
	    	image = candidate

	print(image)
	ds = dicom.dcmread(image)
	sex = np.array(ds[0x0010, 0x0040].value,dtype=str)
	print(sex)
	age = np.array(ds[0x0010, 0x1010].value,dtype=str)
	print(age)


# seg_array, header = nrrd.read(seg_nrrd)
# imgSpa = header['spacings']
# print(imgSpa)