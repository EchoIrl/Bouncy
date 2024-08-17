from cmu_graphics import *
# is ball clicked
pickedUp = False

    ### sky
Rect(0,0,400,400,fill='skyBlue')
    #sun and moon
Sun= Group(Circle(200,50,50,fill=gradient('yellow','lightYellow')))
sunSpeed=0

        ### Clouds
# Generic Cloud
Cloud1 = Group(
    Circle(77,60,35,fill='white',opacity=30),
    Circle(77-35,60+10,35,fill='white',opacity=50),
    Circle(77+30,60+15,35,fill='white',opacity=60),
    Oval(77,64,75,30,fill='white',opacity=70),
    Oval(77-10,64+20,100,30,fill='white',opacity=70),
    Oval(77-10,64+20,110,50,fill='white',opacity=70))
# Fastest Cloud
Cloud2 = Group(
    Circle(77+200,60,35,fill='white',opacity=30),
    Circle(77-35+200,60+10,35,fill='white',opacity=50),
    Circle(77+30+200,60+15,35,fill='white',opacity=60),
    Oval(77+200,64,75,30,fill='white',opacity=70),
    Oval(77-10+200,64+20,100,30,fill='white',opacity=70),
    Oval(77-10+200,64+20,110,50,fill='white',opacity=70))
# Slow Cloud
Cloud3 = Group(
    Circle(77+200,60,35,fill='white',opacity=30),
    Circle(77-35+200,60+10,35,fill='white',opacity=40),
    Circle(77+30+200,60+15,35,fill='white',opacity=60),
    Oval(77+200,64,75,30,fill='white',opacity=60),
    Oval(77-10+200,64+20,100,30,fill='white',opacity=70),
    Oval(77-10+200,64+20,110,50,fill='white',opacity=60))
# Very slow long cloud
Cloud4 = Group(
    Oval(77,60+10,200,35+15,fill='white',opacity=30),
    Oval(77-35,60+10,83,35,fill='white',opacity=50),
    Oval(77+30,60+15,200,35+5,fill='white',opacity=60),
    Oval(77,64,75,30,fill='white',opacity=70),
    Oval(77-10,64+20,200,45,fill='white',opacity=70),
    Oval(77-10,64+20,110,50,fill='white',opacity=70))

    ### Ground
def Ground():
    Polygon(0,400,0,326,400,326, 400,400,fill='saddleBrown')
    Line(0,326,123,337,fill='green',lineWidth=12)
    Line(0,326,400,326,fill='green',lineWidth=12)
    Line(121,337,400,326,fill='green',lineWidth=12)
    Line(0,326-10,123,337-10,fill='green',lineWidth=12,opacity=70)
    Line(0,326-10,400,326-10,fill='green',lineWidth=12,opacity=70)
    Line(121,337-10,400,326-10,fill='green',lineWidth=12,opacity=70)
    Line(0,326-21,400,326-21,fill='green',lineWidth=10,opacity=50)

# draws the ground and makes the object off-screen that bounces the ball
bouncy=Rect(1000,75,10,500)
Ground()

# defines ball
ball = Circle(200,200,20,fill='red')
ballBounce = Oval(200,200,50,20,fill='red')
bounceUp = Oval(200,200,20,50,fill='red')
ball.bottom=bouncy.top
ballBounce.bottom=ball.bottom-10
bounceUp.bottom=ball.bottom-10
ballBounce.visible=False
bounceUp.visible=False

# if you click on the ball it picks it up
def onMousePress(X,Y,button):
    global pickedUp
    if(button==0):
        if(ball.centerX+20>=X>=ball.centerX-20):
            if(ball.centerY+20>=Y>=ball.centerY-20):
                pickedUp=True
    else:
        pickedUp = False

# while picked up the ball moves to your cursor, otherwise it bounces.
def onMouseMove(X,Y):
    global pickedUp
    if(pickedUp==True):
        ball.centerX=X
        ball.centerY=Y
        ballBounce.centerX = X
        ballBounce.centerY = Y 
        bounceUp.centerX = X
        bounceUp.centerY = Y
        bouncy.rotateAngle=90
    ### Controls the speed of all animation in the scene.
# How fast the ball bounces
bounceSpeed=5
# How fast the Clouds Move
speedyCloud=0.5
# How fast everything moves
    # default=30
app.stepsPerSecond=30
    ### Controls all animation in the scene.
def onStep():
    global pickedUp
    global bounceSpeed
    global sunSpeed
    global speedyCloud
    # controls how the ball bounces.
    if(pickedUp!=True):
        bouncy.rotateAngle+=bounceSpeed
        ball.bottom=bouncy.top
        if(100>=bouncy.rotateAngle>=75):
            ballBounce.visible=True
            ball.visible=False
            ballBounce.bottom=ball.bottom+10
        else:
            ballBounce.visible=False
            ball.visible=True
            ballBounce.bottom=ball.bottom
            ballBounce.centerX=ball.centerX
        if(74>=bouncy.rotateAngle>=35 or -100<=bouncy.rotateAngle<=-50):
            bounceUp.visible=True
            ball.visible=False
            bounceUp.bottom=ball.bottom
            bounceUp.centerX=ball.centerX
        else:
            bounceUp.visible=False
        if(bouncy.rotateAngle>=100):
            bouncy.rotateAngle=-80
    #controls the clouds
    Cloud1.centerX+=1.5+speedyCloud
    Cloud2.centerX+=2.2+speedyCloud
    Cloud3.centerX+=0.2+speedyCloud
    Cloud4.centerX+=0+speedyCloud
    if(Cloud1.centerX>=472.5):
        Cloud1.centerX=-72.5
    if(Cloud2.centerX>=472.5):
        Cloud2.centerX=-72.5
    if(Cloud3.centerX>=472.5):
        Cloud3.centerX=-72.5
    if(Cloud4.centerX>=572.5):
        Cloud4.centerX=-172.5
    #controls the sun
                            ###!!!DO NOT REMOVE!!!###
    sunSpeed+=0.03
    ###^ sunSpeed HAS TO BE in the onStep Variable as it increments every frame.
    Sun.centerX,Sun.centerY=getPointInDir(200,400,sunSpeed,350)
    if(sunSpeed>=47.5):
        sunSpeed=-47.5
cmu_graphics.run()
