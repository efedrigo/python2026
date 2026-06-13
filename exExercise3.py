import math

from exRobot import robot

myRobot = robot();

D=100;
wheelD = 44.3;
wheelC = wheelD * math.pi;

x      = 0;
y      = 0;
x_prev = 0;
y_prev = 0;
loopX  = 0;
loopY  = 0;

while (myRobot.getTime()<15):
    t = myRobot.getTime();
    x = myRobot.getEncoderL() * wheelC / 360;
    y = myRobot.getEncoderR() * wheelC / 360;

    if (abs(x-x_prev)>wheelC/2):
        if (x<x_prev):
            loopX = loopX + 1;
        else:
            loopX = loopX - 1;

    x_prev = x;

    if (abs(y-y_prev)>wheelC/2):
        if (y<y_prev):
            loopY = loopY + 1;
        else:
            loopY = loopY - 1;
        
    y_prev = y;

    y_prev = y;

print(x,y,loopX,loopY)
print(x+wheelC*loopX,y+wheelC*loopY);