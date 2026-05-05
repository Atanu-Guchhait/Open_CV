import cv2

image = cv2.imread(r"Images\white_cloud.jpg")


if image is None:
    print("Image Not Loaded")
else:

    center = (200,200)
    radius = 100
    color = (0,0,255)
    thickness = -1

    cirlce_image = cv2.circle(image,center, radius, color, thickness)    
    cv2.imshow("Circle Image: ", cirlce_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()