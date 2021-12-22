
res=0
for dxx in range(287):
	for dyy in range(-100,300):
		dx = dxx
		dy=dyy
		x =0
		y=0
		
		for t in range(300):
			x+=dx
			y+=dy
			if dx > 0:
				dx-=1
			dy-=1
			if 248<=x<=285 and -85<=y<=-56:
			#if 20<=x<=30 and -10<=y<=-5:
				res+=1
				break
print(res)
'''

dx=7
dy=1
x=0
y=0
res=0
for t in range(300):
	x+=dx
	y+=dy
	if dx > 0:
		dx-=1
	dy-=1
	print(x,y,dx,dy)
	#if 248<=x<=285 and -85<=y<=-56:
	if 20<=x<=30 and -10<=y<=-5:
		res+=1
print(res)
'''