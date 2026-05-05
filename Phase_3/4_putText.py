import cv2

image = cv2.imread(r"Images\white_cloud.jpg")


if image is None:
    print("Image Not Loaded")
else:

    text_image = cv2.putText(image, "Welcome to CodelogicX", (50,100),
                             cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255),2)

    cv2.imshow("Text Image: ", text_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()