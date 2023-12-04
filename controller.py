import pygame
import model
pygame.key.set_repeat(100)

def allsobitiya():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_DOWN:
            model.speed()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_UP:
            model.speed2()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_s:
            pygame.display.set_mode([200, 700])
        if a.type == pygame.KEYDOWN and a.key == pygame.K_w:
            pygame.display.set_mode([700, 700])

