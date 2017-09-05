# Snake Game

import pygame
import sys
import random
import time

#checking initializing errors
check_errors = pygame.init()
if check_errors[1] > 0 :
	print("{!} Executred {0} errors! Exiting...!".format(check_errors))
	sys.exit(-1)
else :
	print("{!} Pygame successfully initialized")
	
#play surface
playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('Snake game')

#colours
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
yellow = pygame.Color(255,255,0) #food

#FPS controller
fpsController = pygame.time.Clock()

#Important Variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,64)*10,random.randrange(1,48)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

#Game over function
def gameOver():
	myFont = pygame.font.SysFont('monaco',72)
	GOsurf = myFont.render('Game over!',True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (320,15)
	playSurface.blit(GOsurf,GOrect)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit() #pygame quit
	sys.exit(-1) #console exit

#Scoreboard
def showScore(choice = 1) :
	scoreFont = pygame.font.SysFont('monaco',50)
	Ssurf = scoreFont.render('Score : {0}'.format(score),True,black)
	Srect = Ssurf.get_rect()
	if choice == 1 :
		Srect.midtop = (100,20)
	else :
		Srect.midtop = (360,80)
	playSurface.blit(Ssurf,Srect)
	pygame.display.flip()
	
#Main logic of the game
while True :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN :
			if event.key == pygame.K_RIGHT or event.key == ord('d') :
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a') :
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w') :
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s') :
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE :
				pygame.event.post(pygame.event.Event(pygame.QUIT))
				
	#validation of directions
	if changeto == 'RIGHT' and not direction == 'LEFT' :
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT' :
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN' :
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP' :
		direction = 'DOWN'
		
	#Updating snake position
	if direction == 'RIGHT' :
		snakePos[0] += 10
	if direction == 'LEFT' :
		snakePos[0] -= 10
	if direction == 'UP' :
		snakePos[1] -= 10
	if direction == 'DOWN' :
		snakePos[1] += 10
		
	#Snake body mechanism
	snakeBody.insert(0,list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1] :
		foodSpawn = False
		score += 1
	else :
		snakeBody.pop()
		
	if foodSpawn == False :
		foodPos = [random.randrange(1,64)*10,random.randrange(1,48)*10]
	foodSpawn = True
	
	#Background ND STUFF
	playSurface.fill(white)
	
	
	for pos in snakeBody :
		pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
	
	pygame.draw.rect(playSurface,yellow,pygame.Rect(foodPos[0],foodPos[1],10,10))
	
	if snakePos[0] > 640 or snakePos[0] < 0  or snakePos[1]>480 or snakePos[1]<0:
		showScore(0)
		gameOver()
		
	for block in snakeBody[1:] :
		if snakePos[0] == block[0] and snakePos[1] == block[1] :
			showScore(0)
			gameOver()
	
	pygame.display.flip()
	showScore()
	fpsController.tick(17)