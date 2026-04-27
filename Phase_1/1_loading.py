import cv2

image = cv2.imread(r"Images\small_bird.jpg")

if image is None:
    print("No Image Found")
else:
    print("Image Found")    
