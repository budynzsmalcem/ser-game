import pygame


pygame.init()

screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption(" Ser")

portret = pygame.image.load('ser.png')
pygame.display.set_icon(portret)

running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    screen.fill(( 255,255,255 ))
    pygame.display.update()