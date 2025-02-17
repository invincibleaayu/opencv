from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np
#fetching the argument and saving it in dictionary
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required= True , help="Enter path to image")
args = vars(ap.parse_args())
#load and showing the image into numpy array
#printing th required data
image=cv2.imread(args["image"])
blurred=np.hstack([
    cv2.blur(image,(3,3)),
    cv2.blur(image,(5,5)),
    cv2.blur(image,(7,7))])
cv2.imshow("averaged blurred",blurred)
cv2.waitKey(0)
blurred=np.hstack([
    cv2.bilateralFilter(image,(3),21,21),
    cv2.bilateralFilter(image,(5),31,31),
    cv2.bilateralFilter(image,(7),41,41)])
cv2.imshow("bilateral blurred",blurred)
cv2.waitKey(0)
blurred=np.hstack([
    cv2.GaussianBlur(image,(3,3),0),
    cv2.GaussianBlur(image,(5,5),0),
    cv2.GaussianBlur(image,(7,7),0)])
cv2.imshow("gussian blurred",blurred)
cv2.waitKey(0)
blurred=np.hstack([
    cv2.medianBlur(image,3),
    cv2.medianBlur(image,5),
    cv2.medianBlur(image,7)])
cv2.imshow("median blurred",blurred)
cv2.waitKey(0)


    