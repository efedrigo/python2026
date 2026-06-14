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

print("m=[")
while (myRobot.getTime()<15):
    t = myRobot.getTime();
    x = myRobot.getEncoderL();
    y = myRobot.getEncoderR();

    print(t,",",x,",",y,";");
print("];")
