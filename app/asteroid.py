from random import randint

from .graphics import Circle, Point


color = ("white", "yellow", "red", "blue", "green", "black", "cyan", "purple")
asteroidList = []


class Asteroid:
    def __init__(self, X=0, Y=0, dX=0, dY=0, size=0, clr=0):
        self.new = True
        if dX or dY:    # This is coming from another node
            self.dX = dX
            self.dY = dY
            self.size = size
            self.color = clr
        else:           # New asteroid instance
            self.dX = randint(-50, 50)
            self.dY = randint(-50, 50)
            self.size = randint(50, 200)
            self.color = randint(0, 7)
            X = 200 + randint(0, 3600)
            Y = 200 + randint(0, 2600)
        self.circle = Circle(Point(X, Y), self.size)
        self.circle.setFill(color[self.color])
        if self.color >= 2:
            self.circle.setOutline(color[self.color])
