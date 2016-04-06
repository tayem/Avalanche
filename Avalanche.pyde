import State;
keys = [False,False,False,False, False];
import GameState;
import GameOverState;
import IntroState;
import TrumpState;
currentState = 0;
import Player;
player = Player.Player(450, 700, keys);
stateList = [IntroState.IntroState(keys), GameState.GameState(keys,player), GameOverState.GameOverState(keys,player), TrumpState.TrumpState(keys,player)];

def setup():
    frameRate(60);
    size(1200,800);
    smooth();
    colorMode(RGB,255,255,255);
    background(0,0,0);
    return None;

def draw():
    global player;
    global stateList;
    currentState = stateList[checkState(player)];
    if currentState == stateList[0]:
        if currentState.moveToGame(keys) == True:
            currentState = stateList[1];
    currentState.draw(player);
    return None;

def keyPressed():
    if keyCode == UP:
        keys[0] = True;
    if keyCode == DOWN:
        keys[1] = True;
    if keyCode == LEFT:
        keys[2] = True;
    if keyCode == RIGHT:
        keys[3] = True;
    if key == " ":
        keys[4] = True;
    return None;

def keyReleased():
    if keyCode == UP:
        keys[0] = False;
    if keyCode == DOWN:
        keys[1] = False;
    if keyCode == LEFT:
        keys[2] = False;
    if keyCode == RIGHT:
        keys[3] = False;
    if key == " ":
        keys[4] = False;
    return None;

def checkState(player):
    if player.points == 1:
        return 0;
    elif player.lives > 0:
        return 1;
    elif player.lives == 0:
        return 2;
    elif player.points > 100:
        return 3;