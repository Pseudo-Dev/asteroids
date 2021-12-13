from graphics import GraphWin, update
from asteroid import Asteroid

screenW = 400
screenH = 300
win = GraphWin("Node 1", screenW, screenH, autoflush=False)
win.setCoords(0, 0, screenW*10, screenH*10)
list = []

for i in range(6):
    asteroid = Asteroid()
    list.append(asteroid)
    asteroid.circle.draw(win)

while True:
    for asteroid in list:
        asteroid.circle.move(asteroid.dX, asteroid.dY)

    if win.checkMouse():
        break

    update(10)  # Frames per second
