import pathlib

file_path = '../cropped_image'

image_list = list(pathlib.Path(file_path).glob('*.png'))

for i in range(len(image_list)):
	print(image_list)
