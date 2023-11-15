import pygame

import view


def allsobitiya():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_UP:
            view.xz()