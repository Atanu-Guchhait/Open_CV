import cv2

image = cv2.imread(r"Images\Blue_rectangle.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thres = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:

  
    if cv2.contourArea(contour) < 100:
        continue

    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        shape_name = "Rectangle"

    elif corners == 5:
        shape_name = "Pentagon"

    else:
        shape_name = "Circle/Unknown"

    cv2.drawContours(image, [approx], 0, (0,255,0), 2)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    cv2.putText(image, shape_name, (x, y),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()