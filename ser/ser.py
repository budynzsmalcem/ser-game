import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption(" Ser")

portret = pygame.image.load('ser.png')
pygame.display.set_icon(portret)


xblock = 275
yblock = 200
blockimage = pygame.image.load('basicblock.png')
secblockimage = pygame.image.load('chosenblock.png')

class block():
    def __init__(self, x, y, blockimg):
        self.x = x
        self.y = y
        self.blockimg = blockimg
        self.iscliked = False

    def elm(self):
        screen.blit(self.blockimg, (self.x, self.y))


a = block(xblock, yblock, blockimage)
b = block(225,255,blockimage)
c = block(275,255,blockimage)
d = block(325,255,blockimage)
e = block(175,310,blockimage)
f = block(225,310,blockimage)
g = block(275,310,blockimage)
h = block(325,310,blockimage)
i = block(375,310,blockimage)
j = block(125,365,blockimage)
k = block(175,365,blockimage)
l = block(225,365,blockimage)
m = block(275,365,blockimage)
n = block(325,365,blockimage)
o = block(375,365,blockimage)
p = block(425,365,blockimage)
r = block(75,420,blockimage)
s = block(125,420,blockimage)
t = block(175,420,blockimage)
u = block(225,420,blockimage)
w = block(275,420,blockimage)
y = block(325,420,blockimage)
z = block(375,420,blockimage)
aa = block(425,420,blockimage)
ab = block(475,420,blockimage)
gg = block(475,420,blockimage)
gg.iscliked = True

lista =  [[gg,gg,gg,gg,a,gg,gg,gg,gg],
          [gg,gg,gg,b,c,d,gg,gg,gg],
          [gg,gg,e,f,g,h,i,gg,gg],
          [gg,j,k,l,m,n,o,p,gg],
          [r,s,t,u,w,y,z,aa,ab]]
listb = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,w,y,z,aa,ab]


turn = 3
p1score = 0
p2score = 0

running = True
while running:

    screen.fill(( 255,255,255 ))

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            running = False

        if events.type == pygame.MOUSEBUTTONDOWN:
            clicks = pygame.mouse.get_pos()

            hoz = float(clicks[0])
            ver = float(clicks[1])
            hoztrans = (hoz-75)/50
            vertrans = (ver-225)/55
            hoztrans = math.floor(hoztrans)
            vertrans = round(vertrans)

            if vertrans < 0 or vertrans > 4:
                pass
            else:
                temp = lista[vertrans][hoztrans]
                temp.iscliked = True
                columncliked = True

                for number in range(9):
                    if lista[vertrans][number].iscliked == False:
                        columncliked = False
                if columncliked == True:
                    addscore = 9-(lista.count("gg"))
                    if turn%2 != 0:
                        p1score += addscore
                    else:
                        p2score += addscore
                    addscore = 0

                rowcliked = True
                for number in range(5):
                    if lista[number][hoztrans].iscliked == False:
                        rowcliked = False
                if rowcliked == True:
                    addscore = 9-(lista.count(gg))
                    if turn%2==0:
                        p2score += addscore
                    else:
                        p1score += addscore
                    addscore = 0
                    turn +=1


    for element in listb:
        if element == gg:
            pass
        else:
            if element.iscliked == False:
                element.elm()
            else:
                element.blockimg = secblockimage
                element.elm()






    pygame.display.update()
