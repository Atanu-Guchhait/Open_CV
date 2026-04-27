import cv2

image = cv2.imread(r"Images\small_bird.jpg")


if image is None:
    print("Image Not Loaded")

else:
    cropped = image[200:400, 350:500]

    cv2.imshow("Original Image:", image)
    cv2.imshow("Cropped Image:", cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()