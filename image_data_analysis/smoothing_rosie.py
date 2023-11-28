# Smoothing algorithm

# First try on a small, single label mesh in 2D

import numpy as np
import copy
import nrrd
import json
import matplotlib.pyplot as plt
from smoothing_utils import *
from img import *

resolution_multiplier = 4
kernel_order = 7

image_folder = "./"
path2image = image_folder+"/seg_final.nrrd"

origin_spacing_file = open(image_folder+'/origin_spacing.json')
origin_spacing_data = json.load(origin_spacing_file)
origin = origin_spacing_data['origin']
spacings = origin_spacing_data['spacing']

S = []
for s in spacings:
	S.append(float(s)/float(resolution_multiplier))

image, header = nrrd.read(path2image)



# image = np.array([[0, 0, 0, 1, 1, 2],
# 		 		  [0, 0, 1, 1, 2, 2],
# 		 	 	  [0, 1, 1, 2, 2, 2],
# 		 	 	  [1, 1, 2, 2, 2, 2],
# 		 	 	  [1, 2, 2, 2, 2, 2]])


# image = np.array([[[0, 0, 0, 1, 1, 2],
# 		 		   [0, 0, 1, 1, 2, 2],
# 		 	 	   [0, 1, 1, 2, 2, 2],
# 		 	 	   [1, 1, 2, 2, 2, 2],
# 		 	 	   [1, 2, 2, 2, 2, 2]],
# 		 	 	   [[0, 0, 1, 1, 1, 2],
# 		 		   [0, 1, 1, 1, 2, 2],
# 		 	 	   [1, 1, 1, 2, 2, 2],
# 		 	 	   [1, 1, 2, 2, 2, 1],
# 		 	 	   [1, 2, 2, 2, 1, 1]],
# 		 	 	   [[1, 1, 1, 1, 1, 2],
# 		 		   [1, 1, 1, 1, 2, 2],
# 		 	 	   [1, 1, 1, 2, 2, 1],
# 		 	 	   [1, 1, 2, 2, 1, 1],
# 		 	 	   [1, 2, 2, 1, 1, 1]]])

image_original = copy.deepcopy(image)

image_resampled = resample_image_3D(image,resolution_multiplier)

image_smooth = smooth_image_3D(image_resampled,kernel_order)


# height = np.shape(image_smooth)[0]


# for p in range(height):
# 	plt.subplot(2,int(0.5*height),p+1)
# 	plt.imshow(image_smooth[p])

# plt.show()

# ----------------------------------------------------------------------------------------------
# Format and save the segmentation
# ----------------------------------------------------------------------------------------------
image_array = np.swapaxes(image_smooth,0,2)
save_itk(image_array, origin, S, image_folder+'/seg_final_smooth.nrrd')
print(" ## Done! ## \n")





