import cv2

image = cv2.imread(r"Images\small_bird.jpg")


if image is None:
    print("Image Not Loaded")

else:
    w, h = image.shape[:2]

    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotate_image = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Original Image: ", image)
    cv2.imshow('Ratate Image: ', rotate_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
