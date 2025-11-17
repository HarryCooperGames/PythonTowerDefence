#import pygame and other modules
import sys
import pygame
from pygame import *
import math
from pygame import mixer
from objects import *
from colours import *
#initialise pygame
pygame.init()
#initialise music mixer
mixer.init()
#volume variable
volume = 0.5
#music for main game
#mixer.music.load("main_game_song.MP3")
mixer.music.set_volume(volume)
#mixer.music.play(-1)
#define screen
clock = pygame.time.Clock()
clock.tick(30)
screen = pygame.display.set_mode((500, 500))
#points that the enemies travel to and from
waypoints = [(250,0), (250,400), (350,400), (350,250), (400,250), (400,100), (550,100)]
#used to check the previous game state so that when back button is pressed the correct screen loads
backtrack = 0
#money variable tracks players money
money = 100
#keeps track of the wave number
wave_num = 0
#tracks the players health
player_health = 100
#enemy class
class Enemy():
  #index used to track enemies position in list
  def __init__(self,waypoints,image,speed,health,money_value,damage):
    #add waypoint list to enemy class
    self.waypoints = waypoints
    #the first position of the enemy will be the first waypoint
    self.pos = Vector2(self.waypoints[0])
    #chooses the next waypoint it needs to go to
    self.target_waypoint = 1
    self.image = image
    self.rect = image.get_rect()
    self.rect.center = self.pos
    self.x = float(self.rect.x)
    self.speed = speed
    self.health = health
    self.money_value = money_value
    self.damage = damage
  def move(self):
    self.health_check()
    #defines the nextwaypoint the enemy will go to
    self.target = Vector2(self.waypoints[self.target_waypoint])
    #calculates displacement from the next waypoint
    self.movement = self.target - self.pos
    #calculate remaining distance to target
    distance = self.movement.length()
    #check if distance is greater the how much the enemy will move
    if distance >= self.speed:
      #move the enemy towards the next waypoint
      self.pos += self.movement.normalize() * self.speed
    else:
      if distance != 0:
        self.pos += self.movement.normalize() * distance
      if len(waypoints)-1 > self.target_waypoint:
        self.target_waypoint += 1
    #update the center to the position that is being moved
    self.rect.center = self.pos
    self.draw()
  def draw(self):
    screen.blit(self.image,(self.rect.x,self.rect.y))
  #checks if the enemy is still alive
  def health_check(self):
    global player_health, money
    if self.health <= 0:
      enemy_group.remove(self)
      money += self.money_value
    if self.pos == waypoints[len(waypoints)-1]:
      enemy_group.remove(self)
      player_health -= self.damage
#tower class
class Tower():
  def __init__(self,x,y,x2,y2,colour,range,damage,cost):
    self.x = x 
    self.y = y
    self.x2 = x2
    self.y2 = y2
    self.colour = colour
    self.rect = pygame.Rect((x,y,x2,y2))
    self.range = range
    self.hitbox = pygame.Rect((x-self.range, y-self.range, x2+2*self.range, y2+2*self.range))
    self.damage = damage
    #checks which enemy the tower will attack
    self.target = None
    #checks if the tower is selected
    self.selected = False
    #checks how many upgrades the tower has
    self.upgrade_count = 0
    #checks the initial cost of the tower which can be increased by upgrades
    self.cost = cost
  #draws tower on screen
  def draw_tower(self):
    global money
    if (self.rect.colliderect(path_1.rect)or self.rect.colliderect(path_2.rect) or self.rect.colliderect(path_3.rect)
        or self.rect.colliderect(path_4.rect) or self.rect.colliderect(path_5.rect) or self.rect.colliderect(path_6.rect)
        or self.rect.colliderect(tower_main_box) or self.rect.colliderect(wave_box.rect)
        or self.rect.colliderect(health_box.rect) or self.rect.colliderect(map_border1) or self.rect.colliderect(map_border2)
        or self.rect.colliderect(map_border3)):
      print("error")
      tower_group.remove(self)
      money += self.cost
    for tower in tower_group:
      if self != tower:
        if self.rect.colliderect(tower):
          tower_group.remove(tower)
          money += self.cost
    pygame.draw.rect(screen, self.colour, (self.x, self.y, self.x2, self.y2))
  #checks if an enemy collides with the towers hitbox
  def hitbox_check(self):
    for enemy in enemy_group:
      if enemy.rect.colliderect(self.hitbox) and enemy == self.target_enemy():
        self.target_enemy().health -= self.damage
  #targets one enemy that is closest to the tower
  def target_enemy(self):
    x = self.rect.center[0]
    y = self.rect.center[1]
    dist_list = []
    for enemy in enemy_group:
      x_dist = enemy.pos[0]- x
      y_dist = enemy.pos[1]- y
      #finds the enemies distance from the tower
      dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
      dist_list.append(dist)
      if dist == min(dist_list):
        if enemy.rect.colliderect(self.hitbox):
          return enemy
        else:
          dist_list = []
  def select_check(self):
    #draws the text and boxes for upgrades and sell
    upgrade_damage_box.draw(screen)
    upgrade_range_box.draw(screen)
    sell_box.draw(screen)
    upgrade_damage_text.draw_text(screen)
    upgrade_range_text.draw_text(screen)
    sell_text.draw_text(screen)
