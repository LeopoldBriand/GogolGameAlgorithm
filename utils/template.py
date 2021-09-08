
class GogoleTemplate:
    def __init__(self, name):
        self.circles = []
        self.name = name

    def initCircles(self, card, config):
        i = 0
        for image in card:
            self.circles.append(GogoleObject(image, config[i]['radius'], config[i]['pos']))
            i+=1

class GogoleObject:
    def __init__(self, num, radius, pos):
        self.num = num
        self.radius = radius
        self.pos = pos

    def getRadius(self):
        return self.radius 
    
    def getPos(self):
        return (self.pos[0]-self.radius, self.pos[1]-self.radius)

    def returnCirclePositions(self):
        return (self.pos[0]-(self.radius), self.pos[1]-(self.radius), self.pos[0]+(self.radius), self.pos[1]+(self.radius))