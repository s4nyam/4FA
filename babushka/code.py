import turtle 
s = raw_input("enter string")
polygon = turtle.Turtle()



z = [ord(c) for c in s]

for i in range(len(z)):
	#for j in range(len(z)):
	polygon.forward(z[i])
	polygon.left(z[i])
	#polygon.forward(z[i])
	#polygon.degrees(45)
	polygon.pos()
turtle.done()
