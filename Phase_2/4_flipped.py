import cv2

image = cv2.imread(r"Images\small_bird.jpg")


if image is None:
    print("Image Not Loaded")

else:
    flipped_vertical = cv2.flip(image, 0)
    flipped_horizontal = cv2.flip(image, 1)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original Image:", image)
    cv2.imshow("Horizontal Image", flipped_horizontal)
    cv2.imshow("Vertical Image:", flipped_vertical)
    cv2.imshow("Flipped Both:", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
