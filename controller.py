import pygame
import model


def allsobitiya():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_DOWN:
            model.speed()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_UP:
            model.speed2()
