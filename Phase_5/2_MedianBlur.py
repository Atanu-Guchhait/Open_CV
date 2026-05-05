import cv2

image = cv2.imread(r"Images\Noisy.jpg")
median_blurred_image = cv2.medianBlur(image, 11)

cv2.imshow("Original Image", image)
cv2.imshow("Median Blurred Image", median_blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()