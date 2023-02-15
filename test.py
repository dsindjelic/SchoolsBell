import time
# you can use subprocess to exec commands
from subprocess import call
command = "sudo  /usr/bin/hidusb-relay-cmd on ALL".split()

time.sleep(3)
call(command)

time.sleep(5)
command = "sudo  /usr/bin/hidusb-relay-cmd off ALL".split()
call(command)
