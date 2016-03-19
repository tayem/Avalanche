import random;
class Spike():
    def __init__(self, Y, speed):
        self.X = random.randint(10,990);
        self.Y = Y;
        self.Width = 20;
        self.Height = 50;
        self.speed = speed;
    def draw(self):
        fill(255,0,0);
        rect(self.X, self.Y, self.Width, self.Height);
        if self.Y > 800:
            self.Y = random.randint(-200, -50);
        self.Y += self.speed;
        
        return None;