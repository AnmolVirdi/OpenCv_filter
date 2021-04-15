import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
#Using the realtime video as input

while True:
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for (x, y, w, h) in faces:
        #cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #cv2.putText(img2,'Face',(x+50,y-50),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,0),2)

        cv2.line(img2,(x+30,y+50),(x+70, y+90),(255,0,0),2)
        cv2.line(img2,(x+30,y+90),(x+70,y+50 ),(255,0,0),2)

        cv2.line(img2,(x+90,y+50),(x+130, y+90),(255,0,0),2)
        cv2.line(img2,(x+90,y+90),(x+130,y+50 ),(255,0,0),2)

    # Display

    cv2.imshow('img', img2)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
