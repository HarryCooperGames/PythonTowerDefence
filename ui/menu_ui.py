from objects.user_interface.box import *
from objects.user_interface.text import *
from colours import *
#menu title box defined
menu_title_box = Box(WHITE,75,50,350,125, 10)
#menu button list to add all the boxes too
menu_button_list = []
#for loop to append the different main menu boxes to the list
for i in range(0,3):
  menu_button_list.append(Box(WHITE, 100, 200 + i * 100, 300, 75, 10))
#title text
menu_title_text = Text("Title",BLACK,250,125,100)
#text list
menu_text_list = []
#list of the text for each index of the text list
menu_text = ["Play", "Settings", "Exit"]
#for loop to add each piece of text to the text list
for i in range(0,3):
  menu_text_list.append(Text(menu_text[i], BLACK, 250, 237.5 + i * 100, 50))