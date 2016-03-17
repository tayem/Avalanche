import Player as P;
def setup():
    
    fullScreen();
    colorMode(RGB,255,255,255);
    background(0,0,0);
    player1 = P.Player(displayWidth/2, displayHeight/1.03, 100,100);
    return None;
def draw():
    
    player1.Draw();
    return None;

def keyPressed():

    return None;
        