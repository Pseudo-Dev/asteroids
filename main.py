import asyncio
import syslog

from app.graphics import asyncUpdate
from app.asteroid import Asteroid, asteroidList
from app.canvas import init, screenW, screenH
from remote.server import serve
from remote.client import send, get_id, discovery


# Initialize app
my = get_id()
canvas = init(my)
syslog.openlog("asteroids")
server = serve(my, asteroidList, canvas)
asyncio.run(discovery(my))


async def main():
    while True:
        if len(asteroidList) < 6:
            asteroidList.append(Asteroid())

        for asteroid in asteroidList:
            if asteroid.new:
                asteroid.circle.draw(canvas)
                asteroid.new = False
            asteroid.circle.move(asteroid.dX, asteroid.dY)
            x = asteroid.circle.getCenter().getX()
            y = asteroid.circle.getCenter().getY()
            if x <= 0 or y <=0 or x >= screenW or y >= screenH:
                asteroid.circle.undraw()
                asteroidList.remove(asteroid)
                syslog.syslog("Asteroid moved out of bounds")
                if my.id == 1 and x >= screenW:
                    asteroid.circle.move(-screenW, 0)
                    asyncio.create_task(send(asteroid, 2))
                if my.id == 2 and x <= 0:
                    asteroid.circle.move(screenW, 0)
                    asyncio.create_task(send(asteroid, 1))

        if canvas.checkMouse():
            break

        await asyncUpdate(10)  # Frames per second


asyncio.run(main())
