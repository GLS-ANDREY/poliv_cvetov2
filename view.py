import pygame
import random
import model

v = pygame.image.load("voda.png")
cj = pygame.image.load("joltiy_cvetok.png")
ck = pygame.image.load("krasniy_cvetok.png")
vv = pygame.transform.scale(v, [75, 100])
kc = pygame.transform.scale(ck, [100, 200])
jc = pygame.transform.scale(cj, [100, 200])
def ekran():
    global o,l
    display.fill([0, 0, 0])
    vvv = pygame.transform.scale(v, [model.rect.width, model.rect.height])
    yc = pygame.transform.scale(cj, [model.rectyc.width, model.rectyc.height])
    rc = pygame.transform.scale(kc, [model.rectrc.width, model.rectrc.height])
    display.blit(yc, [model.rectyc.x, model.rectyc.top])
    display.blit(rc, [model.rectrc.x, model.rectrc.top])
    display.blit(vvv, [model.rect.x, model.rect.top])
    pygame.draw.rect(display,[140,209,243],model.rect,4)
    pygame.draw.rect(display,[219,16,0],model.rectyc,4)
    pygame.draw.rect(display,[219,16,0],model.rectrc,4)
    pygame.display.flip()


display = pygame.display.set_mode([200, 500])
