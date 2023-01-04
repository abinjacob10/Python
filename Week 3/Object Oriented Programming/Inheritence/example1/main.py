'''Main program calls other classes' methods.
   This program aims to show how  classes could be used.
'''

from devices import switches
from devices import routers

switch1 = switches("HPE")
print(switch1.CRC_calc('garbage'))

router1 = routers("HPE MSR")
print(router1.CRC_calc('garbage'))
