import cv2

face_cascade = cv2.CascadeClassifier(r"HaarCascade\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"HaarCascade\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"HaarCascade\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)


    roi_gray = gray_image[y:y+h, x:x+h]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
    if len(eyes)>0:
        cv2.putText(frame, "Eyes Detected", (x,y-30), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 2)

    smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 5)
    if len(smiles)>0:
        cv2.putText(frame, "Smile Detected", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 2)    


    cv2.imshow("Webcam Live", frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()      


