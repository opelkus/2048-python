from dataclasses import dataclass
import pygame
import under
import time as TIME
from pygame import *
from pygame.locals import *

Data=under.Data()

screen = pygame.display.set_mode((1280,720),HWSURFACE|DOUBLEBUF|RESIZABLE)

pygame.display.set_caption('moje 2048')
pygame.init()

def hexx(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
k_back="CCC0B3"

k_fence=(187,173,160)


a=(237,224,200)
rgb=(242,177,121)
rgb=(238,228,218)
print(Data.board)



def cyl(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

def gen_sqrt(coord,type,value,offset=(0,0)):
    kolor=["CCC0B3","CCC0B3"]
    szer_kl=105
    szer_ram=16
    poz=(Data.offset[0]+offset[0]+(coord[0])*(szer_kl+szer_ram),Data.offset[1]+offset[1]+(coord[1])*(szer_kl+szer_ram))
    
    cyl(screen,(poz[0]+szer_ram,poz[1]+szer_ram,szer_kl,szer_kl),k_fence,0)
    cyl(screen,(poz[0]+szer_ram,poz[1]+szer_ram,szer_kl,szer_kl),hexx(kolor[0]))
    font = pygame.font.SysFont("comicsansms", 20)
    color=(255,0,255)
    text = font.render(str(value), False, color)
    screen.blit(text,((poz[0]+szer_ram+szer_kl/2-text.get_width()/2,poz[1]+szer_ram+szer_kl/2-text.get_height()/2)))

def refresh_board(board):
    gen_ramki()
    for iy in range(len(board)):
        for ix in range(len(board[0])):
            gen_sqrt((ix,iy),1,board[0][0])


def gen_ramki(offset=(0,0)):
    poz=(Data.offset[0]+offset[0],Data.offset[1]+offset[1])
    global k_fence
    
    szer_ram=16
    szer_kl=105
    szer=500
    for kol in range(5):
        cyl(screen,(poz[0]+(szer_kl+szer_ram)*kol,poz[1],szer_ram,szer),k_fence,0.5)

    for rzad in range(5):
        cyl(screen,(poz[0],poz[1]+(szer_kl+szer_ram)*rzad,szer,szer_ram),k_fence,0.5)

    
    display.flip()




a=[1,2,3,4]*69


i=-1


running = True

while (running): # loop listening for end of game
    t0= TIME.process_time()
    TIME.sleep(1)
    refresh_board(Data.board)
    
    i+=1
    
    t= TIME.process_time()
    #print(1/(t-t0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




pygame.quit()