
class Player:
    def __init__(self, X, Y, keys):
        self.X = X;
        self.Y = Y;
        self.Width = 70;
        self.Height = 70;
        self.isHit = False;
        self.powers = [];
        self.speed = 5;
        self.keys = keys;
        self.numTrue = 0;
    def draw(self):
        if self.keys[0] == True:
            for i in self.keys:
                if i == True:
                    self.numTrue += 1;
            if self.numTrue > 1:
                self.speed = 3.5;
            else:
                self.speed = 5;
            self.move(0,self.speed);
        
        if self.keys[1] == True:
            for i in self.keys:
                if i == True:
                    self.numTrue += 1;
            if self.numTrue > 1:
                self.speed = 3.5;
            else:
                self.speed = 5;
            self.move(0,-self.speed);
        
        if self.keys[2] == True:
            for i in self.keys:
                if i == True:
                    self.numTrue += 1;
            if self.numTrue > 1:
                self.speed = 3.5;
            else:
                self.speed = 5;
            self.move(-self.speed,0);
        
        if self.keys[3] == True:
            for i in self.keys:
                if i == True:
                    self.numTrue += 1;
            if self.numTrue > 1:
                self.speed = 3.5;
            else:
                self.speed = 5;
            self.move(self.speed,0);
        fill(0,0,255);
        rect(self.X, self.Y, self.Width, self.Height);
    def move(self, dX, dY):
        self.X += dX;
        self.Y -= dY;
       