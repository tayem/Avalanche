import PowerUp;
import random;
class Coin(PowerUp.PowerUp):
    def __init__(self, sprite):
        self.X = random.randint(0,950);
        self.Y = random.randint(100, 700);
        self.sprite = sprite;
        return None;
    def draw(self):
        image(self.sprite, self.X, self.Y, 70, 70);
    def hitDetect(self, X, Y, player):
        if player.X < X < player.X+player.Width and player.Y < Y < player.Y+player.Height:
            return True;
        else:
            return False;