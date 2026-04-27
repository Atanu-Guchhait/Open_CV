import cv2

image = cv2.imread(r"Images\small_bird.jpg")


if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray image showing", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Not Loaded")    