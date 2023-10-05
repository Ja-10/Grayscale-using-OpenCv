import cv2
#load input image
image = cv2.imread('/Users/joshna/Documents/image.jpeg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
#convert input image to grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Resultant Image', gray_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()
