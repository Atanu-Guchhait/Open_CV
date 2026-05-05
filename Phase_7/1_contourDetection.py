import cv2

image = cv2.imread(r"Images\Blue_rectangle.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 6)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
