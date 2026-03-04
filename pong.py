import pygame
import sys


pygame.init()

PRETO= (0, 0, 0)
BRANCO = (255, 255, 255)

largura = 800
altura = 600        

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

player1_x = 15
player1_y = altura // 2 - raquete_altura // 2

player_2 = largura - 15 - raquete_largura
player_2_y = altura // 2 - raquete_altura // 2

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    pygame.draw.rect(tela, BRANCO, (player1_x, player1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (player_2, player_2_y, raquete_largura, raquete_altura))
    pygame.draw.circle(tela, BRANCO, (largura // 2, altura // 2), tamanho_bola)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()




