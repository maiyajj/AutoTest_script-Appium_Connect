import os

command = "title 123"
command1 = "pause"
print os.popen(command).read()
print os.popen(command1).read()
