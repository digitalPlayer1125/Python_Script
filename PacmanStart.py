"""
	Start windows of the Pacman:
"""

#Pygame, Time and OS Modules
import pygame
pygame.init()
import time
import os

# Defining BLACK color
BLACK = (0,0,0)

#Centering the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Defining Screen Size
size = (1280, 720)

#Setting the first screen
screen=pygame.display.set_mode(size)

#Giving the caption
pygame.display.set_caption("Pacman")

#Inserting the images of characters
Pacman = pygame.image.load('Pacman.png')

#For letting the screen be displayed until exit
running = 1
screen.fill((BLACK))
i=1

#Audio File
file = 'PacmanAudio.wav'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
#Here's the first introductory screen part

while running and i<900:
		screen.fill((BLACK))
		screen.blit(Pacman,(i+2,400))
		pygame.display.flip()
		i+=1
pygame.display.quit()

##################################################################################################################
""" To Check If the button has been pressed"""
def main(button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos  # gets mouse position
			# checks if mouse position is over the button
			if button.collidepoint(mouse_pos):
				# prints current location of mouse
				return 0

##################################################################################################################
"""Second Screen"""

#Defining Screen Size
size = (1280, 720)

#Setting the second screen
screen=pygame.display.set_mode(size)

#Giving the caption
pygame.display.set_caption("Pacman")
screen.fill((BLACK))

#Inserting the images of characters
Logo = pygame.image.load('Logo.png')
Logo = pygame.transform.scale(Logo, (640, 480))
Pacman = pygame.image.load('Pacman.png')
Pinky = pygame.image.load('Pinky.png')
Inky = pygame.image.load('Inky.png')
Blinky = pygame.image.load('Blinky.png')
Clyde = pygame.image.load('Clyde.png')
Ghost = pygame.image.load('Ghost.png')
Play = pygame.image.load('PlayG.png')

#For letting the screen be displayed until exit
running = 1
i=1
button = pygame.Rect(600, 605, 95, 80)
pygame.draw.rect(screen, [0, 0, 0], button)  # draw button
while running :
		if(main(button)==0):
			#button is pressed then switched to next window
			break
			screen.fill((BLACK))
		elif(i<500):
			screen.fill((BLACK)) #Screen fill black

			screen.blit(Logo,(380,100))
			#print(i,"Logo")

			screen.blit(Ghost,(i,400))
			#print(i,"Ghost")

			screen.blit(Pacman,(i+60,400))
			#print(i+60,"Pacman")

			screen.blit(Pinky,(i+120,400))
			#print(i+120,"Pinky")

			screen.blit(Inky,(i+180,400))
			#print(i+180,"Inky")

			screen.blit(Blinky,(i+240,400))
			#print(i+240,"Blinky")

			screen.blit(Clyde,(i+300,400))
			#print(i+300,"Clyde")
			
			button = pygame.Rect(600, 605, 95, 80)
			pygame.draw.rect(screen, [0, 0, 0], button)  # draw button
			screen.blit(Play,(600,600))
			pygame.display.flip()
			if(main(button)==0):
				break
			else:
				def li():
					return None
		i+=1
		if(main(button)==0):
				break
import PacmanMain 	#Switch to the Game