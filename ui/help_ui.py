from objects.user_interface.box import *
from objects.user_interface.text import *
from colours import *

#help menu stuff
help_title = Box(WHITE,75,50,350,125, 10)
help_title_text = Text("Help",WHITE,250,100,80)
help_back = Box(WHITE,100,400,300,75, 10)
help_back_text = Text("Back",WHITE,250,430,50)
#help menu help text
help_text1 = Text("Towers cannot be placed on top of one another or the enemies path or buttons",BLACK,250,200,12)
help_text2 = Text("When one wave is defeated the next wave begins immediately", BLACK, 250, 220, 12)
help_text3 = Text("Rifle tower: medium range and medium damage", BLACK, 250, 240, 12)
help_text4 = Text("Sniper tower: large range and low damage", BLACK, 250, 260, 12)
help_text5 = Text("Shotgun tower: low range and high damage", BLACK, 250, 280, 12)
help_text6 = Text("tower buttons must be clicked to select a tower then clicked to place", BLACK, 250, 300, 12)
help_text7 = Text("tower can then be clicked to select and upgrade/sell", BLACK, 250, 320, 12)
help_text8 = Text("any tower placed can be upgraded up to 5 times costing 100 per upgrade", BLACK, 250, 340, 12)
help_text_list = [help_text1] + [help_text2] + [help_text3] + [help_text4] + [help_text5] + [help_text6] + [help_text7] + [help_text8]