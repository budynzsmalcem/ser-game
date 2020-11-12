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

class block():
    def __init__(self, x, y, blockimg):
        self.x = x
        self.y = y
        self.blockimg = blockimg

    def elm(self):
        screen.blit(self.blockimg, (self.x, self.y)
                    
one = block(xblock, yblock, blockimage)

running = True
while running:
    
    screen.fill(( 255,255,255 )
                
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    one.elm()
    
    pygame.display.update()
