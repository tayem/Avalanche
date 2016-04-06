class PowerUp:
    def __init__(self, X, Y, Width, Height):
        self.X = X;
        self.Y = Y;
        self.Width = Width;
        self.Height = Height;
    def draw():
        ellipseMode(CORNER);
        fill(255,0,0);
        ellipse(self.X, self.Y, self.Width, self.Height);
    def hitDetect(self, player):
        if player.X < self.X < player.X+player.Width and player.Y < self.Y < player.Y+player.Height:
            return True;
        else:
            return False;