#functions to make tower follow mouse until placed
def place_tower1():
  if placing_tower1 == True:
      pygame.draw.rect(screen, MAGENTA, (mouse_pos[0]-20, mouse_pos[1]-20, 40, 40,))
def place_tower2():
  if placing_tower2 == True:
    pygame.draw.rect(screen, CYAN, (mouse_pos[0]-20, mouse_pos[1]-20, 40, 40))
def place_tower3():
  if placing_tower3 == True:
    pygame.draw.rect(screen, RED, (mouse_pos[0]-20, mouse_pos[1]-20, 40, 40))
#list used to store all towers
tower_group = []
#load images/sprites
red_enemy_image = pygame.image.load("Red_Balloon.webp").convert_alpha()
red_enemy_image = pygame.transform.scale(red_enemy_image,(20,20))
blue_enemy_image = pygame.image.load("Blue_Balloon.webp").convert_alpha()
blue_enemy_image = pygame.transform.scale(blue_enemy_image,(20,20))
green_enemy_image = pygame.image.load("Green_Balloon.webp").convert_alpha()
green_enemy_image = pygame.transform.scale(green_enemy_image,(20,20))
#enemy group to add enemies to and display it
enemy_group = []
#main menu stuff
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
path_1 = Box(YELLOW, waypoints[0][0]-10, waypoints[0][1], 20, waypoints[1][1]-waypoints[0][1], 10)
path_2 = Box(YELLOW, waypoints[1][0]-10, waypoints[1][1]-10, waypoints[2][0]-waypoints[1][0]+10, 20, 10)
path_3 = Box(YELLOW, waypoints[2][0]-10, waypoints[3][1], 20, waypoints[2][1]-waypoints[3][1]+10, 10)
path_4 = Box(YELLOW, waypoints[3][0]-10, waypoints[3][1]-10, waypoints[4][0]-waypoints[3][0]+10, 20, 10)
path_5 = Box(YELLOW, waypoints[4][0]-10, waypoints[5][1], 20, waypoints[4][1]-waypoints[5][1]+10, 10)
path_6 = Box(YELLOW, waypoints[5][0]-10, waypoints[5][1]-10, waypoints[6][0]-waypoints[5][0]+10, 20, 10)
path_list = path_list + [path_1] + [path_2] + [path_3] + [path_4] + [path_5] + [path_6]
#variables to check if the user is placing towers
placing_tower1 = False
placing_tower2 = False
placing_tower3 = False
#variables to check time for the last spawn and how many enemies so far
last_red_spawn = 0
last_blue_spawn = 0
last_green_spawn = 0
count = 0
#function to spawn a red enemy
def spawn_red_enemy():
  global last_red_spawn,count
  #checks the time since the last enemy spawned
  if pygame.time.get_ticks() - last_red_spawn > 300:
    enemy_group.append(Enemy(waypoints, red_enemy_image, 2, 20, 10,1))
    #sets the time the last enemy spawned to the current time
    last_red_spawn = pygame.time.get_ticks()
    count+=1
#function to spawn a blue enemy
def spawn_blue_enemy():
  global last_blue_spawn,count
  if pygame.time.get_ticks() - last_blue_spawn > 300:
    enemy_group.append(Enemy(waypoints, blue_enemy_image, 4, 25, 20,2))
    last_blue_spawn = pygame.time.get_ticks()
    count+=1
#function to spawn a green enemy
def spawn_green_enemy():
  global last_green_spawn,count
  if pygame.time.get_ticks() - last_green_spawn > 300:
    enemy_group.append(Enemy(waypoints, green_enemy_image, 3, 100, 50,5))
    last_green_spawn = pygame.time.get_ticks()
    count+=1
