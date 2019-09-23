import os
import cv2
import numpy as np

path = './r/'
path = '/home/dabai/Downloads/MOT16/test/MOT16-01/img1/'
filelist = os.listdir(path)



size = (573,269)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter('output.MP4',fourcc, 10.0, (573,269))
#fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')#cv2.VideoWriter_fourcc('I', '4', '2', '0')
out = cv2.VideoWriter("./VideoTest1.avi", fourcc, 10, size)


for item in filelist:
    if item.endswith('.jpg'): 
        item = path + item
        img = cv2.imread(item)
        out.write(img)
out.release()
cv2.destroyAllWindows()
