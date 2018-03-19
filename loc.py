import geocoder
import math
g = geocoder.ip('me')
z=g.latlng
lat=math.floor(z[0])
lon=math.floor(z[1])
print(lat,lon)
