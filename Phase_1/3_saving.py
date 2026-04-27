import cv2

image = cv2.imread(r"Images\small_bird.jpg")

if image is not None:
    success = cv2.imwrite("Images\output.png", image)
    if success:
        print("Image saved successfully")
    else:
        print("Error: Image not saved")
else:
    print("Image Not loaded")            