import random, math
import os, sys, inspect, thread, time
sys.path.insert(0, "C:\Users\ahanamukhopadhyay\Downloads\LeapDeveloperKit_2.3.1+31549_mac\LeapSDK\lib/x86")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

import random, math
from Tkinter import *

class Pod(object):
    #Model
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.fill = "green"
    
    #View 
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "green3", outline = "black", width = 2)
        
    def drawLeap(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "purple", outline = "black", width = 2)
        
    def drawWithScroll(self,scrollY,hieght):
        self.cy += scrollY
        if self.cy > hieght:
            return False
    
    def getTop(self):
        return self.cy - 100
        
    # def __repr__(self):
    #     return "normal pod"
    
class WithSpring(Pod):
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "green3", outline = "black", width = 2)
        x = (x1 + x2) // 2
        canvas.create_oval(x - 5, y1 - 8, x + 10, y1)
        canvas.create_oval(x - 5, y1 - 10, x + 10, y1 - 2)
        canvas.create_oval(x - 5, y1 - 12, x + 10, y1 - 4)
        canvas.create_oval(x - 5, y1 - 14, x + 10, y1 - 6)        
        
class BreakingPod(Pod):
    # def __init__(self, cx, cy):
    #     super().__init__(cx,cy)
    
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "brown", outline = "black", width = 2)
        
        crackP = (self.cx - 2, self.cy - 10, self.cx + 2, self.cy - 10, self.cx, self.cy, self.cx - 3, self.cy + 2, self.cx + 2, self.cy + 10, self.cx  - 2, self.cy + 10, self.cx - 7, self.cy + 2, self.cx - 5, self.cy)
        canvas.create_polygon(crackP, fill = "white")

class MovingPod(Pod):
    def __init__(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.speed = 5
        self.direction = 1
    
    def draw(self,canvas):
        x1 = self.cx - 30
        x2 = self.cx + 30
        y1 = self.cy - 10
        y2 = self.cy + 10
        r = 5
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, smooth = True, fill = "blue", outline = "black", width = 2)
    
    def move(self):
        self.cx += self.speed * self.direction
    
    def isHittingSide(self, width, height):
        return (self.cx - 30 <= 0 or self.cx + 30 >= width)
               
    def change(self):
        self.direction *= -1
    

    
##
 
