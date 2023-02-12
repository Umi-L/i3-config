import sys
import subprocess
import json
import DisplayTools as tools

from screeninfo import get_monitors

MONITOR_OFFSET = 10

monitors = get_monitors()

currentDisplay = tools.getCurrentMouseDisplay(monitors)

index = (monitors.index(currentDisplay) * MONITOR_OFFSET) + int(sys.argv[1])

print(index)

command = ["i3-msg", "workspace", str(index)]

subprocess.call(command)