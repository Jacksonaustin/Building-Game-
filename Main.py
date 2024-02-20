import pygame 

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

Screen_Width = 1000
Screen_Height = 1000

screen = pygame.display.set_mode((Screen_Width, Screen_Height))

running = True

while running:
    for event in pygame.event.get():
        
        if(event.type == KEYDOWN):
            if(event.key == K_ESCAPE):
                running = False 

        elif(event.type == QUIT):
            running = False 
            