class Ball(object):
    def __init__(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.speed = 30
        
    def draw(self,canvas):
        canvas.create_oval(self.cx - 5, self.cy - 5, self.cx + 5, self.cy + 5, fill = "IndianRed1", outline = "black")
    
    def shootBall(self):
        self.cy -= self.speed
        print(self.cy)
        
    def onScreen(self):
        return(self.cy >= 0)

##      
        
#Model
class Dude(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.speed = 50
        
    def draw(self, canvas):
        r = 50/2
        #yellow circle body
        canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, fill = "gold", outline = "gold")
        #yellow rectangle body
        canvas.create_rectangle(self.cx-r, self.cy,self.cx+r, self.cy+r, fill = "gold", outline = "gold")
        #green pantS
        canvas.create_rectangle(self.cx-r, self.cy+r,self.cx+r, self.cy+2*r, fill = "green", outline = "black")
        canvas.create_line(self.cx-r, self.cy+r+r/3,self.cx+r, self.cy+r+r/3)
        canvas.create_line(self.cx-r, self.cy+r+2*r/3,self.cx+r, self.cy+r+2*r/3)
        #legs
        margin = 5
        legDiff = (2*r-2*margin)//3
        for leg in range(4):
            x1 = self.cx-r+margin+legDiff*leg
            x2 = x1 + 4
            y1 = self.cy+2*r
            y2 = self.cy+2*r + 10
            canvas.create_line(x1, y1, x1, y2, width = 2)
            canvas.create_line(x1, y2, x2, y2, width = 2)
        #rectangle and circle nose
        nose = 10
        canvas.create_rectangle(self.cx+r, self.cy-nose/4,self.cx+r+8, self.cy+nose/4, fill = "gold", outline ="gold")
        centerX = self.cx+r+8
        centerY = self.cy
        noseR = nose/4
        canvas.create_oval(centerX-noseR, centerY-noseR, centerX+noseR, centerY+noseR, fill = "gold", outline = "gold")
        #two eyes
        canvas.create_oval(self.cx+6, self.cy-3, self.cx+8, self.cy, fill = "black")
        canvas.create_oval(self.cx+15, self.cy-3, self.cx+17, self.cy, fill = "black")
        
    def drawWithScroll(self,scrollY):
        self.cy -= scrollY
        
    def abovePod(self,other):
        if(not isinstance(other, Pod)): # Other must be an Pod
            return False
        else:
            return (other.cy - 10 >= self.cy + 35) and (other.cx + 30 >= self.cx >= other.cx - 30) 
            
    def touchMonster(self,other):
        if(not isinstance(other, Monster)):
            return False
        else:
            d = ((self.cx-other.cx)**2 + (self.cy-other.cy)**2)**0.5
            return d < 50
            
     


class LeftDude(Dude):
    def draw(self, canvas):
        r = 50/2
        #yellow circle body
        canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, \
        fill = "gold", outline = "gold")
        #yellow rectangle body
        canvas.create_rectangle(self.cx-r, self.cy,self.cx+r, self.cy+r, fill = "gold", outline = "gold")
        #green pants
        canvas.create_rectangle(self.cx-r, self.cy+r,self.cx+r, self.cy+2*r, fill = "green", outline = "black")
        canvas.create_line(self.cx-r, self.cy+r+r/3,self.cx+r, self.cy+r+r/3)
        canvas.create_line(self.cx-r, self.cy+r+2*r/3,self.cx+r, self.cy+r+2*r/3)
        #legs
        margin = 5
        legDiff = (2*r-2*margin)//3
        for leg in range(4):
            x1 = self.cx-r+margin+legDiff*leg
            x2 = x1 - 4
            y1 = self.cy+2*r
            y2 = self.cy+2*r + 10
            canvas.create_line(x1, y1, x1, y2, width = 2)
            canvas.create_line(x1, y2, x2, y2, width = 2)
        #rectangle and circle nose
        nose = 10
        canvas.create_rectangle(self.cx-r, self.cy-nose/4,self.cx-r-8, self.cy+nose/4, fill = "gold", outline ="gold")
        centerX = self.cx-r-8
        centerY = self.cy
        noseR = nose/4
        canvas.create_oval(centerX-noseR, centerY-noseR, centerX+noseR, \
        centerY+noseR, fill = "gold", outline = "gold")
        #two eyes
        canvas.create_oval(self.cx-6, self.cy-3, self.cx-8, self.cy, fill = "black")
        canvas.create_oval(self.cx-15, self.cy-3, self.cx-17, self.cy, fill = "black")

class UpDude(Dude):
    def draw(self, canvas):
        r = 50/2
        #yellow circle body
        canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, \
        fill = "gold", outline = "gold")
        #yellow rectangle body
        canvas.create_rectangle(self.cx-r, self.cy,self.cx+r, self.cy+r, \
        fill = "gold", outline = "gold")
        #green pants
        canvas.create_rectangle(self.cx-r, self.cy+r,self.cx+r, self.cy+2*r, \
        fill = "green", outline = "black")
        canvas.create_line(self.cx-r, self.cy+r+r/3,self.cx+r, self.cy+r+r/3)
        canvas.create_line(self.cx-r, self.cy+r+2*r/3,self.cx+r, self.cy+r+2*r/3)
        #legs
        margin = 5
        legDiff = (2*r-2*margin)//3
        for leg in range(4):
            x1 = self.cx-r+margin+legDiff*leg
            y1 = self.cy+2*r
            y2 = self.cy+2*r + 10
            canvas.create_line(x1, y1, x1, y2, width = 2)
        #rectangle and circle nose
        nose = 10
        canvas.create_rectangle(self.cx-nose/4, self.cy-r, self.cx+nose/4, self.cy-r-8, fill = "gold", outline = "gold")
        centerX = self.cx
        centerY = self.cy-r-8
        noseR = nose/4
        canvas.create_oval(centerX-noseR, centerY-noseR, centerX+noseR, \
        centerY+noseR, fill = "gold", outline = "gold")
        #two eyes
        canvas.create_oval(self.cx-6, self.cy-10, self.cx-4, self.cy-7, fill = "black")
        canvas.create_oval(self.cx+4, self.cy-10, self.cx+6, self.cy-7, fill = "black")



