import State;
import Player;
import Spike;
import random;
class GameState(State.State):
    def __init__(self, keys):
        global player;
        player = Player.Player(450, 700, keys);
        global spikes;
        spikes = [];
        for i in range(20):
            spikes.append(Spike.Spike(i*-200, 5));
        return None;
    
    def draw(self):
        background(0,0,0);
        for aSpike in spikes:
            aSpike.draw();
        player.draw();
        return None;