import cv2
import os
import sys
import pathlib

def o2e(file_path):
	i=0

	result_path = './o2e_result'

	image_list = list(pathlib.Path(file_path).glob('*.png'))

	radius = 1440
	center = (1440,1440)
	height, width = 700, 2048

	for i in range(len(image_list)):
		image = cv2.imread(str(image_list[i]))
		flags = cv2.INTER_CUBIC + cv2.WARP_FILL_OUTLIERS + cv2.WARP_POLAR_LINEAR

		result_image = cv2.warpPolar(image, (height, width), center, radius, flags)
		result_image2 = cv2.rotate(result_image, cv2.ROTATE_90_CLOCKWISE)
		output_path = result_path + '/' + image_list[i].name
		cv2.imwrite(output_path, result_image2)
