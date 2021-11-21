from graphics import *
import time
import random
import json

def n1():
    coordinates = {
        "c1" : [200+random.randint(30, 50), 150+random.randint(30, 50)],
        "c2" : [200-random.randint(30, 50), 150-random.randint(30, 50)],
        "c3" : [200+random.randint(30, 50), 150+random.randint(30, 50)],
        "c4" : [200-random.randint(30, 50), 150-random.randint(30, 50)],
        "c5" : [200+random.randint(30, 50), 150+random.randint(30, 50)],
        "c6" : [200-random.randint(30, 50), 150-random.randint(30, 50)],
        "c7" : [200+random.randint(30, 50), 150+random.randint(30, 50)],
        "c8" : [200-random.randint(30, 50), 150-random.randint(30, 50)]
    }
    screenW = 300
    screenH = 400
    win = GraphWin("Node 1", screenH, screenW)
    c1 = Circle(Point((coordinates["c1"])[0], (coordinates["c1"])[1]), 5)
    c1.draw(win)
    c2 = Circle(Point((coordinates["c2"])[0], (coordinates["c2"])[1]), 5)
    c2.draw(win)
    c3 = Circle(Point((coordinates["c3"])[0], (coordinates["c3"])[1]), 5)
    c3.draw(win)
    c4 = Circle(Point((coordinates["c4"])[0], (coordinates["c4"])[1]), 5)
    c4.draw(win)
    c5 = Circle(Point((coordinates["c5"])[0], (coordinates["c5"])[1]), 5)
    c5.draw(win)
    c6 = Circle(Point((coordinates["c6"])[0], (coordinates["c6"])[1]), 5)
    c6.draw(win)
    c7 = Circle(Point((coordinates["c7"])[0], (coordinates["c7"])[1]), 5)
    c7.draw(win)
    c8 = Circle(Point((coordinates["c8"])[0], (coordinates["c8"])[1]), 5)
    c8.draw(win)
    with open('n1.json', 'w') as file:
        file.write(json.dumps(coordinates))
    weightList = [1, -1]
    for i in range(1,2000000000000000):
        c1.move(random.choice(weightList), random.choice(weightList))
        c2.move(random.choice(weightList), random.choice(weightList))
        c3.move(random.choice(weightList), random.choice(weightList))
        c4.move(random.choice(weightList), random.choice(weightList))
        c5.move(random.choice(weightList), random.choice(weightList))
        c6.move(random.choice(weightList), random.choice(weightList))
        c7.move(random.choice(weightList), random.choice(weightList))
        c8.move(random.choice(weightList), random.choice(weightList))

n1()