import random;
import math;
global pi;
pi = math.pi;
numTrue = 0;
global speed;
speed = 0;
class Player:
    def __init__(self, X, Y, keys):
        self.X = X;
        self.Y = Y;
        self.Width = 70;
        self.Height = 70;
        self.powers = [];
        self.speed = 8;
        self.keys = keys;
        self.numTrue = 0;
        self.lives = 3;
        self.points = 0;
    def draw(self):
        moveDist = self.getPlayerSpeed();
         # Player pressed up arrow
        if self.keys[0] == True:
            self.move(0, moveDist);        
    # Player pressed down arrow    
        if self.keys[1] == True:
            self.move(0,(-1 * moveDist));        
    # Player pressed left arrow    
        if self.keys[2] == True:        
            self.move((-1 * moveDist), 0);        
    # Player pressed right arrow    
        if self.keys[3] == True:        
            self.move(moveDist, 0);
        fill(0,0,255);
        rect(self.X,self.Y,self.Width,self.Height);
        return None;
        
    def getPlayerSpeed(self):
        global level;
        numTrue = 0;
        global pi; 
        speed = 0;
        for i in self.keys:
            if i == True:
                numTrue += 1;
        if numTrue > 1:
            speed = sin(pi/4) * 8;
        else:
            speed = 8;

        self.speed = speed;
        return speed;
    def move(self, dX, dY):
        self.X += dX;
        self.Y -= dY;
        if self.X+self.Width > 1000:
            self.X = 1000 - self.Width;
        if self.X < 0:
            self.X = 0;
        if self.Y+self.Height > 800:
            self.Y = 800 - self.Height;
        if self.Y < 0:
            self.Y = 0;