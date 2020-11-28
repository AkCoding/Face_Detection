# import OpenCV
import cv2

# Load trained cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read image file
color_image = cv2.imread('Mypic.jpg')

# Convert color image into grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)