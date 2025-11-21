#import pygame and other modules
import sys
import pygame
from pygame import *
import math
from pygame import mixer
from colours import *

from objects.user_interface.box import Box
from objects.user_interface.text import Text
from objects.entities.enemy import Enemy
from objects.entities.tower import Tower

from ui.main_ui import *
from ui.menu_ui import *

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
#used to check the previous game state so that when back button is pressed the correct screen loads
backtrack = 0
#keeps track of the wave number
wave_num = 0
player_state = {"player_health": 100,
                "money": 100}


def select_check(self):
    # draws the text and boxes for upgrades and sell
    upgrade_damage_box.draw(screen)
    upgrade_range_box.draw(screen)
    sell_box.draw(screen)
    upgrade_damage_text.draw_text(screen)
    upgrade_range_text.draw_text(screen)
    sell_text.draw_text(screen)


# functions to make tower follow mouse until placed
def place_tower1():
    if placing_tower1 == True:
        pygame.draw.rect(screen, MAGENTA, (mouse_pos[0] - 20, mouse_pos[1] - 20, 40, 40,))


def place_tower2():
    if placing_tower2 == True:
        pygame.draw.rect(screen, CYAN, (mouse_pos[0] - 20, mouse_pos[1] - 20, 40, 40))


def place_tower3():
    if placing_tower3 == True:
        pygame.draw.rect(screen, RED, (mouse_pos[0] - 20, mouse_pos[1] - 20, 40, 40))
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
    enemy_group.append(Enemy(250, 0, 2, 20, RED, 1, 2, 100,
                             waypoints, red_enemy_image, 10, player_state, screen))
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
  money_box_text = Text(("£"+str(player_state["money"])), BLACK, 125, 440, 12)
  #define the wave text so changes with wave_num
  wave_text = Text(("Wave " + str(wave_num)), BLACK, 400, 25, 12)
  #define health text that changes with health
  health_text = Text(("Health:" + str(player_state["player_health"])), BLACK, 465, 25, 12)
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
          tower_group.append(Tower(mouse_pos[0]-20, mouse_pos[1]-20, 40, 40, MAGENTA,50,1,1, 50))
          player_state["money"] -= tower_group[len(tower_group)-1].cost
        if placing_tower2 == True:
          placing_tower2 = False
          tower_group.append(Tower(mouse_pos[0]-20, mouse_pos[1]-20, 40, 40, CYAN,150,0.5,150))
          player_state["money"] -= tower_group[len(tower_group)-1].cost
        if placing_tower3 == True:
          placing_tower3 = False
          tower_group.append(Tower(mouse_pos[0]-20, mouse_pos[1]-20, 40, 40, RED,25,3,300))
          player_state["money"] -= tower_group[len(tower_group)-1].cost
        if settings_main.rect.collidepoint(event.pos):
          return "Settings"
        if help_box.rect.collidepoint(event.pos):
          return "Help"
        if tower_selection_boxes[0].rect.collidepoint(event.pos):
          if player_state["money"] >= 50:
            placing_tower1 = True
          else:
            print("not enough money")
        if tower_selection_boxes[1].rect.collidepoint(event.pos):
          if player_state["money"] >= 150:
            placing_tower2 = True
          else:
            print("not enough money")
        if tower_selection_boxes[2].rect.collidepoint(event.pos):
          if player_state["money"] >= 300:
            placing_tower3 = True
          else:
            print("not enough money")
  #function that checks if the button is pressed and the tower appears and follows the mouse
  place_tower1()
  place_tower2()
  place_tower3()
  #each enemy moves
  for enemy in enemy_group:
    enemy.move(waypoints, enemy_group, player_state, screen)
  if player_state["player_health"] <= 0:
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
