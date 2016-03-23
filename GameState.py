import State;
import Player;
import Spike;
import random;
import time;
timer = 0;
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
        fill(255,255,255);
        rect(1000,0,200,800);
        for aSpike in spikes:
            detect1 = aSpike.hitDetect(aSpike.X1, aSpike.Y1, player);
            detect2 = aSpike.hitDetect(aSpike.X2, aSpike.Y2, player);
            detect3 = aSpike.hitDetect(aSpike.X3, aSpike.Y3, player);
            if detect1 or detect2 or detect3:
                player.lives -=1;
                print(player.lives);
                spikes.remove(aSpike);
            aSpike.draw();
        player.draw();
        return None;