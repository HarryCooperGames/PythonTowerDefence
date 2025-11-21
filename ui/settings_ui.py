from objects.user_interface.box import *
from objects.user_interface.text import *
from colours import *

#settings menu stuff
#settings boxes
settings_title = Box(WHITE,75,50,350,125, 10)
settings_back = Box(WHITE,100,400,300,75, 10)
volume_decrease = Box(WHITE, 100, 200, 125,75, 10)
volume_increase = Box(WHITE, 275, 200, 125,75, 10)
#settings text
settings_title_text = Text("Settings",BLACK,250,100,80)
settings_back_text = Text("Back",BLACK,250,430,50)
volume_decrease_text = Text("Volume -", BLACK, 163, 238, 32)
volume_increase_text = Text("Volume +", BLACK, 338, 238, 32)