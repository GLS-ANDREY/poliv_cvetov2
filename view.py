import pygame
import time
import model

v = pygame.image.load("voda.png")
cj = pygame.image.load("joltiy_cvetok.png")
ck = pygame.image.load("krasniy_cvetok.png")
vv = pygame.transform.scale(v, [75, 100])
kc = pygame.transform.scale(ck, [100, 200])
jc = pygame.transform.scale(cj, [100, 200])
k = 1
def xz():
    global k
    k = k + 30
def ekran():
    global k
    time.sleep(0.010)
    k = k + 1
    e.blit(jc,[100,300])
    e.blit(kc,[0,300])
    e.blit(vv, [75, k])
    pygame.display.flip()
    e.fill([0,0,0])


e = pygame.display.set_mode([200, 500])