##
class Monster(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        
    def draw(self, canvas):
        #main shape
        r = 35
        coord = self.cx - r/2,self.cy+100, self.cx+r/2, self.cy+40
        canvas.create_arc(coord, start=0, extent=180, fill="dodger blue", outline = "black", width = 4)
        #teeth with lines
        canvas.create_rectangle(self.cx, self.cy+61, self.cx+3, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+3, self.cy+61, self.cx+3, self.cy+55, fill = "black")
        canvas.create_rectangle(self.cx+3, self.cy+61, self.cx+6, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+6, self.cy+61, self.cx+6, self.cy+55, fill = "black")
        canvas.create_rectangle(self.cx+6, self.cy+61, self.cx+9, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+9, self.cy+61, self.cx+9, self.cy+55, fill = "black")
        canvas.create_rectangle(self.cx+9, self.cy+61, self.cx+12, self.cy+55, fill = "violet")
        canvas.create_line(self.cx+12, self.cy+61, self.cx+12, self.cy+55, fill = "black")
        eyeX = self.cx + 4
        eyeY = self.cy +50
        #draws eye
        canvas.create_oval(eyeX-2, eyeY-2, eyeX+3, eyeY+3, fill = "yellow")
        #draws hair spikes
        canvas.create_line(self.cx, self.cy+40, self.cx, self.cy+30)
        canvas.create_line(self.cx-3, self.cy+41, self.cx-4, self.cy+30)
        canvas.create_line(self.cx+3, self.cy+41, self.cx+4, self.cy+30)
        canvas.create_line(self.cx-6, self.cy+42, self.cx-8, self.cy+32)
        canvas.create_line(self.cx+6, self.cy+42, self.cx+8, self.cy+32)
        #draw two legs
        margin = 5
        legX = self.cx - r/2 + margin
        y1 = self.cy+100
        y2 = self.cy+110
        canvas.create_line(legX + r/2, self.cy+70, legX+r/2, self.cy+80, fill = "dodger blue", width = 3)
        canvas.create_line(legX, self.cy+70, legX, self.cy+80, fill = "dodger blue", width = 3)
        canvas.create_line(legX + r/2, self.cy+80, legX+r/2+7, self.cy+80, fill = "dodger blue", width = 3)
        canvas.create_line(legX, self.cy+80, legX+7, self.cy+80, fill = "dodger blue", width = 3)
    
    def move(self):
        x = random.randint(0,2)
        directionX = random.choice([-1,1])
        self.cx += x * directionX
        y = random.randint(0,2)
        directionY = random.choice([-1,1])
        self.cy += y * directionY

        
    
class RedMonster(Monster):
    def draw(self, canvas):
        xr = 40
        yr = 35
        #spikes
        angle = 0
        r = xr * 2/3
        for i in range(16):
            canvas.create_line(self.cx, self.cy, self.cx + r*math.cos(angle), self.cy + r*math.sin(angle))
            angle += math.radians(360/16)
        #main oval
        canvas.create_oval(self.cx - xr/2, self.cy - yr/2, self.cx + xr/2, self.cy + yr/2, fill = "tomato", width = 3)
        xrDif = xr/5
        #three yellow dots
        canvas.create_oval(self.cx - xr/2 + 5, self.cy - 3, self.cx - xr/2 + 5 + xrDif, self.cy + 5, fill = "gold", width = 2)
        canvas.create_oval(self.cx - xr/2 + 2*xrDif+1, self.cy - 10, self.cx - xr/2 + 3*xrDif+1, self.cy-2, fill = "gold", width = 2)
        canvas.create_oval(self.cx + xr/2 - 5 - xrDif, self.cy - 3, self.cx + xr/2 - 5, self.cy + 5, fill = "gold", width = 2)
        #eyes inside yellow dots
        canvas.create_oval(self.cx - xr/2 + 5+xrDif/2-1, self.cy - 1, self.cx - xr/2 + 5 + xrDif/2+1, self.cy + 1, fill = "black")
        canvas.create_oval(self.cx - xr/2 + 2*xrDif+1+xrDif/2-1, self.cy - 7, self.cx - xr/2 + 2*xrDif+1+xrDif/2+1, self.cy-6, fill = "black", width = 2)
        canvas.create_oval(self.cx + xr/2 - 5 - xrDif/2-1, self.cy, self.cx + xr/2 - 5 - xrDif/2-1, self.cy+1, fill = "black", width = 2)
        #two eyes
        canvas.create_oval(self.cx-3, self.cy+1, self.cx-1, self.cy + 4, fill = "gold", width = 2)
        canvas.create_oval(self.cx+2, self.cy+1, self.cx+4, self.cy + 4, fill = "gold", width = 2)
        #line
        canvas.create_line(self.cx-xr/2+3, self.cy+8, self.cx+xr/2-3, self.cy+8, width = 2)




#### Graphics Functions ####



def init(data):
    
    data.pods = []
    data.monsters = []
    data.score = 0

    data.highScore = 0

    data.name = "dude"
    data.timerCalls = 0
    data.endDudeX = data.width//2 - 200
    data.endDudeY = data.height - 100
    data.endDude = Dude(data.endDudeX,data.endDudeY)
    data.endPod = Pod(data.endDudeX, data.endDudeY+70)
    data.endMonster = Monster(400, 50)
    data.endRedMonster = RedMonster(60, 260)
    #grid
    data.rows = 26
    data.cols = 20
    
    data.springSpeed = 50
    
    #dude
    data.dudeMode = "normal"
    data.dudeX = data.width//2
    data.dudeY = data.height - 120
    data.dude = Dude(data.dudeX,data.dudeY)
    data.speed = 40
    data.fall = False
    data.mode='homescreen'
    
    #board
    data.newBoard = True
    data.scrollY = 0
    
    #leap motion data
    data.secs = 0
    data.blockCoords = []
    data.tipPos = 0
    data.controller = Leap.Controller()
    data.frame = data.controller.frame()
    data.fingerNames = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    data.boneNames = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    data.currDir = "Right"
    data.yCoor = data.height 
    data.xCoor = data.width // 2
    
    data.over = False
    data.overTime = 0

    data.player = False
def endScreen(data, canvas):
    #background
    canvas.create_rectangle(0,0,data.width,data.height, fill = "old lace")
    #grid
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, outline = "gold")
    canvas.create_text(250, 200, text = "gameover!", font = "Courier 60", fill = "red4")
    score=data.score
    canvas.create_text(250, 300, text = "your score:%d" %score, font = "Courier 30", fill = "black")
    canvas.create_text(300, 350, text = "name: %s" %data.name, font = "Courier 30", fill = "black")

    #play again 
    canvas.create_oval(150, 450, 305, 515, width = 3, fill = "old lace")
    canvas.create_oval(155, 455, 300, 510, width = 4, fill = "old lace", outline = "gold")
    canvas.create_text(227, 480, text = "play again", font = "Courier 22")
    #menu
    canvas.create_oval(260, 520, 415, 585, width = 3, fill = "old lace")
    canvas.create_oval(265, 525, 410, 580, width = 4, fill = "old lace", outline = "gold")
    canvas.create_text(337, 550, text = "menu", font = "Courier 25")
    #draw dude
    data.endDude.draw(canvas)
    data.endPod.draw(canvas)
    data.endMonster.draw(canvas)
    data.endRedMonster.draw(canvas)
