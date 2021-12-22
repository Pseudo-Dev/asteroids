import asyncio
import syslog

from app.graphics import asyncUpdate
from app.asteroid import Asteroid, asteroidList
from app.canvas import init, screenW, screenH
from app.direction import up, down, left, right
from remote.server import serve
from remote.client import send, get_id, discovery


# Initialize app
me = get_id()
canvas = init(me)
syslog.openlog("asteroids")
server = serve(me, asteroidList)
asyncio.run(discovery(me))


async def main():
    while True:
        if len(asteroidList) < 5:   # Add more asteroids
            asteroidList.append(Asteroid())

        for asteroid in asteroidList:
            if asteroid.new:        # New asteroids must be drawn
                asteroid.circle.draw(canvas)
                asteroid.new = False

            asteroid.circle.move(asteroid.dX, asteroid.dY)

            # Check if out of bounds
            x = asteroid.circle.getCenter().getX()
            y = asteroid.circle.getCenter().getY()
            if x < 0:
                asteroid.circle.undraw()
                asteroidList.remove(asteroid)
                asteroid.circle.move(screenW, 0)
                asyncio.create_task(send(asteroid, left(me.id)))
            elif y < 0:
                asteroid.circle.undraw()
                asteroidList.remove(asteroid)
                asteroid.circle.move(0, screenH)
                asyncio.create_task(send(asteroid, down(me.id)))
            elif x > screenW:
                asteroid.circle.undraw()
                asteroidList.remove(asteroid)
                asteroid.circle.move(-screenW, 0)
                asyncio.create_task(send(asteroid, right(me.id)))
            elif y > screenH:
                asteroid.circle.undraw()
                asteroidList.remove(asteroid)
                asteroid.circle.move(0, -screenH)
                asyncio.create_task(send(asteroid, up(me.id)))

        # Stop if mouse is pressed
        if canvas.checkMouse():
            break

        await asyncUpdate(10)  # Frames per second


asyncio.run(main())
