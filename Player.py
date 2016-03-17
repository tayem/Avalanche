class Player:
    def __init__(self, X, Y, Width, Height):
        self.X = X;
        self.Y = Y;
        self.Width = Width;
        self.Height = Height;
        self.isHit = False;
        self.powers = [];
    def drawSelf(self):
        rect(self.X, self.Y, self.Width, self.Height);
    def move(self, dX, dY):
        self.X += dX;
        self.Y -= dY;