def timerFired(data):
    if data.mode == 'play':
        data.score += 1
    if data.mode=='play' or data.player == True:
        #Pods
        data.timerCalls += 1
        if data.over == True:
            data.overTime += 1
            if data.overTime >= 30:
                data.mode = "gameover"
        #movement
        for pods in data.pods:
            if isinstance(pods,MovingPod):
                pods.move()
                if pods.isHittingSide(data.width,data.height):
                    pods.change()
        for monster in data.monsters:
            monster.move()
            
        if data.timerCalls == 2:
            data.newBoard = False
        
        gameOver = True
        for pod in data.pods:
            if data.dude.abovePod(pod):
                if isinstance(pod, WithSpring):
                    data.dudeY = pod.getTop()
                else:
                    gameOver = False
                    data.dudeY = pod.getTop()
        if gameOver == True:
            if data.timerCalls > 20:
                data.speed = -40
                data.dudeY -= data.speed
                data.over = True
                #data.overTime += 1
            else:
                #jumping
                data.dudeY += data.speed
                g = 10 #gravity acceleration 
                data.speed -= g
                # if data.fall == False:
                if data.speed < -40:
                    data.speed = 40
        else:
            #jumping
            data.dudeY += data.speed
            g = 10 #gravity acceleration 
            data.speed -= g
            # if data.fall == False:
            if data.speed < -30:
                data.speed = 30
        
        # #scroll
        if data.dudeY <= data.height//2:
            data.scrollY += 20
        else: data.scrollY = 0
        
        
        for monster in data.monsters:
            if data.dude.touchMonster(monster):
                data.mode = "gameover"
            
        # maxPod = 0
        # for pod in data.pods:
        #     if data.dude.abovePod(pod):
        #         tempPod = pod.getTop()
        #         if tempPod <= maxPod:
        #             maxPod = tempPod
        #         if isinstance(pod,WithSpring):
        #             data.dudeY = pod.getTop()
        #             data.dudeY -= data.springSpeed
        #         data.dudeY = pod.getTop()   
        #         # elif isinstance(pod,BreakingPod):
        #         #     data.pods.remove(pod)
        #         #     data.dudeMode = "fall"
        #         
        # #jumping
        # data.dudeY += data.speed
        # g = 10 #gravity acceleration 
        # data.speed -= g
        # # if data.fall == False:
        # if data.speed < -30:
        #     data.speed = 30
        #     
        # #scroll
        #     
        # if data.dudeY <= data.height//2:
        #     data.scrollY += 20
        # else: data.scrollY = 0
        
        
        
    #leap motion code
    if data.timerDelay % 10 == 0:
        data.secs += 1
    updateLeapMotionData(data)
    printLeapMotionData(data)
    
