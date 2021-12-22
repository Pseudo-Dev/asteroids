from remote.client import peerDict


gridW = 1
gridH = 3


def up(node):
    result = []
    while node > 0:
        node -= gridW
        if node in peerDict:
            result.append(node)
    return result


def down(node):
    result = []
    while node <= gridW * gridH:
        node += gridW
        if node in peerDict:
            result.append(node)
    return result


def left(node):
    result = []
    edge = int((node-1) / gridW) * gridW
    while node > edge:
        node -= 1
        if node in peerDict:
            result.append(node)
    return result


def right(node):
    result = []
    edge = int((node-1) / gridW + 1) * gridW
    while node <= edge:
        node += 1
        if node in peerDict:
            result.append(node)
    return result
