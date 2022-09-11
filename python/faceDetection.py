import cv2
import serial

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
arduino_serial = serial.Serial('COM1', 9600, timeout=0.1)

while capture.isOpened():
    _, frame = capture.read()
    # Mirror the frame from camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect face
    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    for x, y, w, h in face:
        coords = 'X{0:d}Y{1:d}'.format((x+w//2), (y+h//2))
        print(coords)
        # Write to arduino
        arduino_serial.write(coords.encode('utf-8'))

        # Plot face
        cv2.circle(frame, (x+w//2, y+h//2), 2, (0,255,0), 2)
        # Plot region
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0,0,255), 3)
    # Plot center region
    cv2.rectangle(frame,(640//2-30,480//2-30),
                  (640//2+30,480//2+30),
                  (255,255,255),3)
    # Display image
    cv2.imshow('img', frame)
    if cv2.waitKey(10)&0xFF == ord('q'):
        break
capture.realease()
cv2.destroyAllWindows()
