from objects.user_interface.box import *
from objects.user_interface.text import *
from colours import *

#main game stuff
tower_selection_boxes = []
#tower selection boxes and outlines
tower_main_box = Box(BLUE,0,0,175,500, 10)
settings_main = Box(WHITE, 17.5 ,420, 62.5 ,40, 10)
money_box = Box(WHITE, 97.5, 420, 62.5, 40, 10)
wave_box = Box(WHITE, 375, 0, 50, 50, 10)
health_box = Box(WHITE, 425, 0, 75, 50, 10)
help_box = Box(WHITE, 97.5, 370, 62.5,40, 10)
#upgrade and sell boxes
upgrade_damage_box = Box(WHITE, 17.5 ,320, 62.5 ,40, 10)
upgrade_range_box = Box(WHITE, 17.5, 370, 62.5, 40, 10)
sell_box = Box(RED, 97.5, 320, 62.5, 40, 10)
#upgrade and sell text
upgrade_damage_text = Text("damage", BLACK, 45, 340, 12)
upgrade_range_text = Text("range", BLACK, 45, 390, 12)
sell_text = Text("Sell", BLACK, 125, 340, 12)
for i in range(0,3):
  tower_selection_boxes.append(Box(WHITE, 17.5, 20 + i * 100, 142.5, 75, 10))
#main game text for boxes
main_text_list = []
#list for each index
main_text = ["Rifle", "Sniper", "Shotgun"]
for i in range(0,3):
  main_text_list.append(Text(main_text[i], BLACK, 85, 40 + i * 100, 32))
settings_main_text = Text("Settings", BLACK, 45, 440, 12)
main_text_list.append(settings_main_text)
#help text
help_text = Text("HELP", BLACK, 125, 390, 12)
main_text_list.append(help_text)
#tower cost text
tower_cost_text = ["£50", "£150", "£300"]
for i in range(0,3):
  main_text_list.append(Text(tower_cost_text[i], BLACK, 85, 80 + i*100, 12))
#map and pathway boxes
map_background = Box(GREEN,175,0,500,500, 10)
map_border1 = Box(BLACK,0,0,500,-1, 10)
map_border2 = Box(BLACK,501,-1,1,501, 10)
map_border3 = Box(BLACK,0,501,501,1, 10)
path_list = []
#points that the enemies travel to and from
waypoints = [(250,0), (250,400), (350,400), (350,250), (400,250), (400,100), (550,100)]
path_1 = Box(YELLOW, waypoints[0][0]-10, waypoints[0][1], 20, waypoints[1][1]-waypoints[0][1], 10)
path_2 = Box(YELLOW, waypoints[1][0]-10, waypoints[1][1]-10, waypoints[2][0]-waypoints[1][0]+10, 20, 10)
path_3 = Box(YELLOW, waypoints[2][0]-10, waypoints[3][1], 20, waypoints[2][1]-waypoints[3][1]+10, 10)
path_4 = Box(YELLOW, waypoints[3][0]-10, waypoints[3][1]-10, waypoints[4][0]-waypoints[3][0]+10, 20, 10)
path_5 = Box(YELLOW, waypoints[4][0]-10, waypoints[5][1], 20, waypoints[4][1]-waypoints[5][1]+10, 10)
path_6 = Box(YELLOW, waypoints[5][0]-10, waypoints[5][1]-10, waypoints[6][0]-waypoints[5][0]+10, 20, 10)
path_list = path_list + [path_1] + [path_2] + [path_3] + [path_4] + [path_5] + [path_6]