def updateLeapMotionData(data):
    data.frame = data.controller.frame()

def printLeapMotionData(data):
    frame = data.frame
    data.controller.config.set("Gesture.Circle.MinRadius", 2)
    data.controller.config.set("Gesture.Circle.MinArc", .1)
    data.controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
    data.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    data.controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
    data.controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
    data.controller.config.set("Gesture.Swipe.MinLength", 100)
    data.controller.config.set("Gesture.Swipe.MinVelocity", 500)
    
    mostForwardOnHand = frame.hands[0].fingers.frontmost
    #position of hand
    data.tipPos = (mostForwardOnHand.tip_position[0], \
    mostForwardOnHand.tip_position[1])
    #print data.tipPos[1]
    data.yCoor = data.height - ((data.tipPos[1]-40) * data.height/160)
    data.xCoor = (data.tipPos[0] - (-70))*data.width/140
    print "IMPORTANT", data.xCoor
    #position of block
    blockPos = (data.xCoor, data.yCoor,\
    data.xCoor, data.yCoor, data.secs)
    
    '''blockPos = (data.tipPos[0]+300, data.height-data.tipPos[1]*1.1,\
    data.tipPos[0]+5, data.height-data.tipPos[1]*1.1, data.secs)'''
    

    # Get hands
    prevPos = 0.5
    for hand in frame.hands:
        if hand.grab_strength != prevPos and hand.grab_strength == 1.0:
            print hand.grab_strength
            data.blockCoords.append(blockPos)
            break
        prevPos = hand.grab_strength

        handType = "Left hand" if hand.is_left else "Right hand"
        if handType == "Left hand":
            print "Left HAND"
            data.shootingBall = True

        if handType == "Right hand":
            #print "here", hand.palm_position[0]
            if hand.palm_position[0] > 0: 
                data.dir = "right"
                data.dudeMode = "normal"
                data.dudeX += 7
                #print "right"
            else:
                data.dir = "left"
                data.dudeMode = "left"
                data.dudeX -= 7
                #print "left"
        
                
            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction
    
def drawhome(canvas,data): 
    #background
    canvas.create_rectangle(0,0,data.width,data.height, fill = "old lace")
    #grid
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, outline = "gold")
    createButton(canvas,100,200,'play')
    createButton(canvas,167,300,'design')
    createButton(canvas,130,400,'scores')
    canvas.create_text(45,50,text='doodle jump pro',fill='red4',anchor=NW,font="Courier 45")
    pod1=Pod(60,580)
    pod1.draw(canvas)
    pd2=Pod(360,500)
    pd2.draw(canvas)
    pod3=BreakingPod(400,300)
    pod3.draw(canvas)
    
            
