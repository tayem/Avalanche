class PowerUp:
    def __init__(self, X, Y, Width, Height):
        self.X = X;
        self.Y = Y;
        self.Width = Width;
        self.Height = Height;
        
    def drawSelf:
        ellipseMode(CORNER);
        ellipse(self.X, self.Y, self.Width, self.Height);