#function to create a wave of enemies
wave_num = 1
def wave():
  global wave_num, count, enemy_group
  #spawns 10 red enemies
  if wave_num == 1 and count < 10:
    spawn_red_enemy()
  if wave_num == 1 and count == 10 and not enemy_group:
      wave_num = 2
  #spawns 15 red enemies
  if wave_num == 2 and count < 25:
    spawn_red_enemy()
  if wave_num == 2 and count == 25 and not enemy_group:
    wave_num = 3
  if wave_num == 3 and count < 50:
    spawn_red_enemy()
  if wave_num == 3 and count == 50 and not enemy_group:
    wave_num = 4
  if wave_num == 4 and count < 60:
    spawn_blue_enemy()
  if wave_num == 4 and count == 60 and not enemy_group:
    wave_num = 5
  if wave_num == 5 and count < 75:
    spawn_blue_enemy()
  if wave_num == 5 and count == 75 and not enemy_group:
    wave_num = 6
  if wave_num == 6 and count < 105:
    spawn_red_enemy()
    spawn_blue_enemy()
  if wave_num == 6 and count == 105 and not enemy_group:
    wave_num = 7
  if wave_num == 7 and count < 110:
    spawn_green_enemy()
  if wave_num == 7 and count == 110 and not enemy_group:
    wave_num = 8
  if wave_num == 8 and count < 120:
    spawn_green_enemy()
  if wave_num == 8 and count == 120 and not enemy_group:
    wave_num = 9
  if wave_num == 9 and count < 150:
    spawn_red_enemy()
    spawn_blue_enemy()
    spawn_green_enemy()
  if wave_num == 9 and count == 150 and not enemy_group:
    wave_num = 10
  if wave_num == 10 and count < 210:
    spawn_red_enemy()
    spawn_blue_enemy()
    spawn_green_enemy()
  if wave_num == 10 and count == 210 and not enemy_group:
    wave_num = 11
    
#state variable to change game state
state = "Main menu"
#settings menu function
def Settings():
  global volume
  #background
  screen.fill(BLUE)
  #drawing boxes
  settings_title.draw(screen)
  settings_back.draw(screen)
  volume_decrease.draw(screen)
  volume_increase.draw(screen)
  #drawing text
  settings_title_text.draw_text(screen)
  settings_back_text.draw_text(screen)
  volume_decrease_text.draw_text(screen)
  volume_increase_text.draw_text(screen)
  #button colour change
  if settings_back.rect.colliderect(mouse_rect):
    settings_back.colour = RED
  if not settings_back.rect.colliderect(mouse_rect):
    settings_back.colour = WHITE
  if volume_decrease.rect.colliderect(mouse_rect):
    volume_decrease.colour = RED
  if not volume_decrease.rect.colliderect(mouse_rect):
    volume_decrease.colour = WHITE
  if volume_increase.rect.colliderect(mouse_rect):
    volume_increase.colour = RED
  if not volume_increase.rect.colliderect(mouse_rect):
    volume_increase.colour = WHITE
  #button collision
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        if volume_decrease.rect.collidepoint(event.pos):
          if volume > 0:
            volume -= 0.25
            mixer.music.set_volume(volume)
        if volume_increase.rect.collidepoint(event.pos):
          if volume < 2:
            volume += 0.25
            mixer.music.set_volume(volume)
        if settings_back.rect.collidepoint(event.pos):
          if backtrack == 0:
            return "Main menu"
          if backtrack == 1:
            return "Main game"      
  return "Settings"
#help function
def Help():
  screen.fill(BLUE)
  help_back.draw(screen)
  help_back_text.draw_text(screen)
  help_title.draw(screen)
  help_title_text.draw_text(screen)
  for text in help_text_list:
    text.draw_text(screen)
  if help_back.rect.colliderect(mouse_rect):
    help_back.colour = RED
  if not help_back.rect.colliderect(mouse_rect):
    help_back.colour = WHITE
  #button collision
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        if help_back.rect.collidepoint(event.pos):
          return "Main game"
  return "Help"
        
  #help back button
