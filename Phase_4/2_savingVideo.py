import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')
recorder = cv2.VideoWriter("myvideo.mp4", codec, 20, (frame_width, frame_height))

while True:
    success, frame = camera.read()

    if not success:
        break


    recorder.write(frame)
    cv2.imshow("Live Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break

recorder.release()
camera.release()
cv2.destroyAllWindows()

