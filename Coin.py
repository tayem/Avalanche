import PowerUp;
import random;
class Coin(PowerUp.PowerUp):
    def __init__(self):
        return None;
    def draw(self):
        locationX = random.randint(0,950);
        locationY = random.randint(100, 700);
        coin = loadImage("coin.png");
        image(coin, locationX, locationY, 70, 70);