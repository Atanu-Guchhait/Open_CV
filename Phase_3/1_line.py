import cv2

image = cv2.imread(r"Images\white_cloud.jpg")

if image is None:
    print("Image Not Loaded")
else:
    pt1 = (50,100)
    pt2 = (300,100)
    color = (255, 0, 0)
    thickness = 4


    line_image = cv2.line(image, pt1, pt2, color, thickness)

   
    cv2.imshow("Line Image: ", line_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()    