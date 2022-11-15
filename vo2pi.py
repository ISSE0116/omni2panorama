import convert as co
import os
import sys
import cv2

input_file = sys.argv[1]
input_path = os.path.join('./input', input_file)
cpf = int(sys.argv[2])

co.cropimage.save_frames(input_path,'cropped_image', 'img', cpf)

co.worldpolar.o2e('cropped_image')
