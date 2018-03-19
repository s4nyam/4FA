import numpy as np
import cv2
import os


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#this is the cascade we just made. Call what you want
facesamy_cascade = cv2.CascadeClassifier('myhaar.xml')
####TRAINING DATATSET MUST BE REQUIRED AS PER UP TO 10000 PHOTOS to train #####
camera_port = 0
 
ramp_frames = 30
 
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():

 retval, im = camera.read()
 return im

for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
os.system("sleep 4s")
camera_capture = get_image()
file = "/home/superuser/Desktop/project_KEYRING/test_image.png"

cv2.imwrite(file, camera_capture)

del(camera) 




os.system("python /home/superuser/Desktop/project_KEYRING/ascii.py /home/superuser/Desktop/project_KEYRING/test_image.png > ff.txt")
with open('/home/superuser/Desktop/project_KEYRING/myTextFile.txt','a') as myFile:
	myFile.write('\n')	
	with open('ff.txt','r') as fie:
		data=fie.read()
		myFile.write(data)

cap = cv2.VideoCapture(0)


i=0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # add this
    # image, reject levels level weights.
    facsams = facesamy_cascade.detectMultiScale(gray, 20, 20)
    # add this
    for (x,y,w,h) in facsams:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Sanyam', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Sanyam', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
	if(i==0):	
		os.system("python /home/superuser/Desktop/project_KEYRING/location_module.py")
	i += 1      
	roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 2:
        break
cap.release()
cv2.destroyAllWindows()
