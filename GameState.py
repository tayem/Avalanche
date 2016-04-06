import State;
import Player;
import Spike;
import random;
import time;
import Coin;
timer = 0;
class GameState(State.State):
    def __init__(self, keys, player):
        global spikes;
        global powerups;
        global coins;
        global coinAdded;
        coinAdded = False;
        spikes = [];
        powerups = [];
        coins = [];
        for i in range(20):
            spikes.append(Spike.Spike(i*-200, 5));
        return None;
    def draw(self, player):
        background(0,0,0);
        fill(255,255,255);
        rect(1000,0,200,800);
        fill(0,0,0);
        textSize(20);
        text("Lives: " + str(player.lives), 1005, 75);
        text("Points: " + str(player.points), 1005, 90 );
        for aSpike in spikes:
            detect1 = aSpike.hitDetect(aSpike.X1, aSpike.Y1, player);
            detect2 = aSpike.hitDetect(aSpike.X2, aSpike.Y2, player);
            detect3 = aSpike.hitDetect(aSpike.X3, aSpike.Y3, player);
            if detect1 or detect2 or detect3:
                player.lives -=1;
                print(player.lives);
                spikes.remove(aSpike);
                for aSpike in spikes:
                    aSpike.speed += 2;
            aSpike.draw();
        player.draw();
        if frameCount % 60 == 0:
            player.points += 1;
        if player.points % 6 == 0 and coinAdded == False:
            coins.append(Coin.Coin());
            coinAdded = True;
        for aCoin in coins:
            aCoin.draw();
        return None;