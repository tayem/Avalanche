import Player as P;
player1 = P.Player(450, 700, 70,70);
keys = [False,False,False,False, False];
level = 1;
def setup():
    frameRate(60);
    size(1000,800);
    smooth();
    colorMode(RGB,255,255,255);
    background(0,0,0);
    return None;
def draw():
    global level;
    numTrue = 0;
    background(0,0,0);
    global player1;
    
    if keys[0] == True:
        for i in keys:
            if i == True:
                numTrue += 1;
        if numTrue > 1:
            player1.speed = 2.5;
        else:
            player1.speed = 4;
        player1.move(0,player1.speed + level);
        
    if keys[1] == True:
        for i in keys:
            if i == True:
                numTrue += 1;
        if numTrue > 1:
            player1.speed = 2.5;
        else:
            player1.speed = 4;
        player1.move(0,-player1.speed - level);
        
    if keys[2] == True:
        for i in keys:
            if i == True:
                numTrue += 1;
        if numTrue > 1:
            player1.speed = 2.5;
        else:
            player1.speed = 4;
        player1.move(-player1.speed - level,0);
        
    if keys[3] == True:
        for i in keys:
            if i == True:
                numTrue += 1;
        if numTrue > 1:
            player1.speed = 2.5;
        else:
            player1.speed = 4;
        player1.move(player1.speed + level,0);
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