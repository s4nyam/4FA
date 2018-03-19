import pyrebase
import geocoder
import math
import signal
import os

config = {
  "apiKey": "AIzaSyBHuAYDCCOw72Mk4gvW_rCeMsNRUeGTBew",
  "authDomain": "myapp-f80a0.firebaseapp.com",
  "databaseURL": "https://myapp-f80a0.firebaseio.com",
  "storageBucket": "myapp-f80a0.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
#all_users = db.child("Location").get()
#print(all_users.val())
lastval = db.child("Location").order_by_key().limit_to_last(1).get()
z=lastval.val()
st=str(z)
lat=st[56:58]
lon=st[77:79]
#print(lat,lon)
g = geocoder.ip('me')
y=g.latlng
lattoverify=str(int(math.floor(y[0])))
lontoverify=str(int(math.floor(y[1])))
#print(lattoverify,lontoverify)
if(lat == lattoverify and lon == lontoverify):
	print('Your location Mathched! Proceeding...',lattoverify,lontoverify)
        with open("/home/superuser/Desktop/project_KEYRING/myTextFile.txt",'a') as myFile:
		myFile.write(lattoverify)
		myFile.write(' ')
		myFile.write(lontoverify)
	os.system('python /home/superuser/Desktop/project_KEYRING/EncodeNow.py')
		
			
else:
	print('Your location doesnt match!rolling back...')