#main game function
def Main_game():
  global money, wave_num, placing_tower1, placing_tower2, placing_tower3
  #test background
  screen.fill(BLACK)
  #define the money text
  money_box_text = Text(("£"+str(money)), BLACK, 125, 440, 12)
  #define the wave text so changes with wave_num
  wave_text = Text(("Wave " + str(wave_num)), BLACK, 400, 25, 12)
  #define health text that changes with health
  health_text = Text(("Health:" + str(player_health)), BLACK, 465, 25, 12)
   #drawing map and path boxes
  map_background.draw(screen)
  for path in path_list:
    path.draw(screen)
  #draw each tower
  for tower in tower_group:
    tower.hitbox_check()
    if tower.selected == True:
      pygame.draw.rect(screen, WHITE, (tower.x-tower.range, tower.y-tower.range, tower.x2+2*tower.range, tower.y2+2*tower.range))
  for tower in tower_group:
    tower.draw_tower()
  #drawing tower boxes and outlines
  tower_main_box.draw(screen)
  tower_main_box.draw_outline(screen)
  #draw help box
  help_box.draw(screen)
  for tower in tower_group:
    #if the tower is clicked it runs the method for the tower being selected
    if tower.selected == True:
      tower.select_check()
  settings_main.draw(screen)
  money_box.draw(screen)
  for box in tower_selection_boxes:
    box.draw(screen)
  #draw text
  for text in main_text_list:
    text.draw_text(screen)
  #money text value
  money_box_text.draw_text(screen)
  #wave text value and box 
  wave_box.draw(screen)
  wave_text.draw_text(screen)
  #health box and value
  health_box.draw(screen)
  health_text.draw_text(screen)
  #collisions with tower boxes
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        for tower in tower_group:
          #upgrade and sell handling
          if tower.selected == True and upgrade_damage_box.rect.colliderect(mouse_rect):
            if tower.upgrade_count >= 5:
              print("this tower cannot have any more upgrades")
            else:
              tower.upgrade_count += 1
              tower.damage += 1
              money -= 100
              tower.cost += 100
          elif tower.selected == True and upgrade_range_box.rect.colliderect(mouse_rect):
            if tower.upgrade_count >= 5:
              print("this tower cannot have any more upgrades")
            else:
              tower.upgrade_count += 1
              tower.range += 5
              tower.hitbox = pygame.Rect((tower.x-tower.range, tower.y-tower.range, tower.x2+2*tower.range, tower.y2+2*tower.range))
              money -= 100
              tower.cost += 100
          elif tower.selected == True and sell_box.rect.colliderect(mouse_rect):
            #prevents the player losing all of their money
            if tower.colour == MAGENTA:
              money += tower.cost
            else:
              money += 0.8 * tower.cost
            tower_group.remove(tower)
          tower.selected = False
          #checks if tower is clicked
          if tower.rect.colliderect(mouse_rect):
            tower.selected = True
        #checks if a tower can be placed and places it
        if placing_tower1 == True:
          placing_tower1 = False
          tower_group.append(Tower(mouse_pos[0]-20, mouse_pos[1]-20, 40, 40, MAGENTA,50,1,50))
          money -= tower_group[len(tower_group)-1].cost
        if placing_tower2 == True:
          placing_tower2 = False
          tower_group.append(Tower(mouse_pos[0]-20, mouse_pos[1]-20, 40, 40, CYAN,150,0.5,150))
          money -= tower_group[len(tower_group)-1].cost
        if placing_tower3 == True:
          placing_tower3 = False
          tower_group.append(Tower(mouse_pos[0]-20, mouse_pos[1]-20, 40, 40, RED,25,3,300))
          money -= tower_group[len(tower_group)-1].cost
        if settings_main.rect.collidepoint(event.pos):
          return "Settings"
        if help_box.rect.collidepoint(event.pos):
          return "Help"
        if tower_selection_boxes[0].rect.collidepoint(event.pos):
          if money >= 50:
            placing_tower1 = True
          else:
            print("not enough money")
        if tower_selection_boxes[1].rect.collidepoint(event.pos):
          if money >= 150:
            placing_tower2 = True
          else:
            print("not enough money")
        if tower_selection_boxes[2].rect.collidepoint(event.pos):
          if money >= 300:
            placing_tower3 = True
          else:
            print("not enough money")
  #function that checks if the button is pressed and the tower appears and follows the mouse
  place_tower1()
  place_tower2()
  place_tower3()
  #each enemy moves
  for enemy in enemy_group:
    enemy.move()
  if player_health <= 0:
    return "End game"
  #starts the waves
  wave()
  if wave_num == 11:
    return "End game"
  return "Main game"
#main menu function
def Main_menu():
  #background
  screen.fill(BLUE)
  #draw boxes
  #title box drawn
  menu_title_box.draw(screen)
  #for loop to draw the other menu boxes
  for button in menu_button_list:
    button.draw(screen)
  #draw text
  menu_title_text.draw_text(screen)
  for text in menu_text_list:
    text.draw_text(screen)
  #collision colour changes for each box
  for button in menu_button_list:
    if button.rect.colliderect(mouse_rect):
      button.colour = RED
    if not button.rect.colliderect(mouse_rect):
      button.colour = WHITE
  #collisions
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        #collision with play button
        if menu_button_list[0].rect.collidepoint(event.pos):
          return "Main game"
        #collision with settings button
        if menu_button_list[1].rect.collidepoint(event.pos):
          return "Settings"
        #collision with exit button
        if menu_button_list[2].rect.collidepoint(event.pos):
          pygame.quit()
  return "Main menu"
#the screen for when the game has ended
def End_game():
  screen.fill(BLACK)
  return "End game"
#game running loop
while True:
  #mouse use and rect
  mouse_pos = pygame.mouse.get_pos()
  mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
  if state == "Main menu":
    state = Main_menu()
    #changes the value so that when settings back is pressed goes to right menu
    backtrack = 0
  if state == "Settings":
    state = Settings()
  if state == "Help":
    state = Help()
  if state == "Main game":
    #changes the value so that when settings back is pressed goes to right menu
    backtrack = 1
    state = Main_game()
  if state == "End game":
    state = End_game()
  #quit/exit functions
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  #update the screen
  pygame.display.update()
