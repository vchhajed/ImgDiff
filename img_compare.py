import cv2
import numpy as np

image1 = cv2.imread("download.jpg")

image2 = cv2.imread("download1.jpg")

#print(image1)

difference = cv2.subtract(image1, image2)
#print(difference)

#difference is FALSE means original
result = not np.any(difference)

if result:
	print("The images are same")

else:
	cv2.imwrite("result.jpeg", difference)
	print("The images are different")