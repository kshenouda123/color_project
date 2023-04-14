import cv2
import numpy as np

# Load image
img = cv2.imread('/home/nvidia/project/term-bg-1-3d6355ab.jpeg')

# Resize image to reduce processing time
img = cv2.resize(img, (640, 480))

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range of colors to detect (here, we detect red)
lower_range = np.array([0, 50, 50])
upper_range = np.array([10, 255, 255])

# Threshold the HSV image to get only desired colors
mask = cv2.inRange(hsv, lower_range, upper_range)

# Get the percentage of red pixels in the image
total_pixels = mask.size
red_pixels = cv2.countNonZero(mask)
red_percentage = (red_pixels / total_pixels) * 100

# Print the dominant color based on threshold
if red_percentage > 5:
    print("The dominant color in the image is red.")
else:
    print("The dominant color in the image is not red.")

