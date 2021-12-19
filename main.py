import asyncio
from syslog import syslog, openlog
from graphics import GraphWin, asyncUpdate
from asteroid import Asteroid
from remote.server import serve
from remote.client import send, get_ip

screenW = 4000
screenH = 3000
win = GraphWin("Node 1", screenW/10, screenH/10, autoflush=False)
win.setCoords(0, 0, screenW, screenH)
list = []
openlog("asteroids")
serve()


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
                # send()

        if win.checkMouse():
            break

        await asyncUpdate(10)  # Frames per second

print("######## IP #########")
print(get_ip())

asyncio.run(main())
