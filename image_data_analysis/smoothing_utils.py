import numpy as np
import copy

def resample_image_2D(image,resolution_multiplier):

	rows = image.shape[0]
	cols = image.shape[1]

	resampled_image = np.zeros((resolution_multiplier*rows,resolution_multiplier*cols))
	resampled_rows = np.zeros((resolution_multiplier*rows,cols))

	R = 0		# row number of resampled image

	for r in range(rows):

		for m in range(resolution_multiplier):

			resampled_rows[R,:] = image[r,:]
			R += 1

	C = 0

	for c in range(cols):

		for m in range(resolution_multiplier):

			resampled_image[:,C] = resampled_rows[:,c]
			C += 1

	return resampled_image

def resample_image_3D(image,resolution_multiplier):

	x_rows = image.shape[0]
	y_rows = image.shape[1]
	z_rows = image.shape[2]

	resampled_image = np.zeros((resolution_multiplier*x_rows,resolution_multiplier*y_rows,resolution_multiplier*z_rows))
	resampled_x = np.zeros((resolution_multiplier*x_rows,y_rows,z_rows))
	resampled_x_y = np.zeros((resolution_multiplier*x_rows,resolution_multiplier*y_rows,z_rows))

	X = 0		# row number of resampled image

	for x in range(x_rows):

		for m in range(resolution_multiplier):

			resampled_x[X,:,:] = image[x,:,:]
			X += 1

	Y = 0

	for y in range(y_rows):

		for m in range(resolution_multiplier):

			resampled_x_y[:,Y,:] = resampled_x[:,y,:]
			Y += 1

	Z = 0

	for z in range(z_rows):

		for m in range(resolution_multiplier):

			resampled_image[:,:,Z] = resampled_x_y[:,:,z]
			Z += 1


	return resampled_image

def smooth_image_2D(image, k_order):
	k_centre = int((k_order-1)/2)

	rows = image.shape[0]
	cols = image.shape[1]

	image_smooth = copy.deepcopy(image)

	if (k_order % 2) == 0:
		k_acceptable = False
	else:
		k_acceptable = True

	if k_acceptable == True:	

		for r in range(rows-k_order):
			for c in range(cols-k_order):
				query = np.zeros((k_order,k_order))
				for i in range(k_order):
					for j in range(k_order):
						query[i][j] = image[r+i][c+j]
					
				query = query.flatten()
				query = query.astype(int)
				decision = np.bincount(query).argmax()

				image_smooth[r+k_centre][c+k_centre] = int(decision)

	else:
		print("\n ## Fuzz factor must be an odd number! ##\n")
		print("    Exiting program ...   \n")
		exit()

	return image_smooth

def smooth_image_3D(image, k_order):
	k_centre = int((k_order-1)/2)

	X = image.shape[0]
	Y = image.shape[1]
	Z = image.shape[2]

	image_smooth = copy.deepcopy(image)

	if (k_order % 2) == 0:
		k_acceptable = False
	else:
		k_acceptable = True

	if k_acceptable == True:	

		for x in range(X-k_order):
			print(str(100*x/X)+"percent done")
			for y in range(Y-k_order):
				for z in range(Z-k_order):
					query = np.zeros((k_order,k_order,k_order))
					for i in range(k_order):
						for j in range(k_order):
							for h in range(k_order):
								query[i][j][h] = image[x+i][y+j][z+h]

					query = query.flatten()
					query = query.astype(int)
					decision = np.bincount(query).argmax()

					image_smooth[x+k_centre][y+k_centre][z+k_centre] = int(decision)

	else:
		print("\n ## Fuzz factor must be an odd number! ##\n")
		print("    Exiting program ...   \n")
		exit()

	return image_smooth





