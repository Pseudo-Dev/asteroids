from graphics import GraphWin, update
from asteroid import Asteroid

screenW = 400
screenH = 300
win = GraphWin("Node 1", screenW, screenH, autoflush=False)
win.setCoords(0, 0, screenW*10, screenH*10)
list = []

while True:
    if len(list) < 7:
        new = Asteroid()
        list.append(new)
        new.circle.draw(win)

    for asteroid in list:
        asteroid.circle.move(asteroid.dX, asteroid.dY)
        x = asteroid.circle.getCenter().getX()
        y = asteroid.circle.getCenter().getY()
        if x <= 0 or y <=0 or x >= screenW * 10 or y >= screenH * 10:
            asteroid.circle.undraw()
            list.remove(asteroid)

    if win.checkMouse():
        break

    update(10)  # Frames per second
