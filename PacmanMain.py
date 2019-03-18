"""
	Main screen of the game: 
"""

#Required Imports
import pygame
import random
from pygame.locals import *
from pynput import keyboard
import numpy
from numpy import loadtxt
import time
import sys
import os

#Setting the clock
clock = pygame.time.Clock()

#Centering the window
#Copied from stackoverflow
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 0, 255) #BLACK
GREY = pygame.Color('grey') #GREY
PACMAN_COLOR = pygame.Color(0, 255, 0, 255) # GREEN
GHOST_COLOR = pygame.Color(255, 0, 0, 255) #RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # YELLOW
PORTAL_COLOR = pygame.Color(0, 255, 255, 255) #BLUE_GREEN
TEXT_COLOR = pygame.Color(0, 0, 0, 255) #BLACK
GAME_TOPLEFT = (0, HEIGHT)
GAME_BCKGRND = (0, 0, 100) #BLACK
MENU_BCKGRND = (0, 128, 128) #BLUE_GREEN
MENU_BORDER = pygame.Color(128, 128, 0, 255) #BROWN
DOWN = (0,1)
RIGHT = (1,0)
UP = (0,-1)
LEFT = (-1,0)
NONE = (0,0)

#Initialize drawer functions for all objects
#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	pixels = (pixels[0]+GAME_TOPLEFT[0],pixels[1]+GAME_TOPLEFT[1])
	pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the player
def draw_pacman(screen,pos,color):
	pixels = pixels_from_points(pos)
	pixels = (pixels[0]+GAME_TOPLEFT[0],pixels[1]+GAME_TOPLEFT[1])
	def trytoplotimageofpacman(pixels):
		change=tuple(pixels)
		#print(change)
		#print(change[0])
		change = (change[0]-5,change[1]-5)
		#Pacman = pygame.image.load('pac-man.png')
		#PacMan = pygame.transform.scale(screen,(WIDTH, HEIGHT))
		#screen.blit(Pacman,[change, (WIDTH, HEIGHT)])
		#time.sleep(1)
		Pacman = pygame.image.load('PacmanEat.png')
		PacMan = pygame.transform.scale(screen,(WIDTH, HEIGHT))
		screen.blit(Pacman,[change, (WIDTH, HEIGHT)])
	trytoplotimageofpacman(pixels)
	#pygame.draw.arc(screen, color, [pixels, (WIDTH, HEIGHT)],30,60,1)
	
#Draws a rectangle for the ghost
def draw_ghost(screen,pos):
	pixels = pixels_from_points(pos)
	pixels = (pixels[0]+GAME_TOPLEFT[0],pixels[1]+GAME_TOPLEFT[1])
	def trytoplotimageofghost(pixels):
		change=tuple(pixels)
		#print(change)
		#print(change[0])
		#Pacman = pygame.image.load('pac-man.png')
		#PacMan = pygame.transform.scale(screen,(WIDTH, HEIGHT))
		#screen.blit(Pacman,[change, (WIDTH, HEIGHT)])
		#time.sleep(1)
		Ghost = pygame.image.load('pac-man.png')
		#host = pygame.transform.scale(screen,(WIDTH, HEIGHT))
		screen.blit(Ghost,[change, (WIDTH, HEIGHT)])
	trytoplotimageofghost(pixels)
	#pygame.draw.rect(screen, GHOST_COLOR, [pixels, (WIDTH, HEIGHT)])
	
#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	pixels = (pixels[0]+10,pixels[1]+GAME_TOPLEFT[1]+10)
	#pixels=pixels[0],pixels[1]
	pygame.draw.ellipse(screen, COIN_COLOR, [pixels, (WIDTH/4, HEIGHT/4)])

