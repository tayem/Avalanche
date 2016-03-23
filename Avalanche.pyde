import State;
keys = [False,False,False,False, False];
import GameState;
currentState = GameState.GameState(keys);
def setup():
    frameRate(60);
    size(1200,800);
    smooth();
    colorMode(RGB,255,255,255);
    background(0,0,0);
    return None;

def draw():
    currentState.draw();
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
    if keyCode == BACKSPACE:
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
    if keyCode == BACKSPACE:
        keys[4] = False;
    return None;