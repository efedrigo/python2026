
class robot:
    t=0;
    scale = 200;
    interval = 0.01;
    period = 0;

    def __init__(self):
        self.t=0;
        self.period = 1/self.interval;

    def getTime(self):
        self.t=self.t+self.interval;
        return self.t;

    def getEncoderL(self):
        return (int(round(((self.t*self.period)%self.scale)/self.scale*360)))
    
    def getEncoderR(self):
        return (int(round(((self.t*self.period)%self.scale)/self.scale*(-360))))
    