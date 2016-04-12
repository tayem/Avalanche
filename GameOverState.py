import State;
import Player;
class GameOverState(State.State):
    def __init__(self, keys, player):
        return None;
    def draw(self, player):
        background(0,0,0);
        fill(255,255,255);
        rect(400,400, 200,100);
        fill(0,0,0);
        text("You lost!", 405, 450);