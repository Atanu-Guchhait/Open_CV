import cv2

capture = cv2.VideoCapture(0) # 0-Internal camera, 1-External camera
while True:
    ret, frame = capture.read()

    if not ret:
        print("Could not load frame")
        break

    cv2.imshow("WebCam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break

capture.release()
cv2.destroyAllWindows()
