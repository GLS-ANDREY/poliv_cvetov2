import pygame
import random
rect = pygame.Rect([75,-200,75,100])
rectyc = pygame.Rect([100,300,100,200])
rectrc = pygame.Rect([0,300,100,200])
t = 200

def speed():
    rect.centery += 30

def speed2():
    rect.centery -= 50

def kaply():
    global t
    rect.centery += 3
    if rect.bottom >= 500 and rect.top <= 500:
        t += 2
        pygame.display.set_mode([t, 500])
    p = t - rect.width
    if rect.top >= 550:
        rect.centery -= 750
        rect.x = random.randint(0,p)
        rect.height = random.randint(10,75)
        rect.width = random.randint(10,75)

def yc():
    if rect.bottom >= 500 and rect.top <= 500:
        rectyc.height += 2
        rectyc.width += 1
        rectyc.x += 1
        rectyc.bottom = 500
    if rectyc.top <= 0 and rect.bottom >= 500 and rect.top <= 500:
        rectyc.height -= 2
        rectyc.width -= 1
        rectyc.x -= 1

def rc():
    if rect.bottom >= 500 and rect.top <= 500:
        rectrc.height += 2
        rectrc.width += 1
        rectrc.bottom = 500
    if rectrc.top <= 0 and rect.bottom >= 500 and rect.top <= 500:
        rectrc.height -= 2
        rectrc.width -= 1