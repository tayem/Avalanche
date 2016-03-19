class Bullet():
    def __init__(self, X, Y):
        self.X = X;
        self.Y = Y;
        self.Width = 2;
        self.Height = 4;
    def move(self):
        self.Y -= 5;
        
        