#draws a circle for the powerups
def draw_powerup(screen, pos, color):
	pos = (pos[0]+GAME_TOPLEFT[0]//WIDTH,pos[1]+GAME_TOPLEFT[1]//HEIGHT)
	pygame.draw.circle(screen, GREY, (pos[0]*WIDTH+WIDTH//2,pos[1]*HEIGHT+HEIGHT//2), WIDTH//4)

#draws the life display on menu
def draw_menu(screen, life_left, points, time_taken):
	timeDone = time.time() - time_start
	screen.blit(text.render('Lives left: '+str(life_left), True, TEXT_COLOR),(0,HEIGHT//3))
	screen.blit(text.render('Points: '+str(points), True, TEXT_COLOR),(cols*WIDTH//3,HEIGHT//3))
	screen.blit(text.render('Time: '+str(time_taken), True, TEXT_COLOR),(2*cols*WIDTH//3,HEIGHT//3))

#draws a portal for the jump
def draw_portal(screen, pos, number):
	pos = (pos[0]+GAME_TOPLEFT[0]//WIDTH,pos[1]+GAME_TOPLEFT[1]//HEIGHT)
	plist = [(pos[0]*WIDTH , pos[1]*HEIGHT + HEIGHT),
		 (pos[0]*WIDTH + WIDTH//4 , pos[1]*HEIGHT + HEIGHT//4),
		 (pos[0]*WIDTH + 3*WIDTH//4 , pos[1]*HEIGHT + HEIGHT//4),
		 (pos[0]*WIDTH + WIDTH , pos[1]*HEIGHT + HEIGHT),
		 (pos[0]*WIDTH , pos[1]*HEIGHT + HEIGHT)
		]
	pygame.draw.polygon(screen, PORTAL_COLOR, plist)
	screen.blit(text.render(number, True, TEXT_COLOR),(pos[0]*WIDTH + WIDTH//3,pos[1]*HEIGHT + HEIGHT//4))

#Initialize player(Pacman)
class PacMan:
	move_direction = DOWN
	def __init__(self):
		self.x = 1
		self.y = 1

	def position(self):
		return (self.x,self.y)
	
	def display(self,screen,color):
		draw_pacman(screen, (self.x,self.y), color)

	def moveTo(self, x, y):
		self.x = x
		self.y = y

#Initialise the power_ups
SPEED_PU_COLOR = pygame.Color(235, 34, 228, 255)
GHOSTHUNTER_PU_COLOR = pygame.Color(235, 215, 34, 255)
INVISIBLE_PU_COLOR = pygame.Color(115, 125, 116, 255)

POWER_NONE = ('',PACMAN_COLOR)
POWER_SPEEDUP = ('s',SPEED_PU_COLOR)
POWER_GHOSTHUNTER = ('k',GHOSTHUNTER_PU_COLOR)
POWER_INVISIBLE = ('i',INVISIBLE_PU_COLOR)

#Utility functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)

#Initializing pygame
#Initializing variables
layout = loadtxt('level2.txt', dtype=str)
rows, cols = layout.shape
pygame.display.init()
pygame.font.init()
basic_f = pygame.font.get_default_font()
text = pygame.font.Font(basic_f, 5*HEIGHT//8)

screen = pygame.display.set_mode((cols*WIDTH+GAME_TOPLEFT[0],rows*HEIGHT+GAME_TOPLEFT[1]), 0, 32)
game_background = pygame.surface.Surface((cols*WIDTH,rows*HEIGHT)).convert()
menu_background = pygame.surface.Surface((cols*WIDTH,GAME_TOPLEFT[1])).convert()
time.sleep(2)
class Portals:
	portal_links = {}
	jump_loc = (-1,-1)
	def add(self, x, y, num):
		try:
			src = Portals.portal_links[num]
			Portals.portal_links[src] = (x,y)
			Portals.portal_links.pop(num)
			Portals.portal_links.update([[(x,y),src]])
		except KeyError:
			Portals.portal_links.update([[num,(x,y)],[(x,y),num]])
		
	def check(self, x, y):
		if Portals.jump_loc != (x,y):
			Portals.jump_loc = (-1,-1)
			return Portals.portal_links.get((x,y))
		return None

	def exec_jump(self, x, y):
		global pacman
		pacman.x, pacman.y = Portals.portal_links[(x,y)]
		Portals.jump_loc = (pacman.x,pacman.y)
		
global ghost_positions
ghost_positions = []
portal = Portals()
for y in range(len(layout)):
	ghost_positions.extend([(x,y) for x,val in enumerate(layout[y]) if val == 'O'])
	for x in range(len(layout[y])):
		if layout[y][x] >= '1' and layout[y][x] < '9':
			portal.add(x, y, layout[y][x])

game_background.fill(GAME_BCKGRND)
menu_background.fill(MENU_BCKGRND)

#Utility functions to control how the various characters move
def set_direction(key):
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
		if key.char == 'w':
			PacMan.move_direction = UP
		if key.char == 'a':
			PacMan.move_direction = LEFT
		if key.char == 's':
			PacMan.move_direction = DOWN
		if key.char == 'd':
			PacMan.move_direction = RIGHT
	except AttributeError: pass
	return looping

def random_pos(pos):
	x = random.randint(0,3)
	if x == 0: direction = UP
	if x == 1: direction = DOWN
	if x == 2: direction = RIGHT
	if x == 3: direction = LEFT
	if layout[pos[1]+direction[1]][pos[0]+direction[0]] == 'w':
		direction = NONE
		random_pos(pos)
		#print("This is randomly generated: ",direction)
	return add_to_pos(pos,direction)

def chase(x,y,pos):
	'''
	Avoided This and switched to Randomness as it would make movements unpredictable
	'''
	if x < pos[0] and layout[pos[1]][pos[0]-1] != 'w':
		pos = add_to_pos(pos,LEFT)
	elif x > pos[0] and layout[pos[1]][pos[0]+1] != 'w':
		pos = add_to_pos(pos,RIGHT)
	elif y < pos[1] and layout[pos[1]-1][pos[0]] != 'w':
		pos = add_to_pos(pos,UP)
	elif y > pos[1] and layout[pos[1]+1][pos[0]] != 'w':
		pos = add_to_pos(pos,DOWN)
	return pos

def flee(x,y,pos):
	'''
	Avoided This and switched to Randomness as it would make movements unpredictable,
	enabling the pacman to earn more points.
	'''
	if x < pos[0] and layout[pos[1]][pos[0]+1] != 'w':
		pos = add_to_pos(pos,RIGHT)
	elif x > pos[0] and layout[pos[1]][pos[0]-1] != 'w':
		pos = add_to_pos(pos,LEFT)
	elif y < pos[1] and layout[pos[1]+1][pos[0]] != 'w':
		pos = add_to_pos(pos,DOWN)
	elif y > pos[1] and layout[pos[1]-1][pos[0]] != 'w':
		pos = add_to_pos(pos,UP)
	return pos

global pacman
pacman = PacMan()			

class PowerUP:
	power = POWER_NONE
	timer = 0
	flag = 0
	def __init__(self):
		self.points = 0
		
	def tic(self):
		#If using a power-up,
		if PowerUP.power[0] != '':
			#If time has run out, remove power_up
			if PowerUP.timer == 0:
				PowerUP.power = POWER_NONE
			#Else decrease the time left
			else:
				PowerUP.timer -= 1
	def check(self,y,x):
		#If come in contact with a power-up, grab it!
		if layout[y][x] == 's':
			PowerUP.power = POWER_SPEEDUP
			PowerUP.timer = 180
			layout[y][x] = '.'
			#Audio File
			file = 'pacman_chomp1.wav'
			pygame.init()
			pygame.mixer.init()
			pygame.mixer.music.load(file)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play()
		if layout[y][x] == 'i':
			PowerUP.power = POWER_INVISIBLE
			PowerUP.timer = 180
			layout[y][x] = '.'
			#Audio File
			file = 'pacman_chomp1.wav'
			pygame.init()
			pygame.mixer.init()
			pygame.mixer.music.load(file)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play()
		if layout[y][x] == 'k':
			PowerUP.power = POWER_GHOSTHUNTER
			PowerUP.timer = 60
			layout[y][x] = '.'
			#Audio File
			file = 'pacman_chomp1.wav'
			pygame.init()
			pygame.mixer.init()
			pygame.mixer.music.load(file)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play()
		# coin should dissapear when eating, i.e update the layout array
		if layout[y][x] == 'c':
			layout[y][x] = '.'
			#Audio File
			file = 'pacman_chomp.wav'
			pygame.init()
			pygame.mixer.init()
			pygame.mixer.music.load(file)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play()
			self.points += 5
		if layout[y][x] == '.':
			#Audio File
			file = 'pacman_vague.wav'
			pygame.init()
			pygame.mixer.init()
			pygame.mixer.music.load(file)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play()
			self.points += 0
	def execute(self):
		global ghost_positions
		global lives
		#If using power-up speed 2x
		if PowerUP.power[0] == 's':
			#If first time(flag=1), skip ghost's turn, set flag=0
			if PowerUP.flag == 1:
				PowerUP.flag = 0
				#Time to sleep
				return 1
			#If second time(flag=0), allow ghost turn, set flag=1
			else: PowerUP.flag = 1
		
		#If using power-up invisible, ghosts will roam around randomly
		if PowerUP.power[0] == 'i':
			ghost_positions = [random_pos(pos) for pos in ghost_positions]
		#If using power-up ghosthunter, ghosts will run from you
		elif PowerUP.power[0] == 'k':
			ghost_positions = [random_pos(pos) for pos in ghost_positions]
		#If not using any of above, ghosts will chase you
		else:
			ghost_positions = [random_pos(pos) for pos in ghost_positions]

		#If you come in contact with a ghost(s)
		if any([pacman.position() == ghost_position for ghost_position in ghost_positions]):
			#And have ghosthunter power-up, kill the ghost(s)
			if PowerUP.power[0] == 'k':
				for pos in ghost_positions[:]:
					if pos == pacman.position():
						ghost_positions.remove(pos)
			#Else, you lose a point and restart
			elif PowerUP.power[0] != 'i':
				pacman.x = pacman.y = 1
				self.points -= 1
				lives -= 1
		#Time to sleep
		return 0.15

power = PowerUP()
looping = True
time_start = time.time()
global lives
lives = 3
#TODO: Take input from the user and update pacman moving direction
kl = keyboard.Listener(on_press = set_direction,on_release = None)
kl.start()

# Main game loop
while looping:
	for event in pygame.event.get():
		if event.type == QUIT:
			looping = False

	#If player loses or wins, end game
	if lives == 0 or not any(['c' in row for row in layout]):
		looping = False

	#Setup the background and menu of the game
	screen.blit(menu_background, (0,0))
	screen.blit(game_background, GAME_TOPLEFT)
	draw_menu(screen, lives, power.points, time.time() - time_start)

	#Draw board from the 2d layout array.
	#In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				draw_coin(screen, pos)
			elif value == 's':
				draw_powerup(screen, pos, POWER_SPEEDUP[1])
			elif value == 'i':
				draw_powerup(screen, pos, POWER_INVISIBLE[1])
			elif value == 'k':
				draw_powerup(screen, pos, POWER_GHOSTHUNTER[1])
			elif value >= '1' and value <= '9':
				draw_portal(screen, pos, value)

	#Draw the player
	pacman.display(screen,PowerUP.power[1])
	
	#Draw the ghosts
	for position in ghost_positions:
		draw_ghost(screen, position)

	#If reach a portal, jump to other exit
	if portal.check(pacman.x, pacman.y) != None:
		portal.exec_jump(pacman.x, pacman.y)
	#If just jumped, stabilize(skip a turn)

	#Get next position to go depending on move_direction
	next_x = (pacman.x + PacMan.move_direction[0]) % cols
	next_y = (pacman.y + PacMan.move_direction[1]) % rows
	
	#Check for any coin/power/ghost at next position	
	power.check(next_y, next_x)
	power.tic()

	#Update player position based on movement
	# player should stop when colliding with a wall
	if layout[next_y][next_x] != 'w':
		pacman.moveTo(next_x, next_y)
			
	#If power_up is enabled, execute it	
	sleep = power.execute()
	
	#Update the display
	pygame.display.update()

	#Wait for a while, computers are very fast.
	time.sleep(sleep)

if lives > 0:
	print("YOU WIN!")
	print("You won",power.points,"points!")
else:
	#Audio File
	file = 'sad.wav'
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play()
	print("You Lost!")
	#Defining Screen Size
	size = (1280, 720)

	#Setting the first screen
	screen=pygame.display.set_mode(size)

	#Giving the caption
	pygame.display.set_caption("Pacman")

	#Setting The Font
	writingfont = pygame.font.SysFont('comicsansms', 100)
	running = 1
	i=1
	while running:
		Pacman = pygame.image.load('pac-man.png')
		Pac = pygame.image.load('GameOver.jpg')
		while running and i<2000:
				screen.fill((WALL_COLOR))
				screen.blit(Pac,(360,160))
				screen.blit(Pacman,(numpy.random.randint(1280),numpy.random.randint(1280)))
				pygame.display.flip()
				i+=1
		pygame.display.quit()
		print("Time taken:",time.time()-time_start,"seconds.")
		kl.stop()
		break
	time.sleep(10)
	sys.exit()