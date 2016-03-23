# X1, Y1 is the top left corner, X2, Y2 is the top right corner, X3, Y3 is the bottom corner
import random;
class Spike():
    def __init__(self, Y, speed):
        self.X1 = random.randint(10,990);
        self.Y1= Y;
        self.X2 = self.X1 + 10;
        self.Y2 = self.Y1;
        self.X3 = self.X1 + 5;
        self.Y3 = self.Y1 + 45;
        self.speed = speed;
    def draw(self):
        fill(255,0,0);
        triangle(self.X1, self.Y1, self.X2, self.Y2, self.X3, self.Y3); 
        if self.Y1 > 800:
            newY = random.randint(-200, -50);
            self.Y1 = newY;
            self.Y2 = newY;
            self.Y3 = newY + 45;
        self.Y1 += self.speed;
        self.Y2 += self.speed;
        self.Y3 += self.speed;
        return None;
    def hitDetect(self, X, Y, player):
        if player.X < X < player.X+player.Width and player.Y < Y < player.Y+player.Height:
            return True;
        else:
            return False;