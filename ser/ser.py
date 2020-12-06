import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption(" Ser")

portret = pygame.image.load('ser.png')
pygame.display.set_icon(portret)

turn = 1
p1score = 0
p2score = 0

font = pygame.font.Font('freesansbold.ttf', 20)

p1x = 10
p1y = 10
textp1 = "Gracz 1:   "

p2x = 450
p2y = 10
textp2 = "Gracz 2:   "

xblock = 275
yblock = 200
blockimage = pygame.image.load('basicblock.png')
secblockimage = pygame.image.load('chosenblock.png')

winner = "?"

def show_score(x,y,text,wynik):
    score = font.render(text + str(wynik), True, (1,1,1))
    screen.blit(score, (x, y))

def endscreen(winner):
    text = font.render(f"Zwyciężył {winner}", True, (1,1,1))
    screen.blit(text, (200, 650))

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

lista =  [[0,0,0,0,a,0,0,0,0],
          [0,0,0,b,c,d,0,0,0],
          [0,0,e,f,g,h,i,0,0],
          [0,j,k,l,m,n,o,p,0],
          [r,s,t,u,w,y,z,aa,ab]]
listb = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,w,y,z,aa,ab]




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
                if temp != 0:
                    temp.iscliked = True

                rowcliked = True

                for number in range(9):
                    if lista[vertrans][number] != 0:
                        if lista[vertrans][number].iscliked == False:
                            rowcliked = False

                if rowcliked == True:
                    amountofspace = lista[vertrans]
                    lettersrow = amountofspace.count(0)
                    addscore = 9-lettersrow
                    if turn%2 != 0:
                        p1score += addscore
                    else:
                        p2score += addscore
                    addscore = 0

                columncliked = True

                for number in range(5):
                    if lista[number][hoztrans] != 0:
                        if lista[number][hoztrans].iscliked == False:
                            columncliked = False

                if columncliked == True:
                    pointsneeded = 0
                    for number in range(5):
                        if lista[number][hoztrans] == 0:
                            pointsneeded +=1

                    addscore = 5 - pointsneeded

                    if turn%2==0:
                        p2score += addscore
                    else:
                        p1score += addscore
                    addscore = 0

                turn +=1


    show_score(p1x,p1y,textp1,p1score)
    show_score(p2x, p2y, textp2, p2score)

    for element in listb:
        if element.iscliked == False:
                element.elm()
        else:
            element.blockimg = secblockimage
            element.elm()\

    if p1score + p2score == 50:
        if p1score > p2score:
            winner = "Gracz 1"
            endscreen(winner)
        else:
            winner = "Gracz 2"
            endscreen(winner)
    pygame.display.update()

