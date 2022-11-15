import cv2
import os
import sys

def save_frames(video_path, dir_path, basename, cpf, ext='png'):
    count=0
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            if(count%cpf==0):
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
                n += 1
        else:
            return
        count = count+1
