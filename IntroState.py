import State;
import Player;
class IntroState(State.State):
    def __init__(self, keys):
        return None;
    def draw(self, player):
        background(0,0,0);
        fill(255,255,255);
        rect(5,5, 1190,790);
        fill(0,0,0);
        textSize(40);
        text("Welcome to Trump Avalanche!", 300, 100);
    def moveToGame(self, keys):
        if keys[4] == True:
            return True;