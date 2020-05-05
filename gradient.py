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
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
lap=cv2.Laplacian(image,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("laplacian detection",lap)
sobelx=cv2.Sobel(image,cv2.CV_64F,1,0)
sobely=cv2.Sobel(image,cv2.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
combined=cv2.bitwise_or(sobelx,sobely)
cv2.imshow("sobelx detection",sobelx)
cv2.imshow("sobely detection",sobely)
cv2.imshow("combined detection",combined)
cv2.waitKey(0)
