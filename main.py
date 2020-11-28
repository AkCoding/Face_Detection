# import OpenCV
import cv2

# Load trained cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read image file
color_image = cv2.imread('Mypic.jpg')


