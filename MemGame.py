import pygame
import random
import time
pygame.init()

SIRINA, VISINA=800, 700
ekran = pygame.display.set_mode((SIRINA, VISINA))
pygame.display.set_caption("Igra Pamćenja")

font_veliki=pygame.font.Font(None, 74)
font_mali=pygame.font.Font(None, 36)
font_znak=pygame.font.SysFont("simhei", 48)

BIJELO=(255, 255, 255)
CRNO=(0, 0, 0)
ZELENO=(0, 200, 0)
CRVENO=(255, 0, 0)
PLAVO=(0, 100, 255)

