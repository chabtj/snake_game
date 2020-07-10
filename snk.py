import turtle
import time
import random
import time
tscore=turtle.Turtle()
win=turtle.Screen()
head =turtle.Turtle()
fd=turtle.Turtle()
x=random.randint(-230,230)
y=random.randint(-230,230)
score=0
t=0
framesize=180
body=[]

head.penup()
def create_win():


    win.setup(width=500, height=500)
    win.title("snake game ")
    win.bgcolor ("yellow")
    win.tracer(0)#for screen update





def create_head():

    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(250,250)
    head.speed(0)
    head.direction="stop"
def move ():
    if (head.direction=="up"):
        y=head.ycor()
        head.sety(y+20)
    if (head.direction == "down"):
        y = head.ycor()
        head.sety(y - 20)
    if ( head.direction=="right"):
        x=head.xcor()
        head.setx(x+20)
    if (head.direction == "left"):
        x = head.xcor()
        head.setx(x-20)
def go_left():
    if ( head.direction!="right"):
        head.direction="left"

def go_down():
    if (head.direction!="up"):
        head.direction="down"

def go_up():
    if ( head.direction!="down"):
        head.direction="up"

def go_right():
    if (head.direction!="left"):
        head.direction="right"

def commandreader():
    win.listen()
    win.onkey(go_up,"w")
    win.onkey(go_down,"s")
    win.onkey(go_right,"d")
    win.onkey(go_left,"a")

fd.shape("circle")
fd.color("red")
fd.shapesize(0.5,0.5)




def fruit():
    global x
    global y

    fd.penup()

    fd.speed(0)

    fd.goto(x,y)


def mov_eat():
    global score
    global x
    global y
    if (head.distance(fd)<25):
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        score=score+5
        b1 = turtle.Turtle()
        b1.penup()
        b1.shape("square")
        b1.speed(0)
        b1.color("black")
        body.append(b1)
    fd.penup()
    fd.goto( x, y)

    for i in range (len(body)-1,0,-1):
        x1=body[i-1].xcor()
        y1=body[i-1].ycor()
        body[i].goto(x1,y1)
    if ( len(body)!=0):
        body[0].goto(head.xcor(),head.ycor())




def rubber():
    if (head.xcor() > 230):
        head.setx(head.xcor() - 460)
    if (head.xcor() < -230):
        head.setx(head.xcor() + 460)
    if (head.ycor() > 230):
        head.sety(head.ycor() - 460)
    if (head.ycor() < -230):
        head.sety(head.ycor() + 460)

def out():
    ctr=0
    for i in body :
        if (head.distance(i)<20 and ctr >4):

            return 0;
        ctr=ctr+1
tmp=0


def gameloop():
    create_win()
    create_head()
    flag = True
    while True:
        global t
        flag
        global tmp
        tscore.clear()
        win.update()
        move()
        commandreader()
        t=time.time()
        time.sleep(0.1)
        if (flag==True and (time.time()-t)>3 ):
            fruit()
            flag=False
        rubber()
        mov_eat()





        endgame=out()
        if (endgame==0):
            head.color("red")
            for i in body:
                i.color("red")
            if ( tmp==1):
                time.sleep(2)
                break
            tmp=tmp+1

        if (tmp==1):
            head.direction = "stop"


gameloop()

