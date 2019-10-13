import pygame
import time
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 500
display_height = 500

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Avoid')

x_change = 0
y_change = 0

FPS = 30
block_size = 10

font = pygame.font.SysFont(None, 25)
smallfont = pygame.font.SysFont("comicsansms",25)

def showLives(lives):
    text = smallfont.render("Lives: "+str(lives), True, white)
    screen.blit(text, [0,0])
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [100,250])
                
clock = pygame.time.Clock()

def gameLoop():
    gameExit = False
    gameOver = False

    x = 250
    y = 425

    x_change = 0
    y_change = 0

    obj_speed = 5

    
    obj_y = 0
    obj_x = 0
    
  
    
    lives = 3
    while not gameExit:
        while gameOver == True:
            screen.fill(white)
            message_to_screen("Game Over, Press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
        if x > 500-block_size:
            x-=block_size
        if x < 0+block_size:
            x+=block_size
 #       if x >= display_width-block_size-block_size or x < 0:
 #           gameOver = True
        obj_y = obj_y + obj_speed
        if obj_y > display_height:
            obj_x = random.randrange(0, display_width-block_size)
            obj_y = -25
            
        x += x_change
        y += y_change
        screen.fill(black)
      
        pygame.draw.rect(screen,white, [obj_x,obj_y,20,20])
        pygame.draw.rect(screen, red, [x,y,block_size,block_size])
        showLives(lives)
        pygame.display.update()
        if x == obj_x and y == obj_y:
            lives -= 1
        if lives == 0:
            gameOver = True
    clock.tick(FPS)
    pygame.quit()
    quit()

gameLoop()


