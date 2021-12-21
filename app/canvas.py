from app.graphics import GraphWin, Text, Point

screenW = 4000
screenH = 3000
win = None


def init(my):
    global win
    win = GraphWin(my.ip, screenW/10, screenH/10, autoflush=False)
    win.setCoords(0, 0, screenW, screenH)
    nodeTxt = Text(Point(2000, 1500), my.id)
    nodeTxt.setTextColor("white")
    nodeTxt.setSize(36)
    nodeTxt.draw(win)
    return win
