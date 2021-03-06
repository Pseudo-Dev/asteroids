gridWidth = 3
gridHeight = 3

# All functions return a list of nodes in that direction

def up(node):
    result = []
    while node > 0:
        node -= gridWidth
        result.append(node)
    return result


def down(node):
    result = []
    while node <= gridWidth * gridHeight:
        node += gridWidth
        result.append(node)
    return result


def left(node):
    result = []
    edge = int((node-1) / gridWidth) * gridWidth
    while node > edge:
        node -= 1
        result.append(node)
    return result


def right(node):
    result = []
    edge = int((node-1) / gridWidth + 1) * gridWidth
    while node <= edge:
        node += 1
        result.append(node)
    return result
