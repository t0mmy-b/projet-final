from math import *
global enemySprites
global furnituresSprites
global weaponBullet
global character
global angle
global targetAngle
global easing
global dir
global state
global playerX
global playerY
global livingEntitySpeed
playerX = 800
playerY = 800
livingEntitySpeedX = 0
livingEntitySpeedY = 0
LESX=livingEntitySpeedX
LESY=livingEntitySpeedY
state = 1
angle = 0
targetAngle = 0
easing = 0.2


class Enemy:
    def __init__(self):
        self.x=0
        self.y=0
        self.speed=5
        self.dead=False
        self.hasSeenPlayer=False
        self.accur=1
    def movement(self):
        self.x=self.x+self.speed
        self.y=self.y+self.speed
    def display(self):
        global enemySprites
        image(enemySprites,self.x,self.y)
        
        
        
class Meubles:
    def __init__(self):
        self.x=0
        self.y=80
    def display(self):
        global furnituresSprites
        image(furnituresSprites,self.x,self.y)
        
        
        
        
class Bullet:
    def __init__(self):
        self.x=0
        self.y=320
        self.collide=False
        self.speed=10
    def move(self):
        self.x=self.x+self.speed
        self.y=self.y+self.speed
    def display(self):
        fill(0)
        rect(self.x-3,self.y-1,self.x+3,self.y+1)
        
class Player:
    def __init__(self):
        global playerX
        global playerY
        global livingEntitySpeed
        self.x=playerX
        self.y=playerY
        self.dead=False
        self.hasBeenSeen=False
        self.attackType="ranged"
    def move(self):
        global playerX
        global playerY
        global livingEntitySpeed
        global LESY
        global LESX
        if keyPressed:
            if (key == 'z' or key == 'Z'):
                print(key)
                LESY -= 2
            if (key == 's' or key == 'S'):
                LESY += 2
            if (key == 'q' or key == 'Q'):
                playerX -= LESX
            if (key == 'd' or key == 'D'):
                playerX += LESX
            if (key == 'z' or key == 'Z' and key == 'q' or key == 'Q'):
                playerY -= LESY
                playerX -= LESX
            if (key == 'z' or key == 'Z' and key == 'd' or key == 'D'):
                playerY -= LESY
                playerX += LESX
            if (key == 's' or key == 'S' and key == 'q' or key == 'Q'):
                playerY += LESY
                playerX -= LESX
            if (key == 's' or key == 'S' and key == 'd' or key == 'D'):
                playerY += LESY
                playerX += LESX
            if (key == 'z' or key == 'Z' and key == 's' or key == 'S'):
                playerY = playerY
            if (key == 'q' or key == 'Q' and key == 'd' or key == 'D'):
                playerX = playerX
                
                playerX+=LESX
                playerY+=LESY
    def aimShoot(self):
        global character
        global angle
        global dir
        global targetAngle
        angle = atan2( mouseY-playerX,mouseX-playerY)
        dir = (angle - targetAngle) / PI+HALF_PI
        dir -= round( dir )
        dir *= TWO_PI
        targetAngle+=dir*easing
        noFill()
        pushMatrix()
        translate(playerX,playerY)
        rotate(targetAngle)
        imageMode(CENTER)
        image(character,playerX,playerY)
        translate(playerX, playerY)
        popMatrix()
        
    def display(self):
        global character
        imageMode(CENTER)
        image(character,self.x,self.y)
        
        
        
def inRange(ax,ay,bx,by):
    distance = sqrt(pow((bx-ax),2)+pow((by-ay),2))
    text(Enemy().hasSeenPlayer,50,50)
    text(distance,50,100)
    if distance <= 1000.0:
        Player().hasBeenSeen=True
        Enemy().hasSeenPlayer=True
        fill(0)
        text(Enemy().hasSeenPlayer,50,50)
        text(distance,50,100)
    
def keyPressed():
    global state
    if state == 1:
        Player().move()
def mouseClicked():
    if (mouseButton == LEFT):
        Bullet().x=playerX
        Bullet().y=playerY
        Bullet().move()
def setup():
    frameRate(60)
    clear()
    Player()
    background(255)
    # size(1600,900)
    fullScreen()
    global enemySprites
    global furnituresSprites
    global weaponBullet
    global character
    enemySprites=loadImage("data/sprites/living/enemy/enemy_0.png")
    furnituresSprites=loadImage("data/sprites/furnitures/desk.png")
    weaponBullet=loadImage("data/sprites/weapon/bullet.png")
    character=loadImage("data/sprites/living/player/standing.png")
    inRange(Enemy().x,Enemy().y,Player().x,Player().y)
    
    
def draw():
    smooth()
    noCursor()
    clear()
    fill(80,80,120)
    rect(0,0,width,height)
    line(width/2, 0, width/2, height)
    line(0, height/2, width, height/2)
    fill(255)
    ellipse(0,0,2000,2000)
    Player().aimShoot()
    Player().display()
    Player().move()
    inRange(Enemy().x,Enemy().y,Player().x,Player().y)
    
    # Bullet().display()
    # Enemy().display()
    # Meubles().display()
    
