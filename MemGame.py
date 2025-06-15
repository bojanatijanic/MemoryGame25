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

def napravi_pozicije_karti(redova, kolona):
    pozicije = []
    for i in range(redova):
        for j in range(kolona):
            x = RAZMAK + j * (VELICINA_KARTE + RAZMAK)
            y = RAZMAK + i * (VELICINA_KARTE + RAZMAK)
            pozicije.append((x, y))
    return pozicije

def generisi_parove(pool_simbola, broj):
    simboli = random.sample(pool_simbola, broj) * 2
    random.shuffle(simboli)
    return simboli

class Karta:
    def_ini_(self, simbol, pozicija):
        self.simbol = simbol
        self.pozicija = pozicija
        self.rect = pygame.Rect(pozicija[0], pozicija[1], VELICINA_KARTE, VELICINA_KARTE)
        self.otkrivena = False
        self.pogodjena = False

    def crtaj(self, ekran, kineski=False):
        if self.otkrivena or self.pogodjena:
            pygame.draw.rect(ekran, BIJELO, self.rect)
            font = font_znak if kineski else font_veliki
            tekst = font.render(str(self.simbol), True, CRNO)
            tekst_rect = tekst.get_rect(center=self.rect.center)
            ekran.blit(tekst, tekst_rect)
        else:
            pygame.draw.rect(ekran, ZELENO, self.rect)

def centrirani_tekst(tekst, y, boja=CRVENO):
    ispis = font_veliki.render(tekst, True, boja)
    ekran.blit(ispis, (SIRINA // 2 - ispis.get_width() // 2, y))

def meni_nivoa():
    ekran.blit(pozadina,(0,0))
    centrirani_tekst("Izaberi nivo", 100)

    dugme_lako = pygame.Rect(SIRINA // 2 - 150, 230, 300, 60)
    dugme_tesko = pygame.Rect(SIRINA // 2 - 150, 320, 300, 60)
    dugme_mesano = pygame.Rect(SIRINA // 2 - 150, 410, 300, 60)

    pygame.draw.rect(ekran, PLAVO, dugme_lako)
    pygame.draw.rect(ekran, CRVENO, dugme_tesko)
    pygame.draw.rect(ekran, (200, 100, 0), dugme_mesano)

    ekran.blit(font_mali.render("Brojevi", True, BIJELO), (dugme_lako.x+110, dugme_lako.y + 15))
    ekran.blit(font_mali.render("Slova", True, BIJELO), (dugme_tesko.x+120, dugme_tesko.y + 15))
    ekran.blit(font_mali.render("Zamjena karata", True, BIJELO), (dugme_mesano.x + 60, dugme_mesano.y + 15))
    pygame.display.flip()

    while True:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if dugme_lako.collidepoint(dogadjaj.pos):
                    return 'easy'
                elif dugme_tesko.collidepoint(dogadjaj.pos):
                    return 'hard'
                elif dugme_mesano.collidepoint(dogadjaj.pos):
                    return 'mix'


