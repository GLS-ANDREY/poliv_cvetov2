import random

import pygame
import random
rect = pygame.Rect([75,-200,75,100])
def speed():
    rect.centery += 30

def speed2():
    rect.centery -= 50

def ekran2():
    rect.centery += 1
    if rect.top >= 550:
        rect.centery -= 750
        rect.x = random.randint(50,150)
        rect.height = random.randint(10,75)
        rect.width = random.randint(10,75)