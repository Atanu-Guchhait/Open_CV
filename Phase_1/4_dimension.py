import cv2

image = cv2.imread(r"Images\small_bird.jpg")

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded: \n Height:{h}, \n width:{w},  \n Channels:{c}")
else:
    print("Image not loaded")    