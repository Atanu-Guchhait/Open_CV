import cv2

image = cv2.imread(r"Images\white_cloud.jpg")

if image is None:
    print("Image Not Loaded")
else:
    pt1 = (50,50)
    pt2 = (300,300)
    color = (0, 0, 255)
    thickness = 4

    rectangle_image = cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangle Image:", rectangle_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()    