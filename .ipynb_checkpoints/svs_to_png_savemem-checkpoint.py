import os
import glob
import numpy as np
import openslide
import cv2
import json

def ToPNG(case_name, IMG, Json_dir, output_folder):
	"""
	Converts a large SVS file into a single PNG, downsampled for efficiency.

	Parameters:
		- case_name (str): Name of the case (used in filenames)
		- IMG (str): Path to the SVS file
		- output_folder (str): Where to save the PNGs
	"""
	output_dir = output_folder
	os.makedirs(output_dir, exist_ok=True)

	X20_folder = os.path.join(output_folder, '20X')
	img_20X_path = os.path.join(X20_folder, f"image_{case_name}.png")

	if os.path.exists(img_20X_path):
		return

	try:
		# Open the whole-slide image using OpenSlide
		svs = openslide.OpenSlide(IMG)
	except:
		print('error for loading')
		return

	# Get the original dimensions of the SVS file
	x_length, y_length = svs.dimensions


	now_json = os.path.join(Json_dir, os.path.basename(IMG).replace('.svs','.svs.geojson'))

	with open(now_json, 'r') as f:
		annotation_QA = json.load(f)

	mask_labels = ['sample1','sample2']
	annotations_by_object = {}
	for obj in mask_labels:
		# Get list of contours for the current object type
		contours_obj = []
		for feat in annotation_QA["features"]:
			# try:
			# 	print(feat["properties"]["classification"]["name"])
			# except:
			# 	print('wrong')
			try:
				if feat["properties"]["classification"]["name"] == obj:
					contours_obj.append((feat["geometry"]["coordinates"][0]))
			except:
				print('wrong objects')

			# contours_obj = [
			# 	feat["geometry"]["coordinates"][0]
			# 	for feat in annotation_QA["features"]
			# 	if feat["properties"]["classification"]["name"] == obj
			# ]

		transformed_contours = []
		for contours in contours_obj:  ##### need to check the affine registration code
			for contour in contours:
				pts = np.array(contour)
				transformed_contours.append(pts)

		annotations_by_object[obj] = transformed_contours

	# Define output folders for different magnifications
	X20_folder = os.path.join(output_folder, case_name)

	os.makedirs(X20_folder, exist_ok=True)

	mag = svs.properties['aperio.AppMag']

	if mag == '40':
		lv = 1
		down = 2
	elif mag == '20':
		lv = 0
		down = 1

	# Convert your contour points to a numpy array
	contour = np.array(annotations_by_object['sample1'])

	# Optionally, reshape if needed:
	# This is useful if your points are in shape (N, 2) but OpenCV expects (N, 1, 2)
	if contour.ndim == 2 and contour.shape[1] == 2:
		contour = contour.reshape((-1, 1, 2))
	x, y, w, h = cv2.boundingRect(contour)

	img_5X_sample1 = np.array(svs.read_region((x,y), lv, (int(w/down),int(h/down))))
	img_5X_path = os.path.join(X20_folder, f"{case_name}_0.png")
	cv2.imwrite(img_5X_path, cv2.cvtColor(img_5X_sample1, cv2.COLOR_RGB2BGR))

	del img_5X_sample1

	# Convert your contour points to a numpy array
	contour = np.array(annotations_by_object['sample2'])

	# Optionally, reshape if needed:
	# This is useful if your points are in shape (N, 2) but OpenCV expects (N, 1, 2)
	if contour.ndim == 2 and contour.shape[1] == 2:
		contour = contour.reshape((-1, 1, 2))
	x, y, w, h = cv2.boundingRect(contour)

	img_5X_sample2 = np.array(svs.read_region((x,y), lv,(int(w/down),int(h/down))))
	img_5X_path = os.path.join(X20_folder, f"{case_name}_1.png")
	cv2.imwrite(img_5X_path, cv2.cvtColor(img_5X_sample2, cv2.COLOR_RGB2BGR))

	# Free memory
	del img_5X_sample2
	svs.close()


if __name__ == "__main__":
	svs_dir = '/Data4/Glo_Volume/WSI/HTN'
	# Json_dir = '/Data4/Glo_Volume/WSI/HTN/HTN_capsule/geojson'
	output_dir = '/Data4/Glo_Volume/WSI_png/HTN'

	svs_list = glob.glob(os.path.join(svs_dir, '*.svs'))

	for svs in svs_list:
		name = os.path.basename(svs)
		if not name.endswith('.svs'):
			continue

		case_name = name.split('.svs')[0]
		print(f"Processing: {case_name}")

		ToPNG(case_name, svs, Json_dir, output_dir)