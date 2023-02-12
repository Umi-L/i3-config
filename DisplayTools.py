from screeninfo import get_monitors
from Xlib import display
import subprocess
import json


def getCurrentMouseDisplay(monitors):

    pointerData = display.Display().screen().root.query_pointer()._data
    mousePos = (pointerData["root_x"], pointerData["root_y"])

    for monitor in monitors:

        if pointInRect(mousePos, (monitor.x, monitor.y, monitor.width, monitor.height)):
            return monitor


def pointInRect(point,rect):
    x1, y1, w, h = rect
    x2, y2 = x1+w, y1+h
    x, y = point
    if (x1 < x and x < x2):
        if (y1 < y and y < y2):
            return True
    return False

def getActiveWorkspaceNumber():
    command = ["i3-msg", "-t", "get_workspaces"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    workspaces = json.loads(result.stdout)

    for workspace in workspaces:
        if workspace["focused"]:
            return workspace["num"]