import pygame
import random
import model

v = pygame.image.load("voda.png")
cj = pygame.image.load("joltiy_cvetok.png")
ck = pygame.image.load("krasniy_cvetok.png")
vv = pygame.transform.scale(v, [75, 100])
kc = pygame.transform.scale(ck, [100, 200])
jc = pygame.transform.scale(cj, [100, 200])
t = 220

def ekran():
    global t
    display.fill([0, 0, 0])
    vvv = pygame.transform.scale(v, [model.rect.width, model.rect.height])
    if model.rect.bottom >= 500 and model.rect.top <= 500:
        t += 2
        pygame.display.set_mode([t, 500])
    display.blit(jc, [100, 300])
    display.blit(kc, [0, 300])
    display.blit(vvv, [model.rect.x, model.rect.top])
    # pygame.draw.rect(display,[140,209,243],model.rect,4)
    pygame.display.flip()


display = pygame.display.set_mode([200, 500])
