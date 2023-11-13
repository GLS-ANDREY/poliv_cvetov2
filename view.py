import pygame
import model

v = pygame.image.load("voda.png")
cj = pygame.image.load("joltiy_cvetok.png")
ck = pygame.image.load("krasniy_cvetok.png")
vv = pygame.transform.scale(v, [75, 100])
kc = pygame.transform.scale(ck, [100, 200])
jc = pygame.transform.scale(cj, [100, 200])

def ekran():
    pygame.display.flip()
    e.blit(jc,[100,300])
    e.blit(kc,[0,300])
    e.blit(vv,[75,0])
e = pygame.display.set_mode([200, 500])