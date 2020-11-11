import pygame


pygame.init()

screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption(" Ser")

portret = pygame.image.load('ser.png')
pygame.display.set_icon(portret)

blockimg = pygame.image.load('basicblock.png')
xblock = 275
yblock = 400

nol = 2

def block(x,y,nol):
    k = 0
    while nol > k:
        if k == 0:
            screen.blit(blockimg, (x, ((y-(nol*40)))))
        else:
            for z in range(nol+2):
                screen.blit(blockimg, ((x-60)+60*z, y))
        k+=1

running = True
while running:
    
    screen.fill(( 255,255,255 )
                
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    block(xblock, yblock, nol)
    
    pygame.display.update()
