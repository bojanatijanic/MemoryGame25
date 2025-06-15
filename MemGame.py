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

VELICINA_KARTE = 100
RAZMAK = 20

pozadina = pygame.image.load("wp5035280.webp")
pozadina = pygame.transform.scale(pozadina, (SIRINA, VISINA))

kraj_igre = False
dugme_nova_igra = pygame.Rect(SIRINA // 2 - 100, VISINA // 2 + 60, 200, 50)

slova = list("A B C D E F G H I J K L M N O P".split())
simboli_brojevi = list("1 2 3 4 5 6 7 8 9".split())




