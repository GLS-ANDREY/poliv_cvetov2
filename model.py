import pygame
import random
rect = pygame.Rect([75,-200,75,100])
t = 200

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

def po():
    global t
    if rect.bottom >= 500 and rect.top <= 500:
        t += 2
        pygame.display.set_mode([t, 500])


def op():
    global t
    p = t - rect.width
    return random.randint(0, p)


