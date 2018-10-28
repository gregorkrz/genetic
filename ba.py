import turtle

z = turtle.Turtle()
z.color("blue")
z.penup()
z.speed(10)
z.setx(-200)
z.sety(-240)


for b in range(20):
	for i in range(20):
		z.dot()
		if(i < 19): z.forward(30)
		
	if(b%2):
		z.right(90)
		z.forward(30)
		z.right(90)
	else:
		# 1.,3.,5.
		z.left(90)
		z.forward(30)
		z.left(90)

'''





def draw(coords): #[x,y],[x,y]
	z.pendown()
	for i in range(len(coords)-1):
		goft(coords[i],coords[i+1])

def goft(p1,p2):

	print("goft",p1,p2)
	z.pendown()
	dx = p2[0]-p1[0]
	dy = p2[1]-p1[1]
	z.forward(dx * 30)
	z.left(90)
	z.forward(dy * 30)
	z.right(90)
		
		
#goft([0,0],[1,1])
		
draw([[0,0],[10,2],[20,20]])


#goft([0,0],[15,15])

	'''
turtle.done()
