import cv2
import numpy as np
import time


def reshape_image_2d(img):
    img = img[0:1200, 300:1500] #h,w
    img = cv2.resize(img, dsize=(86, 86), interpolation=cv2.INTER_CUBIC)
    #img = img[0:1200, 372:1572]
    #img = cv2.resize(img, dsize=(486, 300), interpolation=cv2.INTER_CUBIC) #USE WITH CAUTION, may interferre with the pixel size


    return img

k = cv2.imread(r'/home/kukauser/Documents/test_22.04.22.png')
print(k.shape)
#cv2.imshow("original", k)
reshaped = reshape_image_2d(k)
print(k.shape)
done = cv2.imwrite(r'/home/kukauser/Documents/test_22.04.22_reshaped.png', reshaped)