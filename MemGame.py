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

def resetuj_igru(nivo):
    global karte, prva_karta, druga_karta, parovi, pokusaji, kraj_igre, dugme_prikazi, pocetak_vremena, koristi_slova, trenutni_nivo

    redovi, kolone = (4, 4)
    pool = simboli_brojevi
    koristi_slova = False

    if nivo == 'hard':
        pool = slova
        koristi_slova = True

    pozicije = napravi_pozicije_karti(redovi, kolone)
    simboli = generisi_parove(pool, (redovi * kolone) // 2)
    karte = [Karta(simboli[i], pozicije[i]) for i in range(redovi * kolone)]

    prva_karta = None
    druga_karta = None
    parovi = 0
    pokusaji = 0
    kraj_igre = False
    dugme_prikazi = False
    pocetak_vremena = time.time()
    trenutni_nivo = nivo

trenutni_nivo = meni_nivoa()
resetuj_igru(trenutni_nivo)

ekran.blit(pozadina,(0,0))
for k in karte:
    k.otkrivena = True
    k.crtaj(ekran, koristi_slova)
ekran.blit(font_mali.render("Zapamti parove!", True, BIJELO), (10, VISINA - 80))
pygame.display.flip()
pygame.time.wait(3000)
for k in karte:
    k.otkrivena = False

radi = True
sat = pygame.time.Clock()
while radi:
    ekran.blit(pozadina,(0,0))
    proteklo = int(time.time() - pocetak_vremena)

    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            radi = False
        elif dogadjaj.type == pygame.MOUSEBUTTONDOWN:
            if kraj_igre and dugme_nova_igra.collidepoint(dogadjaj.pos):
                trenutni_nivo = meni_nivoa()
                resetuj_igru(trenutni_nivo)
            elif not kraj_igre:
                if prva_karta is None or (prva_karta and druga_karta is None):
                    for k in karte:
                        if k.rect.collidepoint(dogadjaj.pos) and not k.otkrivena and not k.pogodjena:
                            k.otkrivena = True
                            if prva_karta is None:
                                prva_karta = k
                            elif druga_karta is None:
                                druga_karta = k
                                pokusaji += 1

    if prva_karta and druga_karta:
        for k in karte:
            k.crtaj(ekran, koristi_slova)
        pygame.display.flip()
        pygame.time.wait(700)

        if prva_karta.simbol == druga_karta.simbol:
            prva_karta.pogodjena = True
            druga_karta.pogodjena = True
            parovi += 1
        else:
            if trenutni_nivo == 'mix':
                i1 = karte.index(prva_karta)
                i2 = karte.index(druga_karta)

                karte[i1], karte[i2] = karte[i2], karte[i1]

                pozicije = napravi_pozicije_karti(4, 4)
                for i, karta in enumerate(karte):
                    karta.pozicija = pozicije[i]
                    karta.rect.topleft = pozicije[i]

            prva_karta.otkrivena = False
            druga_karta.otkrivena = False

        prva_karta = None
        druga_karta = None

    for k in karte:
        k.crtaj(ekran, koristi_slova)

    info = font_mali.render(f"Pokušaja: {pokusaji}  Vrijeme: {proteklo}s", True, BIJELO)
    ekran.blit(info, (10, VISINA - 80))

    if parovi == len(karte) // 2:
        centrirani_tekst("Pobjeda!", VISINA // 2 - 60, CRVENO)
        pygame.draw.rect(ekran, PLAVO, dugme_nova_igra)
        tekst = font_mali.render("Nova Igra", True, BIJELO)
        ekran.blit(tekst, tekst.get_rect(center=dugme_nova_igra.center))
        kraj_igre = True

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
