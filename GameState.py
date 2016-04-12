import State;
import Player;
import Spike;
import random;
import time;
import Coin;
class GameState(State.State):
    def __init__(self, keys, player, coins, coinSprite):
        global spikes;
        global powerups;
        self.coins = coins;
        self.coinSprite = coinSprite;
        self.coinAdded = False;
        self.timer = 1;
        spikes = [];
        powerups = [];
        for i in range(15):
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
            self.timer += 1;
            player.points += 1;
            for aSpike in spikes:
                aSpike.speed += 0.3;
        
        for aCoin in self.coins:
            detect1 = aCoin.hitDetect(aCoin.X, aCoin.Y, player);
            detect2 = aCoin.hitDetect(aCoin.X+70, aCoin.Y, player);
            detect3 = aCoin.hitDetect(aCoin.X, aCoin.Y+70, player);
            detect4 = aCoin.hitDetect(aCoin.X+70, aCoin.Y+70, player);
            if detect1 or detect2 or detect3 or detect4:
                player.points += 10;
                self.coins.remove(aCoin);
                self.coins.append(Coin.Coin(self.coinSprite));
        if player.points % 5 == 0:
            for aCoin in self.coins:
                aCoin.draw();
        return None;