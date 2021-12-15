from syslog import syslog, openlog
from graphics import GraphWin, update
from asteroid import Asteroid

screenW = 4000
screenH = 3000
win = GraphWin("Node 1", screenW/10, screenH/10, autoflush=False)
win.setCoords(0, 0, screenW, screenH)
list = []
openlog("asteroids")

while True:
    if len(list) < 7:
        new = Asteroid()
        list.append(new)
        new.circle.draw(win)

    for asteroid in list:
        asteroid.circle.move(asteroid.dX, asteroid.dY)
        x = asteroid.circle.getCenter().getX()
        y = asteroid.circle.getCenter().getY()
        if x <= 0 or y <=0 or x >= screenW or y >= screenH:
            asteroid.circle.undraw()
            list.remove(asteroid)
            syslog("Asteroid moved out of bounds")

    if win.checkMouse():
        break

    update(10)  # Frames per second
