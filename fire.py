  
import cv2
import numpy as np
import smtplib
import threading

Fire_Reported = 0


# video = cv2.VideoCapture("video_file") # If you want to use webcam use Index like 0,1.
video = cv2.VideoCapture(0) # If you want to use webcam use Index like 0,1.
 
while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    frame = cv2.resize(frame, (960, 540)) 
 
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)
 
    output = cv2.bitwise_and(frame, hsv, mask=mask)
    
    no_red = cv2.countNonZero(mask)
    
    if int(no_red) > 15000:
        print ('Fire detected')

    cv2.imshow("output", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cv2.destroyAllWindows()
video.release()