def createButton(canvas,topx,topy,text):
    canvas.create_oval(topx,topy,topx+150,topy+50,outline='black')
    canvas.create_oval(topx+4,topy+4,topx+146,topy+46,outline='gold',width=4)
    canvas.create_text((2*topx+100)//2,topy+7,text=text,fill='black',anchor=NW,font="Courier 23 italic")

def getCellBounds(row,col,data):
    columnWidth = data.width / data.cols
    rowHeight = data.height / data.rows
    x0 = col * columnWidth
    x1 = (col+1) * columnWidth
    y0 = row * rowHeight
    y1 = (row+1) * rowHeight
    return (x0, y0, x1, y1)    
def drawBlank(canvas,data):
    #background
    canvas.create_rectangle(0,0,data.width,data.height, fill = "old lace")
    #grid
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, outline = "gold")

def drawBoard(canvas,data):
    cxL = random.sample(range(30,470,5), 18)
    cyL = random.sample(range(10,640,20), 18)
    for i in range(1,9):
        newPod = Pod(cxL[i],cyL[i])
        data.pods.append(newPod)
    for j in range(9,13):
        newBPod = BreakingPod(cxL[j],cyL[j])
        data.pods.append(newBPod)
    for k in range(14,16):
        newSPod = WithSpring(cxL[k],cyL[k]) 
        data.pods.append(newSPod)
    for l in range(16,18):
        newMPod = MovingPod(cxL[l],cyL[l])
        data.pods.append(newMPod)
    
    cxM = random.sample(range(30,470,60), 4)
    cyM = random.sample(range(10,640,20), 4)
    for m in range(3):
        type = random.choice(["red","blue"])
        if type == "blue":
            newMonster = Monster(cxM[m],cyM[m])
        elif type == "red":
            newMonster = RedMonster(cxM[m],cyM[m])
        data.monsters.append(newMonster)
    '''   
    cxL = random.sample(range(30,470,5), 25)
    cyL = random.sample(range(10 + data.height,640 + data.height,20), 25)
    for i in range(1,16):
        newPod = Pod(cxL[i],cyL[i])
        data.pods.append(newPod)
    for j in range(9,20):
        newBPod = BreakingPod(cxL[j],cyL[j])
        data.pods.append(newBPod)
    for k in range(14,23):
        newSPod = WithSpring(cxL[k],cyL[k]) 
        data.pods.append(newSPod)
    for l in range(16,25):
        newMPod = MovingPod(cxL[l],cyL[l])
        data.pods.append(newMPod)
    
    cxM = random.sample(range(30,470,60), 4)
    cyM = random.sample(range(200 + data.height ,640 + data.height,20), 4)
    for m in range(3):
        type = random.choice(["red","blue"])
        if type == "blue":
            newMonster = Monster(cxM[m],cyM[m])
        elif type == "red":
            newMonster = RedMonster(cxM[m],cyM[m])
        data.monsters.append(newMonster)
    '''
def drawPlayer(canvas, data):
        if data.dudeMode == "normal":
            data.dude = Dude(data.dudeX,data.dudeY)
            data.dude.drawWithScroll(data.scrollY)
            data.dude.draw(canvas)
        
        elif data.dudeMode == "left":
            data.dude = LeftDude(data.dudeX, data.dudeY)
            data.dude.drawWithScroll(data.scrollY)
            data.dude.draw(canvas)
            
