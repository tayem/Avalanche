import Player as P;
player1 = P.Player(450, 700, 70,70);
keys = [False,False,False,False, False];
level = 5;
def setup():
    frameRate(60);
    size(1000,800);
    smooth();
    colorMode(RGB,255,255,255);
    background(0,0,0);
    return None;
def draw():
    global level;
    background(0,0,0);
    global player1;
    if keys[0] == True:
        player1.move(0,4+level);
    if keys[1] == True:
        player1.move(0,-4-level);
    if keys[2] == True:
        player1.move(-4-level,0);
    if keys[3] == True:
        player1.move(4+level,0);
    player1.drawSelf();
    test = 2;
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