import cv2

image = cv2.imread(r"Images\flower.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresholded_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Edges", thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()