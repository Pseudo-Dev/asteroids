import asyncio
from syslog import syslog, openlog
from graphics import GraphWin, Text, Point, asyncUpdate
from asteroid import Asteroid
from remote.server import serve
from remote.client import send, get_id

# Set up graphics canvas
screenW = 4000
screenH = 3000
nodeID = get_id()
win = GraphWin(f'Node {nodeID}', screenW/10, screenH/10, autoflush=False)
win.setCoords(0, 0, screenW, screenH)
nodeTxt = Text(Point(2000, 1500), nodeID)
nodeTxt.setTextColor("white")
nodeTxt.setSize(36)
nodeTxt.draw(win)

# Initialize app
list = []
openlog("asteroids")
server = serve()


async def main():
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
                if nodeID == 1 and x >= screenW:
                    print("####### Oikealle")
                    asyncio.create_task(send(asteroid, 2))
                if nodeID == 2 and x <= 0:
                    print("####### Vasemmalle")
                    asyncio.create_task(send(asteroid, 1))

        if win.checkMouse():
            break

        await asyncUpdate(10)  # Frames per second


asyncio.run(main())