def redrawAll(canvas, data):
    if data.mode=='homescreen':
        drawhome(canvas,data)
    elif data.mode=='play':
        if data.newBoard == True:
            drawBoard(canvas,data)
        
        #scrolling background
        y0 = -data.height
        canvas.create_rectangle(0,y0 + data.scrollY,data.width,data.height + data.scrollY, fill = "old lace")
        #grid
        for row in range(data.rows):
            for col in range(data.cols):
                (x0, y0, x1, y1) = getCellBounds(row, col, data)
                canvas.create_rectangle(x0, y0, x1, y1, outline = "gold")
        
        for pods in data.pods:
            pods.drawWithScroll(data.scrollY,data.height)
            pods.draw(canvas)
            
        for monster in data.monsters:
            monster.draw(canvas)
    
                
        if data.dudeMode == "normal":
            data.dude = Dude(data.dudeX,data.dudeY)
            data.dude.drawWithScroll(data.scrollY)
            data.dude.draw(canvas)
        
        elif data.dudeMode == "left":
            data.dude = LeftDude(data.dudeX, data.dudeY)
            data.dude.drawWithScroll(data.scrollY)
            data.dude.draw(canvas)
            
        canvas.create_text(50,50,text = str(data.score),font = "Courier 30", fill = "red4")
    elif data.mode=="gameover":
        endScreen(data,canvas)
    
    # elif data.dudeMode == "shoot":
    #     data.dude = UpDude(data.dudeX, data.dudeY)
    #     data.dude.drawWithScroll(data.scrollY)
    #     data.dude.draw(canvas)
    
    #floating block
    '''canvas.create_oval(data.tipPos[0]+300, data.height-\
    data.tipPos[1],data.tipPos[0]+310, data.height-data.tipPos[1]+10, width = 2)'''
    if data.mode=='design':
        drawBlank(canvas,data)
    canvas.create_oval(data.xCoor, data.yCoor,data.xCoor+10, data.yCoor + 10, width = 2)
    prevSecs = 0
    for i in data.blockCoords:
        if i[4] - prevSecs > 1:
            cx = i[2] 
            cy = i[3]
            newPod = Pod(cx, cy)
            data.pods.append(newPod)
            newPod.drawLeap(canvas)
            #canvas.create_line(i[0], i[1], i[2], i[3])
        prevSecs = i[4]
        
    if data.player == True:
        drawPlayer(canvas, data)
    
        
    

def mousePressed(event, data):
    if data.mode=='homescreen':
        if event.x>100 and event.x<250 and event.y>200 and event.y<250:
            if data.mode=='homescreen':
                data.mode='play'
        if event.x>167 and event.y>300 and event.x<317 and event.y<350:
                if data.mode=='homescreen':
                    data.mode='design'
    if data.mode=='gameover':
        if event.x>150 and event.y>450 and event.x<305 and event.y<515:
            data.mode='play'
            data.pods = []
            data.monsters = []
            data.score = 0
        
            data.highScore = 0
        
            data.name = "dude"
            data.timerCalls = 0
            data.endDudeX = data.width//2 - 200
            data.endDudeY = data.height - 100
            data.endDude = Dude(data.endDudeX,data.endDudeY)
            data.endPod = Pod(data.endDudeX, data.endDudeY+70)
            data.endMonster = Monster(400, 50)
            data.endRedMonster = RedMonster(60, 260)
            #grid
            data.rows = 26
            data.cols = 20
            
            data.springSpeed = 50
            
            #dude
            data.dudeMode = "normal"
            data.dudeX = data.width//2
            data.dudeY = data.height - 120
            data.dude = Dude(data.dudeX,data.dudeY)
            data.speed = 40
            data.fall = False
            
            #board
            data.newBoard = True
            data.scrollY = 0
            
            #leap motion data
            data.secs = 0
            data.blockCoords = []
            data.tipPos = 0
            data.controller = Leap.Controller()
            data.frame = data.controller.frame()
            data.fingerNames = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
            data.boneNames = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
            data.currDir = "Right"
            data.yCoor = data.height 
            data.xCoor = data.width // 2
            
            data.over = False
            data.overTime = 0
        
            data.player = False
        if event.x>260 and event.y>520 and event.x<415 and event.y<585:
            init(data)
    
            
    

def keyPressed(event, data):
    if event.keysym == "Left":
        data.dudeX -= 5
        data.dudeMode = "left"
    elif event.keysym == "Right":
        data.dudeX += 5
        data.dudeMode = "normal"
    elif event.keysym == "space":
        data.shootingBall = True
    elif event.keysym == 'r':
        init(data)
    elif event.keysym == 'p':
        data.player = True



#################################################################
# use the run function as-is
#################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0 , 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.title('doodle jump pro')
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 650)

