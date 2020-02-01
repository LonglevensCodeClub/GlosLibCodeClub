from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(90)

k=0,0,0
w=255,255,255

def setGrid(x,y):
	a,b,c,d=k,k,k,k
	if x==1:
		a=w
	elif x==2:
		b=w
	elif x==3:
		c=w
	else:
		d=w
	t=0.25
	grid = [a,k,c,k,d,k,b,k,
		b,k,d,k,a,k,c,k,
		c,k,a,k,b,k,d,k,
		d,k,b,k,c,k,a,k,
		a,k,c,k,d,k,b,k,
		b,k,d,k,a,k,c,k,
		c,k,a,k,b,k,d,k,
		d,k,b,k,c,k,a,k]
	s=8*y
	for e in range(64-s,64):
		grid[e]=w
	sense.set_pixels(grid)
	sleep(t)
d=0
while True:
	for x in range(4):
		setGrid(x,d)
	d+=1
	if d>8:
		d=0
