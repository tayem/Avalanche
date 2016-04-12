import State;
import Player;
class IntroState(State.State):
    def __init__(self, keys, backgroundSprite):
        self.backgroundSprite = backgroundSprite;
        return None;
    def draw(self, player):
        background(0,0,0);
        image(self.backgroundSprite, 5,5, 1190,790);
        textSize(40);
        text("Welcome to Trump Avalanche!", 300, 100);
    def moveToGame(self, keys):
        if keys[4] == True:
            return True;